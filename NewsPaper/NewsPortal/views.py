from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Post

class PostsList(ListView):

    model = Post
    ordering = '-post_time'
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_time'] = Post.post_time
        return context


class PostDetail(DetailView):

    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_time'] = Post.post_time
        return context
