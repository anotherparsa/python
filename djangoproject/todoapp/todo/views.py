from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(request):
    return render(request, 'todo/homepage.html')

def about_us_page(request):
    return render(request, 'todo/aboutus.html')