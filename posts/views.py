from rest_framework.decorators import permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from .models import Post
from .serializers import PostSerializer, PostCreateSerializer
from rest_framework.request import Request
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
        serializer = PostCreateSerializer(data=data)
        if serializer.is_valid():
            post = serializer.save()
            return Response(PostSerializer(post).data, status=201)
        return Response(serializer.errors, status=400)


class PostRetrieveUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PostSerializer(instance, context={'user': request.user})
        return Response(serializer.data, status=200)

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


class PostVoteView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

    def patch(self, request: Request, *args, **kwargs):
        instance = self.get_object()
        data = request.query_params
        if not data.get('type'):
            return Response({'message': 'You must provide a type.'}, status=400)
        if data.get('type') == 'up':
            if instance.upvotes.filter(id=request.user.id).exists():
                instance.upvotes.remove(request.user)
                instance.points -= 1
            elif instance.downvotes.filter(id=request.user.id).exists():
                instance.downvotes.remove(request.user)
                instance.upvotes.add(request.user)
                instance.points += 2
            else:
                instance.upvotes.add(request.user)
                instance.points += 1
        elif data.get('type') == 'down':
            if instance.downvotes.filter(id=request.user.id).exists():
                instance.downvotes.remove(request.user)
                instance.points += 1
            elif instance.upvotes.filter(id=request.user.id).exists():
                instance.upvotes.remove(request.user)
                instance.downvotes.add(request.user)
                instance.points -= 2
            else:
                instance.downvotes.add(request.user)
                instance.points -= 1
        instance.save()
        return Response(PostSerializer(instance, context={"user": request.user}).data, status=200)
