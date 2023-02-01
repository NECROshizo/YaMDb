from django.contrib.auth.tokens import default_token_generator
from django.core import mail
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

from api_yamdb.settings import GENERAL_EMAIL
from users.models import User
from users.serializers import (GetTokenSerializer, SignupSerializer,
                               UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = (
        permissions.IsAuthenticated,
        permissions.IsAdminUser,
    )


@api_view(['POST'])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    user = get_object_or_404(
        User,
        username=serializer.validated_data['username']
    )
    confirmation_code = default_token_generator.make_token(user)
    mail.send_mail(
        subject='Code for registration in YaMDB',
        message=f'Ваш код подтверждения: {confirmation_code}',
        from_email=GENERAL_EMAIL,
        recipient_list=[user.email],
    )
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_token(request):
    serializer = GetTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(
        User,
        username=serializer.validated_data['username']
    )
    if default_token_generator.check_token(
        user, serializer.validated_data['confirmation_code']
    ):
        jwt_token = RefreshToken.for_user(user)
        return Response(
            {
                'jwt_token': str(jwt_token),
                'access': str((jwt_token.access_token))
            },
            status=status.HTTP_200_OK
        )
    else:
        raise ValidationError('Invalid token')
