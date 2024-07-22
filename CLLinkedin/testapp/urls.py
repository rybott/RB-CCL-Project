from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="home"),
    path('login1/',views.login_employee, name="login1" )
]
