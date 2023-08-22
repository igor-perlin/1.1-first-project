import os
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, reverse
from os import listdir


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


# def time_view(request):
#     current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     msg = f'Текущее время: {current_time}'
#     return HttpResponse(msg)

def time_view(request):
    # Получаем текущее время
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Передаем текущее время как контекст в шаблон
    context = {'current_time': current_time}
    return render(request, 'app/time.html', context)


# def workdir_view(request):
#     workdir = os.listdir()
#     workdir_content = '\n'.join(workdir)
#     return HttpResponse(workdir_content)

def workdir_view(request):
    # Получаем список файлов в рабочей директории
    files = listdir('.')

    # Передаем список файлов как контекст в шаблон
    context = {'files': files}
    return render(request, 'app/dir.html', context)

