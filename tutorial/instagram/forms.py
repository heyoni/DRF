from django import forms
from .models import Post
import re

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', 'photo', 'tag_set', 'is_public']
        # exclude = [] #추천하지 않음, 특정필드를 배재하는 건데, 새로운 필드 생성하면 바로 노출되므로 추천x

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message:
            message = re.sub(r'[a-zA-Z]+', '', message)
        return message