from django.urls import path
from .views import show_all_details, show_details

app_name = 'analytics'

urlpatterns = [
    path('all-details/', show_all_details, name='all_details'),
    path('account/<str:username>/', show_details, {'detail_type': 'account'}, name='account_details'),
    path('post/<str:post_id>/', show_details, {'detail_type': 'post'}, name='post_details'),
    path('analytics/<str:username>/', show_details, {'detail_type': 'analytics'}, name='analytics_details'),
]
