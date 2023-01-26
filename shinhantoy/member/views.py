from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password, make_password
from rest_framework.permissions import IsAuthenticated
from rest_framework import (
    generics, 
    mixins, 
    status,
)
from .serializers import (
    MemberSerializer,
)

class MemberRegisterView(
    mixins.CreateModelMixin, 
    generics.GenericAPIView,
):
    serializer_class = MemberSerializer
        
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class MemberChangePasswordView(
    APIView,
):
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        p_password = request.data.get('p_password')
        password = request.data.get('password')
        password2 = request.data.get('password2')

        if password != password2:
            return Response({
                'detail': 'Different password.'
            }, status=status.HTTP_400_BAD_REQUEST)

        member = request.user

        if not check_password(p_password, member.password):
            return Response({
                'detail': 'Wrong password.'
            }, status=status.HTTP_400_BAD_REQUEST)

        member.password = make_password(password)
        member.save()

        return Response(status=status.HTTP_200_OK)