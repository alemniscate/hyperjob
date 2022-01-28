from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect
from resume import models

def menu(request):
    return render(request, 'hyperjob/index.html')

def home(request):
    if request.user.is_staff:
        return render(request, 'vacancy/home.html')
    else:
        return render(request, 'resume/home.html')

def resumes(request):
    resume_dict = {}
    resume_list = []
    for rec in models.Resume.objects.filter():
        resume_list.append(rec)
    resume_dict['resumes'] = resume_list

    return render(request, 'resume/resume.html', resume_dict)

def resume_new(request):
    if request.user.is_staff:
        return HttpResponseForbidden()
    description = request.POST['description']
    models.Resume.objects.create(description=description, author=request.user)  
    return render(request, 'hyperjob/index.html')
    
