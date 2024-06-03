from django.shortcuts import render
from django.views import View
from .models import *
# Create your views here.


def index(request):
    return render(request, 'products/index.html', {})