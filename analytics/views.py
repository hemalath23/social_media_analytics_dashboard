from django.shortcuts import render, get_object_or_404
from .models import SocialMediaAccount, Post, Analytics

def show_account_details(request, username):
    account = get_object_or_404(SocialMediaAccount, username=username)
    return render(request, 'show_details.html', {'account': account})

def show_post_details(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    return render(request, 'show_details.html', {'post': post})

def show_analytics_details(request, username):
    analytics = get_object_or_404(Analytics, account__username=username)
    return render(request, 'show_details.html', {'analytics': analytics})
