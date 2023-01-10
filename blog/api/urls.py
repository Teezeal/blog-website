from django.urls import path
from .views import api_home_view, api_detail_view


urlpatterns = [
    path("home", api_home_view, name="api-home"),
    path("detail", api_detail_view, name="api-detail")
]