from email import message
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
import csv
from csv import writer
from datetime import date

# Create your views here.
def index(request):
    return render(request, 'index.html')

def teacher(request):
    if request.user.is_anonymous:
        return render(request, 'tlogin.html')
    return render(request, 'teacher.html')

def student(request):
    return render(request, 'student.html')

def sets(request):
    return render(request, 'set.html')

def check(request):
    return render(request, 'check.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

'''# ================== creating a student login function ======================

def login_student(request):
    if request.method == 'POST':                   # checking if the method is POST
        user = request.POST.get('username')        # storing the value of username in username variable
        passw = request.POST.get('password')       # storing value of the password in the password variable
        
    # ============ authentication =================
        user = authenticate(username = user, password = passw)           # creating instance for aunthentication from models 
        if user is not None :                                            # checking if user is not none 
            login(request, user)                                         # calling login function by passing request and the instance of authentication
            return render(request, "student.html")                       # redirecting to the student webpage on succesful authentication
        else:                                                            
            return render(request, "index.html")                         #returning to homepage 

    return render(request, "index.html")'''


# ==================== creating Teacher login function =========================
def login_teacher(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        passw = request.POST.get('password')

        # ======== authentication ===========

        user = authenticate(username = user, password = passw)
        if user is not None:

            return render(request, "teacher.html")
        
        else:
            messages.error(request, "Please check your username or password , contact admin if problem persists")
    
    else:
        messages.error(request, "")
    return render(request, "teacher_signin.html")


def makePaper(request):
    data = request.GET
    subCode = data['code']
    sem = data['sem']
    sec = data['sec']
    link = data['link']

    splits = link.split("/")
    # print(splits)

    today = date.today()
    d1 = today.strftime("%d%m%Y")
    paperCode = d1 + subCode + sem + sec        # today's data + subject code + semester + section
    
    file = open('papers.csv')
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)

    data = [len(rows), paperCode, splits[6]]
    with open('papers.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(data)
        f_object.close()
    
    return render(request, 'teacher.html', {'code': paperCode})

def startTest(request):
    data = request.POST
    code = data['code']             # paper code
    roll = data['roll']             # roll number
    file = open('papers.csv')
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)

    file1 = open('submission.csv')
    csvreader1 = csv.reader(file1)
    header1 = []
    header1 = next(csvreader1)
    rows1 = []
    for row in csvreader1:
        rows1.append(row)
    
    link = ''
    for i in rows:
        if str(i[1]) == code:
            link = i[2]

    # check if the student has appeared for the paper
    flag = 0;
    for l in range(len(rows1) - 1, -1, -1):
        i = rows1[l]
        if str(i[1]) == roll:
            if str(i[2]) == code:
                if str(i[3]) == '1':
                    # paper submitted by this roll number
                    flag = 1
                    break
                else:
                    flag = 0
                    break

    if (flag == 1):
        # paper submitted
        return render(request, 'test.html', {'code': 1, 'roll': data['roll'], 'paperCode': code})
    else:
        # paper not submitted
        return render(request, 'test.html', {'code': code, 'roll': data['roll'], 'paperCode': link})
    

def submitted(request, roll, code):
    url = (request.path).split("/")
    roll = int(url[2])

    file = open('submission.csv')
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)

    data = [len(rows), roll, code, 1]
    with open('submission.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(data)
        f_object.close()
        

    return render(request, 'test.html', {'code': 1})