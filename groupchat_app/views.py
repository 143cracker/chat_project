# groupchat_app/views.py

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from .models import User, Group, GroupMessage
from .serializers import UserSerializer, GroupSerializer, GroupMessageSerializer

# User views
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Group views
class GroupCreateView(generics.CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupDeleteView(generics.DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupListView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# Group message views
class GroupMessageCreateView(generics.CreateAPIView):
    queryset = GroupMessage.objects.all()
    serializer_class = GroupMessageSerializer

class GroupMessageListView(generics.ListAPIView):
    queryset = GroupMessage.objects.all()
    serializer_class = GroupMessageSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_unlike_message(request, message_id):
    try:
        message = GroupMessage.objects.get(pk=message_id)
    except GroupMessage.DoesNotExist:
        return Response(status=404)

    user = request.user
    if user in message.likes.all():
        message.likes.remove(user)
    else:
        message.likes.add(user)
    
    return Response({'status': 'success'})
