# I M P O R T S   &   D E P E N D E N C I E S-----------------------
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


# V I E W S --------------------------------------------------------
