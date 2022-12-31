from django.urls import path
from .views import PostListApiView, PostRetrieveUpdateDeleteApiView, PostVoteView, ReplyListApiView, ReplyRetrieveUpdateDeleteApiView, ReplyVoteView

urlpatterns = [
    path('posts/', PostListApiView.as_view()),
    path('posts/<int:pk>/', PostRetrieveUpdateDeleteApiView.as_view()),
    path('posts/<int:pk>/vote', PostVoteView.as_view()),
    path('posts/<int:post_pk>/reply/', ReplyListApiView.as_view()),
    path('posts/<int:post_pk>/reply/<int:pk>',
         ReplyRetrieveUpdateDeleteApiView.as_view()),
    path('posts/<int:pk>/reply/<int:pk>/vote', ReplyVoteView.as_view()),

]
