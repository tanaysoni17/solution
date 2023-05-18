from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def innovation(request):
    return render(request, 'FIRSTAPPLICATION/innovation.html')
