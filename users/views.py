from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)
            return redirect("dashboard")

        messages.error(request, "Invalid username or password.")

    return render(request, "registration/login.html")


def register_view(request):

    if request.method == "POST":

        username = request.POST["username"].strip()
        email = request.POST["email"].strip()
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        # Username exists
        if User.objects.filter(username=username).exists():

            messages.error(request, "Username already exists.")
            return redirect("register")

        # Email exists
        if User.objects.filter(email=email).exists():

            messages.error(request, "Email already registered.")
            return redirect("register")

        # Validate email format
        try:
            validate_email(email)
        except ValidationError:

            messages.error(request, "Enter a valid email address.")
            return redirect("register")

        # Confirm password
        if password != confirm_password:

            messages.error(request, "Passwords do not match.")
            return redirect("register")

        # Create user
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully.")
        return redirect("login")

    return render(request, "registration/register.html")


def logout_view(request):

    logout(request)
    return redirect("home")