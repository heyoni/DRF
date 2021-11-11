from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag_set = models.ManyToManyField('Tag')
    # 문자열로 지정해주는 이유 : python은 스크립트언어, 앞에서실행하지 않으면 빨간 줄이 나올수도 있기 때문, Tag라고 써도 됨

    def __str__(self):
        return self.message 

    class Meta:
        ordering=['-id']


class Comment(models.Model):
    # 다른앱의 모델 : '다른앱.post'로 작성
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    message = models.TextField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name