from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import status
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
    return Response(serializer.data, status=status.HTTP_200_OK)


# Register User
@api_view(['POST'])
def register_user(incoming):
    try:
        data = incoming.data
        user = User.objects.create(
            username=data['username'],
            password=make_password(data['password']),
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as p:
        print(str(p))
        return Response({'message': 'Registration Failed, Try Again'}, status=status.HTTP_400_BAD_REQUEST)
