from django.urls import path
from . import views
from app_one.dash_apps.finished_apps import simpleexample


urlpatterns = [
    path('', views.home, name='home')

]