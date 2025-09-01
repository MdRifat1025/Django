from django.contrib import admin
from .models import Author


class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','passw')
# Register your models here.
admin.site.register(Author,UserAdmin)