from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import OrderSerializer
from rest_framework.views import APIView
import uuid
from .models import Order,Payment

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MockPaymentAPIView(APIView):
    def post(self, request, *args, **kwargs):
        order_id=request.data.get('order')
        amount = request.data.get('amount')
        payment = Payment.Objects.create(
            order_id=order_id,
            amount=amount,
            status='success',
            transaction_id=str(uuid.uuid4())
        )
        return Response({
            'message':'payment Done successfully!',
            'transaction_id': payment.transaction_id,
            'status': payment.status            
        })