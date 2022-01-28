"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from resume import views as resume_views
from vacancy import views as vacancy_views
from django.views.generic import RedirectView
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'

class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'signup.html'

urlpatterns = [
    path("", resume_views.menu),
    path("home", resume_views.home),
    path("vacancies", vacancy_views.vacancies),
    path("resumes", resume_views.resumes),
    path("vacancy/new", vacancy_views.vacancy_new),
    path("resume/new", resume_views.resume_new),
    path('login', MyLoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('signup', MySignupView.as_view()),
    path('login/', RedirectView.as_view(url='/login')),
    path('logout/', RedirectView.as_view(url='/logout')),
    path('signup/', RedirectView.as_view(url='/signup')),
    path('admin/', admin.site.urls),  
]
