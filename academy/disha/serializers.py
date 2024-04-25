from rest_framework import serializers
from .models import *


class OfficeStaffSerializer(serializers.ModelSerializer):
    
    # profile = serializers.SerializerMethodField()
    
    class Meta:
        model = OfficeStaff
        fields = '__all__'
        
    profile = serializers.ImageField(required=False)
        
    # def get_profile(self, obj):
    #     if obj.profile:
    #         return obj.profile.url
    #     return None