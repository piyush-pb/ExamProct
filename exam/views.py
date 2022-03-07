from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def teacher(request):
    return render(request, 'teacher.html')

def student(request):
    return render(request, 'student.html')

def sets(request):
    return render(request, 'set.html')

def check(request):
    return render(request, 'check.html')

def make(request):
    print("Hiiiiiiii")