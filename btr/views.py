from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h4>Zhums step tur</h4>")

def about(request):
    return HttpResponse("<h4>o nas</h4>")
