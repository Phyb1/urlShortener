from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'page/index.html')

def about(request):
    return render(request, 'page/about.html')

def result(request):
    return render(request, 'page/result.html')