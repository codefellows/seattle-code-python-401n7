from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import CookieStand
from .permissions import IsOwnerOrReadOnly
from .serializers import CookieStandSerializer


class CookieStandList(ListCreateAPIView):
    # queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer

    def get_queryset(self):
        user = self.request.user
        return CookieStand.objects.filter(owner=user)


class CookieStandDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer
