
from rest_framework import routers
from bank import views
from django.contrib import admin
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'branch', views.Branch_Viewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
