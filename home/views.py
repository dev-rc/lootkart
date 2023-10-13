from django.http import HttpResponse
from django.shortcuts import render
from Products.models import *
# Create your views here.

def home(request):
    if(request.method == 'GET'):
        category = Category.objects.all()
        return render(request, 'landing_page.html', {'categories': category})
    else:
        category = Category.objects.all()
    return HttpResponse("Categories are " + str(category))