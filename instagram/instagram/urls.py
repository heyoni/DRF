from django.urls import path
from . import views

app_name = 'instagram'

urlpatterns = [
    path('post/create/', views.create_post, name='create_post')
]
