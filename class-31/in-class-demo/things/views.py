from rest_framework import generics
from .serializers import ThingSerializer
from .models import Thing


class ThingList(generics.ListAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


class ThingDetail(generics.RetrieveAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer

