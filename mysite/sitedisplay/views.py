from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def blog(request):
    return HttpResponse('blog')

def post(request,slug):
    return HttpResponse('post')
def product(request,class_slug,slug):
    return HttpResponse('product')

def product_class(request,slug):
    return HttpResponse('product_class')
