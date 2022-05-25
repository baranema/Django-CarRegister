from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.MainPage.as_view(), name='home'), 
    path('update/<int:pk>/', views.update, name='update'),
    path('add/', views.carview, name='add'),
    path('remove/<int:pk>/', views.remove, name='remove'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
