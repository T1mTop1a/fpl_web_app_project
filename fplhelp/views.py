from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    response = render(request, 'fplhelp/index.html')
    return response


def fdr(request):
    response = render(request, 'fplhelp/fdr.html')
    return response