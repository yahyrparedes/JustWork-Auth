from rest_framework import serializers
from django.contrib.auth.models import User

from empresas.models import Empresa
from .models import MyUser


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'email', 'write_only', 'password')
        extra_kwargs = {'password': {'write_only': True}, 'is_company': {'write_only': True}}

    def create(self, validated_data):
        user = MyUser.objects.create_user(validated_data['email'],
                                          validated_data['password'],
                                          validated_data['is_company'])

        return user


class RegisterUserSerializer(serializers.ModelSerializer):
    id = serializers.ModelSerializer(read_only=True)
    is_company = serializers.BooleanField(write_only=True)

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'is_company')

    def create(self, validated_data):
        pass
        #insertdat
        #

class RegisterCompanySerializer(serializers.ModelSerializer):
    user = RegisterUserSerializer

    class Meta:
        model = Empresa
        fields = ('user', 'razon_social', 'ruc')

    def create(self, validated_data):

        # company = User.objects.create(validated_data['user'])
        pass
        ## isert data

