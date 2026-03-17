from django.shortcuts import render,get_object_or_404
from blog.models import Post
# Create your views here.
def post_list_view(request):
    posts=Post.published.all()
    return render(request,"blog/post_list.html",{"posts":posts})
def post_detail(request, id):
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED
    )
    return render(
        request,
        'blog/detail.html',
        {'post': post}
    )