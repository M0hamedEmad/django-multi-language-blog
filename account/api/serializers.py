from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class CreateUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, write_only=True,  style={'input_type': 'password'})
    email = serializers.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            "password":{
                "write_only":True,
                'style':{'input_type': 'password'}
                }
        }

    def validate_email(self, value):
        user = User.objects.filter(email=value)
        if user.exists():
            raise ValidationError("This email is alredy exists")
        
        return value

    def validate_password(self, value):
        password2 = self.get_initial().get('password2')
        
        password_validation.validate_password(value, self.instance)

        if password2 != value:
            raise ValidationError("passwords didn't match")

        return value

    def validate_password2(self, value):
        password = self.get_initial().get('password')
        if password != value:
            raise ValidationError("passwords didn't match")

        return value

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')

        print("*"*60)

        user = User(email=email, username=username)
        user.set_password(password)
        user.save()

        return user