# -*- coding: utf-8 -*-

from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, user):
        if request.user:
            return user == request.user
        return False


class IsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, user):
        return request.user.is_admin
