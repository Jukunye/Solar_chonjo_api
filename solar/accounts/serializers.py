from rest_framework import serializers
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer

User = get_user_model()

class UserCreateSerializer(BaseUserCreateSerializer):
    role = serializers.ChoiceField(choices=User.USER_ROLES, required=False)
    
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'password', 'role', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True}
        }

class UserSerializer(BaseUserSerializer):
    role = serializers.CharField(source='get_role_display')
    
    class Meta(BaseUserSerializer.Meta):
        model = User
        fields = ('id', 'email', 'role', 'first_name', 'last_name', 'is_active')
        read_only_fields = ('email', 'is_active')