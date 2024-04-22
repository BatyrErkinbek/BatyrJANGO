from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'templates/btr/indd.html')


def about(request):
    return HttpResponse("<h4>o nas</h4>")
