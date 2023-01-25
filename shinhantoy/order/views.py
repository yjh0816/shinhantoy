from rest_framework import (
    generics, 
    mixins, 
    status,
)
from .models import Order
from rest_framework.response import Response
from .serializers import (
    OrderSerializer
)

class OrderListView(
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

class OrderDetailView(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)