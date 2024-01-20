from django.urls import path
from .views import *

urlpatterns = [
    
    path('', registerpage , name="registerpage"),
    path('register/', register , name="register"),
    path('loginpage/', loginpage , name="loginpage"),
    path('login/', login , name="login"),
    path('logout/', logout , name="logout"),

    path('insert/',insert,name='insert'),
    path('queryshow/<str:pk>',queryshow,name='queryshow'),
    path('delete/<int:pk>',delete,name='delete'),
    path('edit/<int:pk>',edit,name='edit'),
    path('update/<int:pk>',update,name='update')

]
