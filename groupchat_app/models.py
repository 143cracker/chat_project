
from django.db import models
from django.contrib.auth.models import AbstractUser,Permission,Group
from django.utils.translation import ugettext_lazy as _
class User(AbstractUser):
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_set',
        help_text=_('Specific permissions for this user.'),
        related_query_name='custom_user'
    )
    groups = models.ManyToManyField(
        Group,
        related_name='group_users',
        blank=True,
        verbose_name=_('groups'),
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_query_name='group_user',
    )

class Group(models.Model):
    name = models.CharField(max_length=100)
    # Use custom related_name for members
    members = models.ManyToManyField(User, related_name='user_groups')

class GroupMessage(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_messages_by', blank=True)

