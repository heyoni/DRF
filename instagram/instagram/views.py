from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from django.contrib import messages
from .models import Tag, Post
from django.contrib.auth import get_user_model
from django.db.models import Q



def index(request):
    post_list = Post.objects.all()\
        .filter(
            # 작성자가 나이거나 팔로잉하고 있는 목록 -> Q사용해서 or문 작성
            Q(author__in= request.user.following_set.all()) | Q(author=request.user)
        )

    suggested_user_list =get_user_model().objects.all()\
        .exclude(pk=request.user.pk)\
        .exclude(pk__in=request.user.following_set.all())
    request.user.following_set.all()

    comment_form = CommentForm()
    
    return render(request, "instagram/index.html", {
        'post_list' : post_list,
        'suggested_user_list' : suggested_user_list,
        'commnet_form': comment_form,
    })


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            
            post.tag_set.add(*post.extract_tag_list())

            messages.success(request, "포스팅을 저장했습니다.")
            # models에서 get_absolute_url 구현이 있어야 함
            return redirect(post)
    else:
        form = PostForm()

    return render(request, "instagram/post_form.html",{
        'form': form,
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm()
    return render(request, 'instagram/post_detail.html',{
        'post':post,
        'comment_form': comment_form
    })

def user_page(request, username):
    page_user = get_object_or_404(get_user_model(), username=username, is_active=True)
    post_list = Post.objects.filter(author=page_user)
    post_list_count = post_list.count() # DB에 count 쿼리를 던져서 받아옴, len 보다 빠름

    # 로그인이 되어있을 경우 page_user와 현재 로그인 되어있는 유저를 비교한 뒤, 팔로우 되어있으면 True, 아니면 False
    if request.user.is_authenticated:
        is_follow = request.user.following_set.filter(pk=page_user.pk).exists()
    else:
        is_follow = False

    return render(request, 'instagram/user_page.html',{
        'page_user' : page_user,
        'post_list': post_list,
        'post_list_count': post_list_count,
        'is_follow': is_follow,
    })



@login_required
def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.like_user_set.add(request.user)

    messages.success(request, f"{post.pk}를 좋아합니다.")
    redirect_url = request.META.get("HTTP_REFERER","root")
    return redirect(redirect_url)


@login_required
def post_unlike(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.like_user_set.remove(request.user)

    messages.success(request, f"{post.pk}를 좋아요를 취소합니다.")
    redirect_url = request.META.get("HTTP_REFERER","root")
    return redirect(redirect_url)


@login_required
def comment_new(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect(comment.post)
    else:
        form = CommentForm()

    return render(request, "instagram/comment_form.html",{
        "form":form,

    })