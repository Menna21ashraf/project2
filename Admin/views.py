from django.shortcuts import render 
# Create your views here.
from .models import product
from django.views.generic import ListView
from django.core.mail import send_mail
from django.conf import settings


def displayPro(request):
    x= product.objects.all()
    return render(request,'Admin/listproduct.html',{'Products':x})


def displaySingle(request):
    x= product.objects.all()
    return render(request,'Admin/single.html',{'Products':x})



def viewpro(request):
    q=request.GET['q']
    data=product.objects.filter(description__contains=q).order_by('-name')
    return render(request,'secProject/products.html',{'data':data})





from django.contrib.auth.forms import UserCreationForm
def signme(request):
    form= UserCreationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        

    return render(request,'secProject/signup.html',{'form':form})    


def email(request):
    
    if request.method=='POST':
        subject=request.POST['subject']
        email=request.POST['email']
        message=request.POST['massage']

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],

        )

    return render(request,'secProject/con1.html')    