from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from reviews.models import Review, Comment, Title


class ReviewSerializer(serializers.ModelSerializer):

    auther = SlugRelatedField(slug_field='username', read_only=True,)
    title = SlugRelatedField(slug_field='name', read_only=True,)

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        model = Review

    def validate_title(self, value):
        """Проверка, что отзыв единственный на произведение"""
        title = get_object_or_404(Title, pk=value.id)
        author = self.context['request'].user
        review = Review.objects.filter(
            author=author, title=title).exists()
        if review:
            raise serializers.ValidationError('Отзыв уже написан')
        return value


class CommentSerializer(serializers.ModelSerializer):

    auther = SlugRelatedField(slug_field='username', read_only=True,)

    class Meta:
        fields = '__all__'
        model = Comment
