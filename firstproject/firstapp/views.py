from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "index1.html")


def dynamic(request, courseid):
    return HttpResponse(courseid)
