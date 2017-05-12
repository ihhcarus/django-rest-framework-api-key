from rest_framework import permissions

from rest_framework_api_key.models import APIKey


class HasAPIAccess(permissions.BasePermission):
    message = 'Invalid or missing API Key.'

    DEFAULT_HEADER_NAME = 'HTTP_API_KEY'
    DEFAULT_QUERY_PARAM = 'api_key'

    header_name = DEFAULT_HEADER_NAME

    allow_query_param = False
    query_param = DEFAULT_QUERY_PARAM

    def has_permission(self, request, view):
        u""" Try to retrieve the api key from the HTTP header or the URL's query parameter if enabled. """
        api_key = request.META.get(self.header_name, '')
        if not api_key and self.allow_query_param:
            api_key = request.query_params.get(self.query_param, '')
        return self.check_api_key(api_key)

    def check_api_key(self, api_key):
        u""" Lookup the api key in the database. """
        return APIKey.objects.filter(key=api_key).exists()
