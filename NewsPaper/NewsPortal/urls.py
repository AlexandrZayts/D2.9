from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page


urlpatterns = [
   path('', cache_page(60*1)(PostsList.as_view()), name='posts'),
   path('<int:pk>', cache_page(60*5)(PostDetail.as_view()), name='post'),
   path('search', PostsList.as_view(), name='search.html'),
   path('news/create/', create_news.as_view(), name='news_create'),
   path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
   path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
   path('articles/create/', create_articles.as_view(), name='articles_create'),
   path('articles/<int:pk>/edit/', ArticlesUpdate.as_view(), name='articles_update'),
   path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='articles_delete'),
   path('categories/<int:pk>', CategoryListView.as_view, name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]