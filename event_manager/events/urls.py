from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet
from .views import EventViewSet, RegisterUserView, RegistrationView


router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')


urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('register_event/', RegistrationView.as_view(), name='register_event'),
    path('', include(router.urls)),
]