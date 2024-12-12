from rest_framework import viewsets, generics
from .models import Event, Registration
from .serializers import EventSerializer, UserSerializer, RegistrationSerializer
from django.contrib.auth.models import User
from django_filters import rest_framework as filters
from .models import Registration


class EventFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    location = filters.CharFilter(lookup_expr='icontains')
    date = filters.DateTimeFilter(lookup_expr='exact')

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filterset_class = EventFilter

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegistrationView(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer




