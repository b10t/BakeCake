from cakes_store import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/', views.reg, name='reg'),
    path('', views.index, name='index'),
    path('lk', views.lk, name='lk'),
    path('login', views.login, name='login'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
