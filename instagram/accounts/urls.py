from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'), # /accounts/login/ -> settings.login_url의 설정값도 이 문자열로 되어있다. 그래서 @login_required를 이 설정값 때문에 사용할 수 있게 됨
    path('logout/',views.logout, name='logout'),
    path('edit/',views.edit, name='profile_edit'),
    path('password_change/',auth_views.PasswordChangeView.as_view(), name='password_change'),

    re_path(r'^(?P<username>[\w.@+-]+)/follow/$', views.user_follow, name='user_follow'),
    re_path(r'^(?P<username>[\w.@+-]+)/unfollow/$', views.user_unfollow, name='user_unfollow'),


    

]