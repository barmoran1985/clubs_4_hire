from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/login/')
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})


def post_details(request, id):
    """
    # Create a view that return a single Post object based on the post ID
    # and and render it to the 'postdetail.html' template.
    # Or return a 404 error if the post is not found

    :param request:
    :param id:
    :return:
    """
    post = get_object_or_404(Post, pk=id)
    post.views += 1  # clock up the number of views
    post.save()
    return render(request, "postdetail.html", {'post': post})


# def top_posts(request):
#     """
#     # Get a list of posts and order them
#     # by the number of views. Only return
#     # the top 5 results. Render it to blogposts.html
#
#     :param request:
#     :return:
#     """
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-views')[:2]
#     return render(request, "blogposts.html", {'posts': posts})

def new_post(request):
    if request.method == "POST":
            form = BlogPostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect(post_details, post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'blogpostform.html', {'form': form})


def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_details, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpostform.html', {'form': form})

