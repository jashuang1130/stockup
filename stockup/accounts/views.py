from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    template = 'accounts/dashboard.html'
    context = {'test': 'new'}
    context['page_name'] = 'Dashboard'
    return render(request, template, context)

def products(request):
    template = 'accounts/products.html'
    context = {'test': 'new'}
    context['page_name'] = 'Products'
    return render(request, template, context)

def customers(request):
    template = 'accounts/customers.html'
    context = {'test': 'new'}
    context['page_name'] = 'Customers'
    return render(request, template, context)
