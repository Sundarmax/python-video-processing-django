from django.contrib import admin
from django.urls import path
from rest_framework import routers
from file_test import views
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'fileupload',views.FileUploadViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/v1/', include(router.urls))
]
