from django.views import generic
from .models import Comment, Post

from .forms import CommentForm
from django.shortcuts import render, get_object_or_404


class PostList(generic.ListView):
    #classbases view which displaces all the post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 2

# class PostDetail(generic.DetailView):
#     #classbases view which displaces the detail for each Post
#     model = Post
#     template_name = 'post_detail.html'


def post_detail(request, slug):
    #functionBased view to displace comment related to details
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, context={'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
