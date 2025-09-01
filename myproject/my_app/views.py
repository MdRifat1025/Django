from django.shortcuts import render,redirect
from authenticate.models import Author
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.hashers import check_password

def home(request):
    return render(request,"header.html")

def Products(request):
    return render(request,"Products.html")

def signin(request):
    if request.method == "POST":
        email= request.POST.get("email")
        password = request.POST.get("passw")

        try:
            user = Author.objects.get(email=email)
        except Author.DoesNotExist:
            messages.error(request, "User not found!")
            return redirect("signin")

        # check password
        if check_password(password, user.passw):
            messages.success(request, "Login successful!")
            return redirect("home")
        else:
            messages.error(request, "Invalid password!")
            return redirect("signin")

    return render(request,"signin.html")

def Signup(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get('email')
        passw=request.POST.get('passw')
        Author.objects.create(username=username,email=email,passw=make_password(passw))
        
        return redirect("signup")
    return render(request,"signup.html")

def about(request):
    return render(request,"about.html")

def category(request):
        
    return render(request,"signup.html")

def about(request):
    return render(request,"about.html")

def category(request):
    return render(request,"category.html")
