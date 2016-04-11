# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login
from rest_framework import viewsets, status, views
from rest_framework.response import Response
from meta_id.authentication.models import User
from meta_id.authentication.serializers import (
    UserSerializer, LoginSerializer, ChangePasswordSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ChangePasswordView(views.APIView):
    def post(self, request, user_pk, format=None):
        user = User.objects.get(pk=user_pk)
        serializer = ChangePasswordSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class LoginView(views.APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():

            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            user = authenticate(email=email, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)

                    serialized = UserSerializer(user,
                                                context={'request': request})

                    return Response(serialized.data)
                else:
                    return Response({
                        'message': 'Essa conta não está autorizada.'
                    }, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({
                    'message': 'Usuário ou senha estão inválidos.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
