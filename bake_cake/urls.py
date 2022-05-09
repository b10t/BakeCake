from cakes_store import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('lk/', views.lk, name='lk'),
    path('signup/', views.signup, name='signup'),
    path('users/', include('django.contrib.auth.urls')),
    path('processing_orders/', views.processing_orders, name='processing_orders'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
