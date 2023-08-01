# groupchat_app/urls.py

from django.urls import path
from .views import UserCreateView, UserUpdateView, GroupCreateView, GroupDeleteView, GroupListView, GroupMessageCreateView, GroupMessageListView, like_unlike_message

urlpatterns = [
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('groups/create/', GroupCreateView.as_view(), name='group-create'),
    path('groups/<int:pk>/delete/', GroupDeleteView.as_view(), name='group-delete'),
    path('groups/', GroupListView.as_view(), name='group-list'),
    path('group-messages/create/', GroupMessageCreateView.as_view(), name='group-message-create'),
    path('group-messages/', GroupMessageListView.as_view(), name='group-message-list'),
    path('group-messages/<int:message_id>/like-unlike/', like_unlike_message, name='like-unlike-message'),
]
