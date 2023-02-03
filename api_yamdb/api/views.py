from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination

from reviews.models import (
    Title,
    Review,
    Comment,
)
from .permissions import (
    IsAdmin,
    IsModerator,
    IsAdminOrReadOnly,
    EditPermission,
)
from .serializers import (
    ReviewSerializer,
    CommentSerializer,
)


class ReviewsViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (EditPermission,)

    def get_queryset(self):
        title_id = self.kwargs.get("title_id")
        title = get_object_or_404(Title, pk=title_id)
        new_queryset = Review.objects.filter(title=title)
        return new_queryset

    def perform_create(self, serializer):
        title_id = self.kwargs.get("title_id")
        title = get_object_or_404(Title, pk=title_id)
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    pagination_class = LimitOffsetPagination
    serializer_class = CommentSerializer
    permission_classes = (EditPermission,)

    def get_queryset(self):
        review_id = self.kwargs.get("review_id")
        review = get_object_or_404(Review, pk=review_id)
        new_queryset = Comment.objects.filter(review=review)
        return new_queryset

    def perform_create(self, serializer):
        review_id = self.kwargs.get("review_id")
        review = get_object_or_404(Review, pk=review_id)
        serializer.save(author=self.request.user, review=review)
