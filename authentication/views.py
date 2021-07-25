from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.views.generic import TemplateView


# Register View
class RegisterView(TemplateView):
    template_name = "register.html"

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect("Home")


# Register User
def create_user(request):
    if request.method == "POST":
        # Create User
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        username = request.POST['user-name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('Register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('Register')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password
                )
                user.save()
                login_user = authenticate(username=username, password=password)
                django_login(request, login_user)
                messages.success(request, 'User has been registered and logged in successfully !')
                return redirect('Home')

        else:
            messages.info(request, 'Password does not match')
            return redirect('Register')


# Sign-In View
class SignInView(TemplateView):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect("Home")


# Authenticate User
def login(request):
    if request.method == "POST":
        login_user = authenticate(username=request.POST['username'], password=request.POST['password'])
        django_login(request, login_user)
        return redirect('Home')
    else:
        return redirect('Login')


# Reset Password View
class ForgotPasswordView(TemplateView):
    template_name = "forgot_password.html"

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect("Home")


# Reset Password
def reset_pass(request):
    if request.method == 'POST':
        if request.POST['new-password'] == request.POST['confirm-password']:
            if User.objects.filter(email=request.POST['registered-email']).exists():
                user = User.objects.get(email__exact=request.POST['registered-email'])
                user.set_password(request.POST['new-password'])
                user.save()
                messages.success(request, 'Password updated successfully!')
                return redirect('Login')
            else:
                messages.error(request, 'The provided email could not be found in the database!')
                return redirect('Reset-Password')
        else:
            messages.error(request, 'Password does not match')
            return redirect('Reset-Password')
    else:
        messages.error(request, 'Something went wrong please try after some time.')
        return redirect("Reset-Password")


# Logout Authenticated User
def logout(request):
    django_logout(request)
    request.session.flush()
    return redirect('Login')
