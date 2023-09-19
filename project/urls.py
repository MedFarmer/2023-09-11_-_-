from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('login/', Login.as_view(), name='login'),
    path('students/', StudentView.as_view(), name='students'),
    path('add_student/', StudentCreate.as_view(), name='studentcreate'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('logout/', Logout.as_view(), name='logout'),
    path('users/', Users.as_view(), name='users'),
]
