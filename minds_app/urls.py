from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.index,name='index'),
    path('Agency/',views.Agency,name='Agency'),
    path('Blog/', views.Blog,name='Blog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





