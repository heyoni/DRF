from django.urls import path
from . import views

urlpatterns=[
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'), # /accounts/login/ -> settings.login_url의 설정값도 이 문자열로 되어있다. 그래서 @login_required를 이 설정값 때문에 사용할 수 있게 됨
    path('logout/',views.logout, name='logout'),
    path('edit/',views.edit, name='edit'),
]