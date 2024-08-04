from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="home"),
    path('loginn/',views.login_employee, name="loginn" ),
    path('register/', views.register_employee, name="register")
]
