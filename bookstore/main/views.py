from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

import datetime

def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    now = datetime.datetime.now()
    if now.hour > 12:
        msg = '午安'
    else:
        msg = '早安'
    context = {'msg':msg}
    return render(request, 'main/main.html', context)
