from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def d3(request):

    s = {10, 20, 30, 40, 50}
    return HttpResponse(s)