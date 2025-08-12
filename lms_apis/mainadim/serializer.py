from rest_framework import serializers

from .models import MainAdmin

import cloudinary.uploader

class AdminSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only = True, required = False )
    email = serializers.EmailField(source = 'user.email', read_only = True)
    
    class Meta:
        model = MainAdmin
        
        fields = ['name','email','phone','pic_url','image']

        extra_kwargs = {
            'pic_url':{'read_only':True}
        }
        
    def create(self, validated_data):
        image = validated_data.pop('image', None)
        
        if image:
            
            uploaded = cloudinary.uploader.upload(image)
            
            validated_data['pic_url'] = uploaded['secure_url']

        return MainAdmin.objects.create(**validated_data)
