from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'mainapp/index.html',{
        'title':'Home'
    })

def aboutus(request):
    return render(request, 'mainapp/aboutus.html',{
        'title':'About'
    })

def register_page(request):

    register_form = RegisterForm()

    if request.method == "POST":
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()
                messages.success(request,'Success register!')
                return redirect('home')


    return render(request, 'users/register.html',{
        'title':'Sign in',
        'register_form':register_form
    } )