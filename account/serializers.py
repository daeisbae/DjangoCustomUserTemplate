from rest_framework import serializers
from .models import Account

# Description: User Account Serializing Class
# Precondition: Using Django Rest Framework
# Postcondition: Maps Django Object To Dictionary And Handles Complex Data Conversion
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('name', 'email', 'password', 'phone')
        extra_kwargs = {
            'password': {'write_only': True}
        }