from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from analytics.models import SocialMediaPlatform, Post, Analytics, SocialMediaAccount

def index(request):
    return render(request, "index.html")

def dashboard(request):
    return render(request, 'dashboard.html')

def posts_analytics(request):
    return render(request, 'posts_analytics.html')

def followers_analytics(request):
    return render(request, 'followers_analytics.html')

def display(request):
    accounts = SocialMediaAccount.objects.all()
    posts = Post.objects.all()
    analytics = Analytics.objects.all()
    return render(request, 'display.html', {'accounts': accounts, 'posts': posts, 'analytics': analytics})
