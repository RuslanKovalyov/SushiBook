from django.http import request
from django.shortcuts import render, redirect

from main.models import Job                                 # move mode local dir

def jobs(request):
    jobs = Job.objects.order_by('-id')
    return render(request, 'job/jobs.html', { 'jobs':jobs })