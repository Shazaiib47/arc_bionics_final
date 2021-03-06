from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from profiles.models import UserProfile


def all_posts(request):
    post_list = Post.objects.filter(status=1).order_by('-created_on')
    paginator = Paginator(post_list, 4)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    context = {
        'blog_page': 'active',
        'page': page,
        'post_list': post_list,
    }

    return render(request, 'blog/blog.html', context)


def post_detail(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                comment_form = CommentForm(initial={
                    'email': profile.user.email,
                    })
            except UserProfile.DoesNotExist:
                comment_form = CommentForm()
        else:
            comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
