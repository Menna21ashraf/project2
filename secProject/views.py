
from django.shortcuts import render

def home(request):
    return render(request,'secProject/Home.html',)


def contact(request):
    return render(request,'secProject/con1.html',)


def logIN(request):
    return render(request,'secProject/login.html',)  



def products(request):
    return render(request,'secProject/products.html',)

def signup(request):
    return render(request,'secProject/signup.html',)


def Sproducts(request):
    return render(request,'secProject/Sproducts.html',)




