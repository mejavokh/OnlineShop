from django.contrib import admin
from django.urls import path, include

from .settings import STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT, DEBUG
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls', namespace='main')),
    path('basket/', include('basket.urls', namespace='basket')),
    path('search/', include('search.urls', namespace='search')),
    path('favorites/', include('favorites.urls', namespace='favorites'))
]


if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
