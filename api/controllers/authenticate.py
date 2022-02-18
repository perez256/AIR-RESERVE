from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

# --- customize session data
from api.serializers import UserSerializer, UserSerializerWithToken


# Login
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['_id'] = self.user.id
        data['username'] = self.user.username
        data['email'] = self.user.email
        # data['token'] = str(self.data.access)

        # serializer = UserSerializerWithToken(self.user).data
        #
        # for k, v in serializer.items():
        #     data['token'] = str(v.token)
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# User Profile
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(incoming):
    user = incoming.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


# Register User
@api_view(['POST'])
def register_user(incoming):
    data = incoming.data
    user = User.objects.create(
        first_name=data['name'],
        username=data['email'],
        email=data['email'],
        password=make_password(data['password'])
    )
    serializer = UserSerializerWithToken(User, many=False)
    return Response(serializer.data)
