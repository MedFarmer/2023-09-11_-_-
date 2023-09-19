from django.shortcuts import render
from .models import Student
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.forms import ModelForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from typing import Any

class StudentView(ListView):
    model = Student
    template_name = 'students.html'
    context_object_name = 'students'

class StudentForm(ModelForm):
    class Meta:
        model = Student        
        fields = '__all__'

class StudentCreate(PermissionRequiredMixin, CreateView):
    model = Student
    permission_required = ('all.add_student')
    form_class = StudentForm
    template_name = 'add_student.html'
    success_url = reverse_lazy('students')

class SignUp(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class Login(LoginView):
    template_name = 'login.html'
    next_page = 'students'

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('students'))
        else:
            return super().get(request, *args, **kwargs)

class Logout(LogoutView):
    next_page = 'home'

class HomeView(ListView):
    model = Student
    template_name = 'home.html'
    context_object_name = 'students'

class Users(ListView):
    model = User
    template_name = 'users.html'
    context_object_name = 'users'
    