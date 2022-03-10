from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

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
            return render(request, "index.html")

