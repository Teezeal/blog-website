from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages 
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hi {username}, your account was crated successfully!!!")
            return redirect("home")
    else:
        form = UserRegistrationForm()

    context = {
        "form" : form
    }
    return render(request, "user/register.html", context)



def register2(request):
    if request.method == "POST":
        username = request.POST.get("username")                       
        email = request.POST.get("email")    
        password1 = request.POST.get("password1")    
        password2 = request.POST.get("password2")

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exist")
                return redirect("register2")  
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username is taken already")
                return redirect("register2")  
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, f"Hi {username}, Your account was crated successfully!!!")
                return redirect("home")
        else:
            messages.info(request, "Password do not match")
            return redirect("register2")    
    return render(request, "user/register2.html")

