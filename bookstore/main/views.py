from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    tt = [1,2,3,4,5]
    
    
    return HttpResponse(tt)