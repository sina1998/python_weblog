# python_blog/urls.py

from django.urls import path
from .views import home, post, signup
from .api.views import PostListView, CreatePostView
from .api.urls import *


from django.urls import path, include

urlpatterns = [
    path('', home, name='home'),
    path('post/', post, name='post'),
    path('signup/', signup, name='signup'),
    path('api/', include('python_blog.api.urls')),
]

