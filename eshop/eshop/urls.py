from django.contrib import admin
from django.urls import path, include
from django.conf import settings # showing images
from django.conf.urls.static import static  # showing images

urlpatterns = [
    path('', include('core.urls')),
    path('items/', include('item.urls')),
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('inbox/', include('conversation.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # showing images
