import json
import requests

from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from django.conf import settings
from django.http import HttpResponseRedirect

from .serializers import UserSerializer, CompanySerializer
from models import User


class UserProfileView(APIView):
    def get(self, request, format=None):
        """
        Return a current_user profile
        """
        return Response(UserSerializer(request.user).data)


class MainUserView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        user_id = int(request.GET.get('id')[0])
        user = User.objects.get(id=user_id)
        return Response(UserSerializer(user).data)


class CreateUserView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        """
        Registration endpoint
        """
        json_data = json.loads(request.body)
        if json_data['is_company']:
            serializer = UserSerializer(data=json_data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.create_or_update(json_data)
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                return Response({"token": token})
        else:
            serializer = CompanySerializer(data=json_data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.create_or_update(json_data)
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                return Response({"token": token})

