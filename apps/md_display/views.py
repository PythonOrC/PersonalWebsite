from django.shortcuts import render
from .models import Post
# Create your views here.
def researches(request):
    return render(request, 'researches.html', {"posts": Post.objects.all()})

def detail(request, slug):
    return render(request, 'research.html', {"post": Post.objects.get(id=slug)})