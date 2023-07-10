from django.http import HttpResponse
from django.shortcuts import render, redirect

from Bankingapp.models import Login


def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        name = request.POST.get('name', )
        desc = request.POST.get('desc', )
        login = Login(name=name, desc=desc)
        return redirect('signin')
    return  render(request,'login.html')
def register(request):
    if request.method == 'POST':
        return redirect('login')
    return render(request,'register.html')
def signin(request):
    if request.method == 'POST':
        return redirect('login')
    return render(request,'signin.html')
def palakkad(request):
    return render(request,'palakkad.html')
def thrissur(request):
    return render(request,'thrissur.html')
def malappuram(request):
    return render(request,'malappuram.html')
def cochin(request):
    return render(request,'cochin.html')
def bangalore(request):
    return render(request,'bangalore.html')
def kozhikode(request):
    return render(request,'kozhikode.html')

# Create your views here.
