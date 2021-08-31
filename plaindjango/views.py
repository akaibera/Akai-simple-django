from django.http.response import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def pallabdef(*args, **kwargs):
    #print("akai")
    #return HttpResponse("<h1>Akai is a bad boy<h1>")
    return HttpResponse("<h1>pallab is a bad boy<h1>")
