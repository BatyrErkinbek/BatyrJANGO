from django.shortcuts import render


def index(request):
    return render(request, 'btr/indd.html')


def about(request):
    return render(request,'btr/about.html')
