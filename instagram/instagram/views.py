from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.contrib import messages
from .models import Tag

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
            return redirect("/")
    else:
        form = PostForm()

    return render(request, "instagram/post_form.html",{
        'form': form,
    })