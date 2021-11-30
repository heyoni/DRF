from django.shortcuts import get_object_or_404, render, redirect
from .forms import SignupForm, EditForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.views import (
    LoginView, logout_then_login, PasswordChangeView as AuthPasswordChangeView
)
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import User



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            auth_login(request, signed_user)
            messages.success(request, "회원가입 환영합니다.")
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html',{
        'form': form
    })


login = LoginView.as_view(template_name='accounts/login_form.html')


def logout(request):
    messages.success(request,'로그아웃되었습니다.')
    return logout_then_login(request)


@login_required
def edit(request):
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "프로필을 수정하였습니다.")
            return redirect('/')
    else:
        form = EditForm(instance=request.user)
    return render(request, 'accounts/profile_edit_form.html',{
            'form':form
    })



class PasswordChangeView(LoginRequiredMixin, AuthPasswordChangeView):
    success_url = reverse_lazy("password_change")
    template_name = 'accounts/password_change_form.html'
    form_class = PasswordChangeForm

    def form_valid(self, form):
        messages.success(self.request, "암호를 변경했습니다.")
        return super().form_valid(form)

password_change = PasswordChangeView.as_view()


@login_required
def user_follow(request, username):
    follow_user = get_object_or_404(User, username=username, is_active=True)

    request.user.following_set.add(follow_user)
    follow_user.follower_set.add(request.user)

    messages.success(request, f"{follow_user}님을 팔로우 했습니다.")
    redirect_url = request.META.get("HTTP_REFERER", "root")
    return redirect(redirect_url)


@login_required
def user_unfollow(request, username):
    unfollow_user = get_object_or_404(User, username=username, is_active=True)

    request.user.following_set.remove(unfollow_user)
    unfollow_user.follower_set.remove(request.user)

    messages.success(request, f"{unfollow_user}님을 언팔로우 했습니다.")
    redirect_url = request.META.get("HTTP_REFERER", "root")
    return redirect(redirect_url)