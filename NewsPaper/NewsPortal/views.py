from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, get_object_or_404, render

from .models import *
from .filters import PostFilter
from .forms import PostForm


class New_Post_on_Category(models.Model):

    name = models.CharField(max_length=127, unique=True)
    subscribers = models.ManyToManyField(User, related_name='PostCategory')


class PostsList(ListView):

    model = Post
    ordering = 'name'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = Post.filterset
        return context


class PostDetail(DetailView):

    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = Post.filterset
        return context


class create_news(PermissionRequiredMixin, CreateView):
    permission_required = ('NewsPortal.news_create',)
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        Post = form.save(commit=False)
        Post.position = 'ns'
        return super().form_valid(form)


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('NewsPortal.news_update',)
    form_class = PostForm
    model = Post
    template_name = 'news_update.html'


class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('NewsPortal.news_delete',)
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('')


class create_articles(PermissionRequiredMixin, CreateView):
    permission_required = ('NewsPortal.articles_create',)
    form_class = PostForm
    model = Post
    template_name = 'articles_create.html'

    def form_valid(self, form):
        Post = form.save(commit=False)
        Post.position = 'ar'
        return super().form_valid(form)


class ArticlesUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('NewsPortal.articles_update',)
    form_class = PostForm
    model = Post
    template_name = 'articles_update.html'


class ArticlesDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('NewsPortal.articles_delete',)
    model = Post
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('')


class CategoryListView(ListView):
    model = Post
    template_name = 'news/category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.object.filter(category=self.category).order_by('-date')
        return  queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context

@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = 'Вы успешно подписались на рассылку новостей категории'
    return render (request, 'news/subscribe.html', {'category': category,'message': message})