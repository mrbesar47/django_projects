from django.shortcuts import render
from django.http import HttpResponse
import random


def generator(request):
    return render(request, 'generator/generator.html')


def password(request):

    characters = list('abcdefghijklmopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMOPQRSTUVXYZ'))
    if request.GET.get('special'):
        characters.extend(list('~!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 8))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password1': thepassword})
