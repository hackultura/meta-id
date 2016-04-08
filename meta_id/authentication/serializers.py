# -*- coding: utf-8 -*-

from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from meta_id.authentication.models import User
from meta_id.core.serializers import EnteSerializer


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=False)
    password2 = serializers.CharField(write_only=True, required=False)
    ente = EnteSerializer(required=False)

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'slug', 'ente',
                  'password1', 'password2', 'is_admin',)
        read_only_fields = ('created_at', 'updated_at',)

    def validate(self, data):
        is_admin = data.get('is_admin', False)
        ente = data.get('ente')
        if not ente and not is_admin:
            raise serializers.ValidationError(
                {"ente": "Os dados dos entes são obrigatórios"}
            )
        return data

    def create(self, validated_data):
        ente = validated_data.pop('ente', None)
        password1 = validated_data.pop('password1', None)
        password2 = validated_data.pop('password2', None)

        if ente:
            serializer = EnteSerializer(data=ente)
            if serializer.is_valid():
                if password1 and password2 and password1 == password2:
                    user = User.objects.create(**validated_data)
                    user.set_password(password1)
                    user.save()
                else:
                    raise serializers.ValidationError(
                        {
                            "password2":
                            "As senhas não se batem. Digite novamente"
                        }
                    )
                serializer.save(user=user)

        return user

    def update(self, instance, validated_data):
        ente = validated_data.pop('ente', None)

        instance.name = validated_data.get('name', instance.name)
        password = validated_data.pop('password1', None)
        confirm_password = validated_data.pop('password2', None)
        is_admin = validated_data.pop('is_admin', False)

        if ente and not is_admin:
            ente_serializer = EnteSerializer(instance.ente, data=ente)
            if ente_serializer.is_valid():
                ente_serializer.save()

        if password and confirm_password and password == confirm_password:
            instance.set_password(password)

        instance.save()
        update_session_auth_hash(self.context.get('request'), instance)

        return instance


class ChangePasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)
    password1 = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        fields = ('email', 'old_password', 'password1', 'password2',)

    def update(self, instance, validated_data):
        email = validated_data.pop('email', None)
        old_password = validated_data.pop('old_password', None)
        password1 = validated_data.pop('password1', None)
        password2 = validated_data.pop('password2', None)

        if email in [None, '']:
            raise serializers.ValidationError("E-mail é obrigatório.")

        if old_password in [None, '']:
            raise serializers.ValidationError("Digite sua antiga senha.")

        user_checked = instance.check_password(old_password)

        if user_checked:
            if password1 and password2 and password1 == password2:
                instance.set_password(password1)
                instance.save()
            else:
                raise serializers.ValidationError(
                    "As senhas não se batem. Digite novamente"
                )
        else:
            raise serializers.ValidationError(
                {
                    'old_password': "A senha antiga é inválida. Tente novamente"
                }
            )

        return instance


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
