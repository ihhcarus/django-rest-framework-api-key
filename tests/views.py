from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_api_key.permissions import HasAPIAccess


class TestViewHeader(APIView):
    """
    A dummy view used only for testing HTTP header authentication.
    """

    def get(self, request):
        return Response({"msg": "Hello World!"}, status=status.HTTP_200_OK)


class HasAPIAccessQueryParam(HasAPIAccess):
    """
    Permission class that enables receiving the api key though the query parameter.
    """
    allow_query_param = True


class TestViewQueryParam(APIView):
    """
    A dummy view used only for testing query parameter authentication.
    """

    permission_classes = (HasAPIAccessQueryParam,)

    def get(self, request):
        return Response({"msg": "Hello World!"}, status=status.HTTP_200_OK)
