from django.db import models
from django.shortcuts import render
from .models import Post
from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import DetailView, ListView


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
# post_detail = DetailView.as_view(
#   model=Post,
#   queryset=Post.objects.filter(is_public=True) # 공개된 포스팅만 보여짐
# )

# 로그인한 사용자는 전부 다 볼 수있고 로그인 안하면 볼 수없도록 만들고 싶을 때는
# 상속을 통해 클래스를 재정의 해야한다.
class PostDetailView(DetailView):
    model = Post
    # queryset = Post.objects.filter(is_public=True)
    
    def get_queryset(self):
        # 재정의할땐 보통 super로 호출함
        qs = super().get_queryset() # 부모의 function을 호출하여 부모가 만들어진 쿼리셋을 가져오고
        if not self.request.user.is_authenticated: # get_queryset은 원래 인자를 받지 않으나 self.request에서 받을 수 있음 -> 여기서는 로그인한 유저의 인스턴스를 가져옴 -> 이 문장은 '로그인이 안되어 있으면 공개된 것만 볼 수 있다'라는 뜻
            qs = qs.filter(is_public=True)
        return qs
post_detail = PostDetailView.as_view(model=Post)
post_list = ListView.as_view(model=Post, paginate_by=10)