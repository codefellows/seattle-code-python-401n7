from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer


class CustomUserCreate(APIView):
    # Anyone can register!
    authentication_classes = ()
    permission_classes = ()

    # this is the method that gets invoked when a user makes a POST
    # request to api/register
    def post(self, request):
        # use the serializer!
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # if this works, `user` will be truthy
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
