# -*- coding: utf-8 -*-

from rest_framework import renderers


class UnicodeJSONRenderer(renderers.JSONRenderer):
    charset = 'utf-8'
