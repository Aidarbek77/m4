from django.shortcuts import render
from django.http import HttpResponse

def test_review(request):
    return HttpResponse('hello world')

def html_view(request): 
    return render(request, "base.html" )
