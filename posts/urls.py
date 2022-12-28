from django.urls import path
from .views import PostListApiView, PostRetrieveUpdateDeleteApiView, PostVoteView

urlpatterns = [
    path('posts/', PostListApiView.as_view()),
    path('posts/<int:pk>/', PostRetrieveUpdateDeleteApiView.as_view()),
    path('posts/<int:pk>/vote', PostVoteView.as_view())
]
