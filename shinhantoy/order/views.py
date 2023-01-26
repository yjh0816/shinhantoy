from rest_framework import (
    generics, 
    mixins, 
    status,
)
from .models import Order, Comment
from rest_framework.response import Response
from .serializers import (
    OrderSerializer,
    CommentSerializer,
    CommentCreateSerializer,
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

class CommentListView(
    mixins.ListModelMixin, 
    generics.GenericAPIView,
):
    serializer_class = CommentSerializer

    def get_queryset(self):
        order_id = self.kwargs.get('order_id')
        if order_id:
            return Comment.objects.filter(order_id=order_id) \
                .select_related('member', 'order') \
                .order_by('-id')
        return Comment.objects.none()

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

class CommentCreateView(
    mixins.CreateModelMixin, 
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    serializer_class = CommentCreateSerializer

    def get_queryset(self):
        if self.request.method == 'DELETE':
            order_id = self.kwargs.get('order_id')
            comment_id = self.kwargs.get('pk')
            print(order_id, comment_id)
            if order_id:
                return Comment.objects.filter(order_id=order_id) \
                    .filter(id=comment_id) \
                    .select_related('member', 'order') \
                    .order_by('-id')
            return Comment.objects.none()
        return Comment.objects.all().order_by('id')

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)
