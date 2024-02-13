from django.urls import path
from . import views

urlpatterns = [
    path('Login/', views.login, name = "login"),
    path('Signin/', views.signin, name = "signin"),
]
