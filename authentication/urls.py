from django.urls import path
from .views import \
    RegisterView, SignInView, ForgotPasswordView, \
    create_user, login, logout, reset_pass

urlpatterns = [
    path('register/', RegisterView.as_view(), name='Register'),
    path('register-user/', create_user, name='Register-User'),
    path('login/', SignInView.as_view(), name='Login'),
    path('login-user/', login, name='Login-User'),
    path('logout/', logout, name='Logout'),
    path('reset-password/', ForgotPasswordView.as_view(), name='Reset-Password'),
    path('update-password/', reset_pass, name='Reset-Pass'),
]
