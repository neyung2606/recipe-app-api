from rest_framework import viewsets, status
from rest_framework.response import Response
from posts.models import Posts
from posts.serializers import PostSerializer


class PostsViewSet(viewsets.ViewSet):
    def list(self, request):
        post_qs = Posts.objects.all()
        serializer_data = PostSerializer(post_qs, many=True)
        return Response(data=serializer_data.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data.copy()
        serializer_data = PostSerializer(data=data)
        if serializer_data.is_valid():
            posts = serializer_data.create()
            return Response(data=posts, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
