from django.http import HttpResponse
from django.shortcuts import render
from .models import PostForm
# Create your views here.

def post(request):
    pf = PostForm.objects.all()
    return render(request, 'post/post.html', {'pf': pf})


def postDetail(request, id):
    pd = PostForm.objects.get(id=id)
    return render(request, 'post/detail.html', {'pd': pd})