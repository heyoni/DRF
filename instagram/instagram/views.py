from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import PostForm
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

    return render(request, "instagram/index.html", {
        'post_list' : post_list,
        'suggested_user_list' : suggested_user_list
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
    return render(request, 'instagram/post_detail.html',{
        'post':post,
    })

def user_page(request, username):
    page_user = get_object_or_404(get_user_model(), username=username, is_active=True)
    post_list = Post.objects.filter(author=page_user)
    post_list_count = post_list.count() # DB에 count 쿼리를 던져서 받아옴, len 보다 빠름

    return render(request, 'instagram/user_page.html',{
        'page_user' : page_user,
        'post_list': post_list,
        'post_list_count': post_list_count,
    })
