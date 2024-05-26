from .serializers.common import ShakeSerializer
from .serializers.populated import PopulatedRecordSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from lib.permissions import IsOwnerOrReadOnly
from .models import Shake
from lib.views import ObjectOwnerView
from rest_framework.response import Response

class ShakeIndexView(ObjectOwnerView, ListCreateAPIView):
    queryset = Shake.objects.all()
    serializer_class = ShakeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ShakeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Shake.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PopulatedRecordSerializer
        else:
            return ShakeSerializer

class ShakeFavouriteView(UpdateAPIView):
    queryset = Shake.objects.all()
    serializer_class = ShakeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def patch(self, request, pk):
        shake = self.get_object()
        if request.user in shake.favourites.all():
            print('User in favourites list')
            shake.favourites.remove(request.user)
            shake.save()
            return Response(status=204)

        else:
            print('User NOT in favourites list')
            shake.favourites.add(request.user)
            shake.save()
            return Response(status=201)

# class UserFavouriteShakeView(ListCreateAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def get(self,request):
#         user = request.user
#         favourite_shakes = user.favourite_shakes.all()
#         serializer = ShakeSerializer(favourite_shakes, many=True)
#         return Response(serializer.data)
