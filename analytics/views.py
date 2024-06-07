from django.shortcuts import render, get_object_or_404
from .models import SocialMediaAccount, Post, Analytics

def show_all_details(request):
    accounts = SocialMediaAccount.objects.all()
    posts = Post.objects.all()
    analytics = Analytics.objects.all()
    return render(request, 'display.html', {'accounts': accounts, 'posts': posts, 'analytics': analytics})

def show_details(request, username=None, post_id=None, detail_type=None):
    context = {}
    
    if detail_type == 'account':
        account = get_object_or_404(SocialMediaAccount, username=username)
        context['account'] = account
    elif detail_type == 'post':
        post = get_object_or_404(Post, post_id=post_id)
        context['post'] = post
    elif detail_type == 'analytics':
        analytics = get_object_or_404(Analytics, account__username=username)
        context['analytics'] = analytics
    
    return render(request, 'show_details.html', context)
