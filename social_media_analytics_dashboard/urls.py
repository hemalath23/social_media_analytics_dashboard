from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from social_media_analytics_dashboard.views import index, dashboard, posts_analytics, followers_analytics



urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('', dashboard, name='dashboard'),
    path('posts/', posts_analytics, name='posts_analytics'),
    path('followers/', followers_analytics, name='followers_analytics'),
    path('followers/', followers_analytics, name='followers_analytics'),
    path('analytics/', include('analytics.urls')),  # Include the analytics app's URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
