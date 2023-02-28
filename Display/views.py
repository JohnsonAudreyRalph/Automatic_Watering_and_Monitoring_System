from django.shortcuts import render
# from .Image_Processing import *

# Create your views here.
def Home(req):
    return render(req, 'Dashobard.html')

def Camera(req):
    return render(req, 'Camera.html')