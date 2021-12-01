from django.urls import path, re_path
from . import views
from django.contrib.auth.validators import UnicodeUsernameValidator


app_name = 'instagram'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/like', views.post_like, name='post_like'),
    path('post/<int:pk>/unlike', views.post_unlike, name='post_unlike'),
    path('post/<int:post_pk>/comment/new/', views.comment_new, name='comment_new'),

    re_path(r'^(?P<username>[\w.@+-]+)/$', views.user_page, name='user_page'),

]
