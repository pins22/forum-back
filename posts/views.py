from rest_framework.decorators import permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
# Create your views here.


class PostListApiView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    authentication_classes = (SessionAuthentication,)

    # @permission_classes([AllowAny])
    def get(self, request, *args, **kwargs):
        # is user loged in?
        if request.user.is_authenticated:
            print("User is authenticated")
        else:
            print("User is not authenticated")
        return Response(self.serializer_class(self.get_queryset(), many=True).data)
