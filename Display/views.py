from django.shortcuts import render

# Create your views here.
def Home(req):
    return render(req, 'Dashobard.html')

def Camera(req):
    return render(req, 'Camera.html')