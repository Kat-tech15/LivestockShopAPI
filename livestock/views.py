from rest_framework import generics, permissions, mixins
from accounts.permissions import IsOwnerOrReadOnly
from .serializers import LivestockSerializer
from .models import Livestock

class LivestockList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Livestock.objects.all()
    serializer_class = LivestockSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class LivestockDetail(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin, 
                      mixins.DestroyModelMixin, 
                      generics.GenericAPIView
                    ):

    queryset = Livestock.objects.all()
    serializer_class = LivestockSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)