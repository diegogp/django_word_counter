import json
from django.shortcuts import render
from urllib3 import HTTPResponse
from django.http import JsonResponse
from .models import Feature

# Create your views here.
def index(request):
     feature1 = Feature()
     feature1.id = 0
     feature1.name = 'Fast'
     feature1.details = 'Our service is very quick'
     return render(request, 'index.html', {'feature': feature1})

def counter(request):
     text = request.POST['text']
     count = len(text.split(" "))
     return render(request, 'counter.html', {'count': count})