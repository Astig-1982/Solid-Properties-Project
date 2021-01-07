from django.contrib import admin
from .models import Services, Category, Main_Category

# Register your models here.
admin.site.register(Services)
admin.site.register(Category)
admin.site.register(Main_Category)
