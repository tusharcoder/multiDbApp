from django.shortcuts import render

# Create your views here.
from core.models import TestData

def getTestData(request):
    """returns the test data from all the databases"""
    raise NotImplementedError
