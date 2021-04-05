from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    description = models.CharField(max_length=255, verbose_name="Description")
    created_at= models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"

    def __str__(self):
        return self.name
    