from django.shortcuts import render 
from django.http import HttpResponse



def index(request):
    return render(request,"index.html")

def dashboard(request):
    return render(request,'dashboard.html')

def posts_analytics(request):
    
    return render(request, 'posts_analytics.html')

def followers_analytics(request):
    
    return render(request, 'followers_analytics.html')

# def engagement_analytics(request):
#     # Context can include data related to engagement analytics
#     context = {
#         'title': 'Engagement Analytics',
#         # Include other data as needed
#     }
#     return render(request, 'analytics/engagement_analytics.html', context)
