from django.shortcuts import render
from.models import Image

def index(request):
    return render(request,'minds_app/index.html')

def Agency(request):
    return render(request,'minds_app/agensy.html')

def Blog(request):
    pics=Image.objects.all()
    context={'pics':pics}
    return render(request,'minds_app/blog.html',context)