# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Practice

# Create your views here.

class MarkDown(TemplateView):
    template_name = 'week4.html'

    def get_context_data(self, **kwargs):
        markdowntext = open('p2app/templates/hello.md').read()

        context = super(MarkDown, self).get_context_data(**kwargs)
        context['markdowntext'] = markdowntext

        return context


def home(request):
    
    context = {
        'practices' : Practice.objects.all()
    }
    
    return render(request, 'week4.html' , context)



def login(request):
    return render(request, 'login.html')

def project(request):
    return render(request, 'project.html')

def shop(request):
    return render(request, 'shop.html')

def lesson(request):
    return render(request, 'lesson.html')


