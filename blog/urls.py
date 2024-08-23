from django.urls import path
from . import views
app_name = 'blog'

urlpatterns = [
# post views
    path('', views.post_list, name='post_list'),
    path('blog/', include('blog.urls', namespace='blog')),
]