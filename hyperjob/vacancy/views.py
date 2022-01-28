from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from vacancy import models

def vacancies(request):
    vacancy_dict = {}
    vacancy_list = []
    for rec in models.Vacancy.objects.filter():
        vacancy_list.append(rec)
    vacancy_dict['vacancies'] = vacancy_list

    return render(request, 'vacancy/vacancy.html', vacancy_dict)

def vacancy_new(request):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    description = request.POST['description']
    models.Vacancy.objects.create(description=description, author=request.user)  
    return render(request, 'hyperjob/index.html')  
