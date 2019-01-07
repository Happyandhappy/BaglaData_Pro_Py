from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, "alphaVantage/index.html")
