from django.shortcuts import render

def home(request):
    return render(request,"header.html")

def Products(request):
    return render(request,"Products.html")

def signin(request):
    return render(request,"signin.html")

def Signup(request):
    return render(request,"signup.html")
