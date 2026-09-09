from django.shortcuts import render, redirect, get_object_or_404

from .models import Post
from .forms import PostForm


def feed(request):

    posts = Post.objects.all().order_by("-id")

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("feed")

    else:
        form = PostForm()

    context = {
        "posts": posts,
        "form": form,
    }

    return render(request, "posts/feed.html", context)


def like_post(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    post.likes += 1
    post.save()

    return redirect("feed")