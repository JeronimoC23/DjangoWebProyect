from django.urls import path
from . import views 

urlpatterns = [
    path('articles/', views.list, name="list"),
]