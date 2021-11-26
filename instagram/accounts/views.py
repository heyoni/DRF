from django.shortcuts import render, redirect
from .forms import SignupForm, EditForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required


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
            edited_user = form.save()
            messages.success(request, "프로필을 수정하였습니다.")
            return redirect('/')
    else:
        form = EditForm(instance=request.user)
        return render(request, 'accounts/profile_edit_form.html',{
            'form':form
        })