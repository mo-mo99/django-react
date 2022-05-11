from email.policy import HTTP
from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import Content_form


def index(request):
    if request.method == "POST":
        form = Content_form(data = request.POST, files = request.FILES)
        if form.is_valid():
            
            form.save()
            return HttpResponse("<h1>uploaded </h1>")
    else:
        form = Content_form()
    content = Content.objects.all()
    return render(request, "index.html", {'content': content, 'form': form})
