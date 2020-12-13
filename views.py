from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
# Create your views here.
def index(request):
	#return HttpResponse('Blog from Chayan')
	myposts=Blogpost.objects.all()
	print(myposts)
	return render(request,'blog/index.html',{'myposts':myposts},)
def blog(request,id):
	post=Blogpost.objects.filter(post_id=id)[0]
	return render(request,'blog/blog.html',{'post':post},)