from django.urls import path
from .views import PostsList, PostDetail


urlpatterns = [
   path('', PostsList.as_view()),
   path('<int:pk>', PostDetail.as_view()),
   path('search/', PostsList.as_view(), template_name='search.html'),
]