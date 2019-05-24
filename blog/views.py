from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    #def perform_create(self, serializer):
        #if self.request.user.is_authenticated():
            #serializer.save(user=sel.request.user)


class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

