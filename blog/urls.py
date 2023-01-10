from django.urls import path
from.views import Home, Detail

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("<slug:slug>", Detail.as_view(), name="detail")
]