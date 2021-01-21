from django.urls import path, include
from .views import all_blog, details

app_name = 'blog'

urlpatterns = [
    path('', all_blog, name = 'all_blogs'),
    path('<int:blog_id>/', details, name = 'details'),
]