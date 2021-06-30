from datetime import time
from django import http
from django.shortcuts import render
from django.http import HttpResponse, response, HttpResponseRedirect
from pasteleria.models import Ciudad, Cliente, Comuna, Producto
from django.utils import timezone
from django.urls import reverse


def index(request):
    return render(request,'cliente/index.html')