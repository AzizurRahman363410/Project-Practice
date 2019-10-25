from django.shortcuts import render
from . models import Post
from .serializers import PostSerializer
from rest_framework import generics
from django.db.models import Q


# Create your views here.
class PostListAPIView(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    # def get_queryset(self):
    #     return Post.objects.all()

        # or
    # queryset = Post.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = Post.objects.all()

        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(description__icontains=query)
                )
        return qs








class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()