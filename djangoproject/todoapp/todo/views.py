from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(request):
    contextdic = {"datakey" : "datavalue"}
    return render(request, 'todo/homepage.html', contextdic)

def about_us_page(request):
    clients_list = [
        {
        "name" : "Testname1",
        "family" : "testfamily1",
        "age" : "2221", 
        },
        {
        "name" : "Testname2",
        "family" : "testfamily2",
        "age" : "2222", 
        },
        {
        "name" : "Testname3",
        "family" : "testfamily3",
        "age" : "2223", 
        },
    ]
    contextdic = {
        'clientlist' : clients_list
    }
    return render(request, 'todo/aboutus.html', contextdic)

def client_info(request, clientid):
    clients_dic = {
        "1" : {
        "name" : "Testname1",
        "family" : "testfamily1",
        "age" : "2221", 
        },
        "2" : {
        "name" : "Testname2",
        "family" : "testfamily2",
        "age" : "2222", 
        },
        "3" : {
        "name" : "Testname3",
        "family" : "testfamily3",
        "age" : "2223", 
        },
    }
    target_client = clients_dic[str(clientid)]
    return render(request, 'todo/clients.html', target_client)
   