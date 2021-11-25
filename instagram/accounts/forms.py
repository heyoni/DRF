from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


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