from django.shortcuts import render
from .models import Post
from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import DetailView


def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q','')
    if q:
        qs = qs.filter(message__icontains=q)
    
    return render(request, 'instagram/post_list.html', {
        'post_list' : qs,
        'q':q
    })


# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     # try:
#     #     post = get_object_or_404(Post, pk=pk)
#     # except Post.DoesNotExist: # post가 없으면 404 에러를 띄움
#     #     raise Http404

#     # 위 내용과 아래 내용은 같은의미다!
#     post = get_object_or_404(Post,pk=pk)

#     return render(request, 'instagram/post_detail.html', {
#         'post': post,
#         'object': post,
#     })

# 위 내용과 아래 내용은 같다!
post_detail = DetailView.as_view(model=Post)