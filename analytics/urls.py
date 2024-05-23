from django.urls import path
from .views import show_account_details, show_post_details, show_analytics_details

app_name = 'analytics'

urlpatterns = [
    path('account/<str:username>/', show_account_details, name='account_details'),
    path('post/<str:post_id>/', show_post_details, name='post_details'),
    path('analytics/<str:username>/', show_analytics_details, name='analytics_details'),
]
