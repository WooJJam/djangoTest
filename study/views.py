from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def center_sort(request) :
    return render(request, 'study/sort.html')
