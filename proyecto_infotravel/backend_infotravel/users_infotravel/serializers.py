from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):

    self = "null"
    def validate_password(self, value):
        return make_password(value)

    email = serializers.EmailField(
        required=True)
    username = serializers.CharField(
        required=True)
    password = serializers.CharField(
        min_length=8)
    #password = validate_password(self, str(password))


    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password')



