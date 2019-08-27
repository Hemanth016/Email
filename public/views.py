# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response,HttpResponsePermanentRedirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings


# Create your views here.
def index(request):
    if request.method=='POST':
        message=request.POST['message']
        send_mail('Friend',
        message,
        settings.EMAIL_HOST_USER,
        ['poojarir86@gmail.com'],
        fail_silently=False)
        print("succesfull")
    return render(request,'public/email.html')
