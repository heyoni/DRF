from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm

urlpatterns = [
    path('login/', LoginView.as_view(
        form_class = LoginForm,
        template_name='accounts/login_form.html'
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/',views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('signup/', views.signup,'name=signup'),
] 