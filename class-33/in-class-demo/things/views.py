from rest_framework import generics
from .serializers import ThingSerializer
from .models import Thing
from .permissions import IsOwnerOrReadOnly


class ThingList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


class ThingDetail(generics.RetrieveUpdateDestroyAPIView):
    # check for authentication here!
    permission_classes = (IsOwnerOrReadOnly,)  # new
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
