from django.shortcuts import render

# Create your views here.

def table1(request):
    return render(request,"table1.html")

def table2(request):
    return render(request,"table2.html")
