from django.urls import path, re_path
from .api import CarCreateApi, CarApi, CarUpdateApi, CarDeleteApi, CarList, CarEdit, CarCreate
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path('api', CarApi.as_view()),
    path('api/create', CarCreateApi.as_view()),
    path('api/<int:pk>', CarUpdateApi.as_view()),
    path('api/<int:pk>/delete', CarDeleteApi.as_view()),
    path('all', CarList.as_view(), name='all_entries'),
    re_path('^all/get/(?P<pk>.*)$', CarEdit.as_view(), name='edit_car'),
    path('create', CarCreate().as_view(), name='create_car'), 
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)