from rest_framework.fields import SerializerMethodField
from post.models import Comment, Post
from rest_framework import serializers
from post.models import Post, Comment
from account.api.serializers import UserDetailSerializer

class PostSerializer(serializers.ModelSerializer):
    post_categories = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(view_name='post_api:post', lookup_field='slug')

    class Meta:
        model = Post
        fields = [
            'url',
            'author', 
            'title', 
            'content', 
            'post_categories',
            'categories',
            'image', 
            'published_at', 
            'views_count', 
            'active', 
            'slug'
            ]
        read_only_fields = ('slug', 'post_categories', 'author')
        extra_kwargs = {
            'categories':{'write_only': True},
            'active':{'write_only': True}
        }

    def get_post_categories(self, obj):
        categories = obj.categories.all()
        return [categpry.name for categpry in categories]

    def get_author(self, obj):
        return obj.author.username

class PostDetailSerializer(serializers.ModelSerializer):
    post_categories = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'author', 
            'title', 
            'content', 
            'post_categories',
            'categories',
            'image', 
            'published_at', 
            'views_count', 
            'active', 
            'slug',
            'comments',
            ]
        read_only_fields = ('slug', 'post_categories', 'author')
        extra_kwargs = {
            'categories':{'write_only': True},
            'active':{'write_only': True}
        }

    def get_post_categories(self, obj):
        categories = obj.categories.all()
        return [categpry.name for categpry in categories]

    def get_author(self, obj):
        return obj.author.username        
        
    def get_comments(self, obj):
        serializer = CommentSerailzer(obj.comments.filter(active=True), many=True)
        return serializer.data


class PostCommentSerailzer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'created_at']
        read_only_fields = ('user',)


class CommentSerailzer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'post', 'created_at']
        read_only_fields = ('user',)
