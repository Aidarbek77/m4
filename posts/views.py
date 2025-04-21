from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

def test_review(request):
    return('hello world')

def html_view(request): 
    return render(request, "base.html" )

