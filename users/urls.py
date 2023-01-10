from django.urls import path
from .views import register, register2

urlpatterns = [
    path("register/", register, name="register"),
    path("register2/", register2, name="register2")
]