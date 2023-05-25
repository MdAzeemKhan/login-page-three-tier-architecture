from django.shortcuts import render,redirect
from .models import Candidate

# Create your views here.
def index(requests):
    return render(requests,'index.html')

def login(requests):
    if requests.method=='POST':
        email=requests.POST.get("email")
        password=requests.POST.get("password")

        user=Candidate.objects.filter(email=email,password=password)
        if user:
            return render(requests,"index.html")
        else:
            return redirect("login")
        
    if requests.method=='GET':
        return render(requests,'login.html')
    

def register(requests):
    if requests.method=='POST':
        name=requests.POST.get('name')
        city=requests.POST.get('city')
        email=requests.POST.get('email')
        password=requests.POST.get('password')

        ob1=Candidate.objects.create(name=name,city=city,email=email,password=password)
        if ob1:
            ob1.save()
            return render(requests,'login.html')
        else:
            return render(requests,'register.html')
        
    elif requests.method=='GET':
        return render(requests,"register.html")
    