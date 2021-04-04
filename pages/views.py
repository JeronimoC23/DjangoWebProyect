from django.shortcuts import render

# Create your views here.

def page(request):
    return render (request, "pages/page.html",{
        "page":"Holamundo desde app page",
        "title":"Pagina individual"
    })