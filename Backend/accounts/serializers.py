from rest_framework import serializers
from .models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','first_name','last_name',
        'email','phone_number','role','date_joined']
        read_only_fields=['id','role','date_joined']

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    password2=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username','email','password','password2','first_name',
        'last_name','phone_number']
   
    
    def validate(self,attrs):
        if attrs['password']!=attrs['password2']:
            raise serializers.ValidationError({"password":"Passwords do not match."}) 
        return attrs
    def create(self,validated_data):
        validated_data.pop('password2')
        validated_data['role']='customer'
        user=User.objects.create_user(
            **validated_data
        )
        return user



