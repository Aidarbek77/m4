
from django.contrib import admin
from django.urls import path, include
from posts.views import test_review , html_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('test/', test_review),
    path('html/', html_view)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)