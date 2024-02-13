from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth 
from django.contrib import messages

# Create your views here.

def login(request):
    return render (request, "Login.html")

def signin(request):

    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        user_name = request.POST['user_name']
        email_id = request.POST['email']
        password = request.POST['pass1']
        confirm_pass = request.POST['pass2']

        if password ==confirm_pass:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, "User Name is already ragistered")
                return redirect("signin")

            elif User.objects.filter(email = email_id).exists():
                messages.info(request,"Email Id is already ragistered")
                return redirect("signin")

            else:
                user = User.objects.create_user(username=user_name, password = password, email=email_id, first_name=first_name, last_name=last_name)
                user.save();
                messages.info(request, "User created, Please Login with Username and password")
                return redirect("login")
        
        else:
            messages.info(request, "Password not matched")   
            return redirect("signin")


    else:
        return render (request, "Signin.html")