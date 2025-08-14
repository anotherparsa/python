from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(request):
    contextdic = {"datakey" : "datavalue"}
    return render(request, 'todo/homepage.html', contextdic)

def about_us_page(request):
    return render(request, 'todo/aboutus.html')