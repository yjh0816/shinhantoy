from rest_framework.response import Response
from rest_framework import (
    generics, 
    mixins, 
    status,
)
from .models import Member
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
