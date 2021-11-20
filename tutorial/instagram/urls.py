from django.urls import path
from . import views
from .views import PostDeleteView, PostDetailView, PostUpdateView, PostListView
from django.urls import path, re_path, register_converter
from .converters import YearConverter, MonthConverter, DayConverter

register_converter(YearConverter, 'year')
register_converter(MonthConverter, 'month')
register_converter(DayConverter, 'day')


app_name = 'instagram'  # URL Reverse에서 namespace역할을 하게 됩니다.
# app_name='instagram'
urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),    
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/update/',PostUpdateView.as_view(),name='post_edit'),
    path('<int:pk>/delete/',PostDeleteView.as_view(),name='post_delete'),


    path('archive/', views.post_archive, name='post_archive'),
    path('archive/<year:year>/', views.post_archive_year, name='post_archive_year'),
    path('archive/<year:year>/<month:month>/', views.post_archive_year, name='post_archive_year'),
    path('archive/<year:year>/<month:month>/<day:day>/', views.post_archive_year, name='post_archive_year'),
    path('new/', views.post_new, name='post_new'),

]   

