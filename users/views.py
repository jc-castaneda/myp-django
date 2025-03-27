from django.db.utils import IntegrityError
from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
# Import your CustomUser model instead of the default User
from users.models import CustomUser
from django.contrib.auth import authenticate
from rest_framework import status

class MyTokenObtainPairView(TokenObtainPairView):
    pass  # Inherits default JWT behavior

@csrf_exempt
@api_view(['POST'])
def register_user(request):

    """Register a new user"""

    # Handling succesful registration requests
    try:
        data = request.data
        user = CustomUser.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            user_type=data.get('user_type', CustomUser.UserType.MUSICIAN)  # Set a default type
        )
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

    # Handling bad registration requests
    except IntegrityError as e:
        # If email already exists
        if 'UNIQUE constraint failed: users_customuser.email' in str(e):
            return Response({'error': 'User email already exists!'}, status=status.HTTP_400_BAD_REQUEST)

        # If username already exists
        elif 'UNIQUE constraint failed: users_customuser.username' in str(e):
            return Response({'errr' : "User username already exists!"}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
def logout_user(request):

    """Blacklist token on logout"""
    try:
        token = RefreshToken(request.data.get('refresh'))
        token.blacklist()
        return Response({'message': 'User logged out'}, status=status.HTTP_205_RESET_CONTENT)
    except:
        return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
