from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView
from app.forms import *
from django.http import HttpResponse

class Student_form_data(FormView):
    template_name='Student_form_data.html'
    form_class=StudentForm

    def form_valid(self, form):
        data=form.cleaned_data
        return HttpResponse(str(data))
    

class insert_data_hemabflist(FormView):
    template_name='insert_data_hemabflist.html'
    form_class=hemabflistForm

    def form_valid(self, form):
        form.save()
        return HttpResponse('insert_data_hemabflist is done successfully')






