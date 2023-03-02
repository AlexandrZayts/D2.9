
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin', admin.site.urls),
    path('pages', include('django.contrib.flatpages.urls')),
    path("account", include("allauth.urls")),
    path("accounts", include("accounts.urls")),
    path('news', include('NewsPortal.urls'))

]
