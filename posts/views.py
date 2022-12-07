from rest_framework.decorators import permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from core.pagination import Pagination
# Create your views here.


class PostListApiView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = Pagination
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request, *args, **kwargs):
        data = request.data
        data['author'] = request.user.id
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PostRetrieveUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != request.user:
            return Response({'message': 'You are not the author of this post.'}, status=403)
        return super().delete(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != request.user:
            return Response({'message': 'You are not the author of this post.'}, status=403)
        return super().patch(request, *args, **kwargs)
