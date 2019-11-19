from django.shortcuts import render
from .models import Post



def post_list(request):
    post = Post.objects.all()


    return render(request, 'here/post_list.html', {'posts':post})

# Create your views here.
