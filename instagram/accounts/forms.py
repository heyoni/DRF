from .models import User
from django import forms
from django.contrib.auth.forms import (
    UserCreationForm, UserChangeForm, PasswordChangeForm as AuthPasswordChangeForm
    )
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class SignupForm(UserCreationForm):
    # UserCreationForm 쓰기전
    # class Meta:
    #     model = User
    #     fields = ['username', 'password']

    # 쓴 후
    def __init__(self, *args, **kwargs):
        # 부모 호출
        super().__init__(*args, **kwargs)
        # 모델이 만들어지고 나서 form에서도 변화를 줄 수 있음
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email','first_name','last_name']

    # 중복 방지
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError("이미 등록된 이메일 주소입니다.")
        return email


# class EditForm(UserChangeForm):
#     class Meta:
#         model = get_user_model()
#         fields = ['first_name','last_name','picture','bio', 'website_url','phone_number','gender']

class EditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','picture','bio', 'website_url','phone_number','gender']


class PasswordChangeForm(AuthPasswordChangeForm):
    def clean_new_password1(self):
        old_password = self.cleaned_data.get('old_password')
        new_password1 = self.cleaned_data.get('new_password1')
        if old_password and new_password1:
            if old_password == new_password1:
                raise forms.ValidationError("새로운 암호는 기존 암호과 다르게 입력해주세요.")
        return new_password1

 