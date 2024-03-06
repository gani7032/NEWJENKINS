from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    x="This is jenkins pratices"
    return HttpResponse(x)