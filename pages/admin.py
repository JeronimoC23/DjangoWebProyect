from django.contrib import admin
from .models import Page
# Register your models here.

admin.site.register(Page)

title = "Django Web Proyect by Jeronimo Clinaz"
subtitle = "Management Panel"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle