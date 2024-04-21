from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def d2(request):

    d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
    return HttpResponse(d)