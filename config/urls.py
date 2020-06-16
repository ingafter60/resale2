# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import resale.views

urlpatterns = [
    path('', resale.views.home, name='home'),
    # path('category/', resales.views.category, name='hocategory'),
    path('category/', include('resale.urls')),
    path('admin/', admin.site.urls),
] 
# Serving static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Serving files uploaded by a user during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


