from django.shortcuts import render

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

    return render(request, 'users/register.html',{
        'title':'Sign in'
    } )