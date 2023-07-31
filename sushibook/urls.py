from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include

#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('users.urls')),
    path('', include('book.urls')),
    path('', include('job.urls')),
]
# Use static() to add url mapping to serve static files during 
# development (only) ***

from django.conf import settings
from django.conf.urls.static import static
from .settings import DEBUG
if DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'main.views.Oops'


#add robots.txt
from django.views.static import serve
from django.urls import re_path

urlpatterns += [
    re_path(r'^robots\.txt$', serve, {'document_root': settings.BASE_DIR, 'path': "/robots.txt"}),
]


