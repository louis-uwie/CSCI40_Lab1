from django.shortcuts import render
from django.http import HttpResponse

def recipe_list(request):

    return HttpResponse("this is just a test")

def recipe_1(request):

    return HttpResponse("this is just a test for recipe1")