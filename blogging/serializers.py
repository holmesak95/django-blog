from django.contrib.auth.models import User
from blogging.models import Post, Category
from rest_framework import serializers

# These serializers will convert the User model, Post model, and Category model into JSON to be used by the API to return the data to the user
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['url', 'title', 'text', 'author', 'created_date', 'modified_date', 'published_date']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'name', 'description', 'posts']
