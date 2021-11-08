from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    qs = Post.object.all()
    q = request.GET.get('q','')
    if q:
        qs = qs.filter(message__icontains=q)
    
    return render(request, 'instagram/post_list.html', {
        'post_list' : qs,
        'q':q
    })