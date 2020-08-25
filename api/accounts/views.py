from django.shortcuts import render
from django.http import  HttpResponse

def home(request):
    # The django will search for accounts/dashboard.html on api/accounts/templates
    return render(request, 'accounts/dashboard.html')

def products(request):
    return HttpResponse('products')

def customer(request):
    return HttpResponse('customer')
