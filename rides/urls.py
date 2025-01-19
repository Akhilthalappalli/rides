from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RideViewSet, RegisterAPIView

router = DefaultRouter()
router.register(r'rides', RideViewSet, basename='ride')

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('', include(router.urls)),
]
