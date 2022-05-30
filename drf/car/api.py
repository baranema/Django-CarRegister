from rest_framework import generics
from rest_framework.response import Response
from .serializer import CarSerializer
from .models import Car

class CarCreateApi(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarApi(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDeleteApi(generics.DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer