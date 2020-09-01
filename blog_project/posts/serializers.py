from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.Serializer):
    class Meta:
        fields = ('id', 'title', 'created_at', 'updated_at',)
        model = Post
