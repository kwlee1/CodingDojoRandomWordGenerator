# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    context = {
        'attempt': request.session['attempt'],
        'random': get_random_string(length=14)
    }
    return render(request,'rwg/index.html',context)

def gen(request):
    if 'attempt' not in request.session:
        request.session['attempt'] = 1
    else:
        request.session['attempt'] += 1 
    print request.session['attempt']
    return redirect('/')