import json
from django.shortcuts import render
from urllib3 import HTTPResponse
from django.http import JsonResponse

# Create your views here.
def index(request):
     return render(request, 'index.html')

def counter(request):
     text = request.POST['text']
     count = len(text.split(" "))
     return render(request, 'counter.html', {'count': count})