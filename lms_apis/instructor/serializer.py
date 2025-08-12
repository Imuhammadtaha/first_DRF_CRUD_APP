from rest_framework import serializers

from .models import Instructor

import cloudinary.uploader

class InstructorSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only = True, required = False)
    email = serializers.EmailField(source =  'user.email', read_only = True)
    
    class Meta:
         model = Instructor
         
         fields = ['name','email','phone','pic_url','image','department','subject']

         extra_kwargs = {
             'pic_url':{'read_only':True}
             
         }
         
    def create(self, validated_data):
         image = validated_data.pop("image",None)
         
         if image:
             uploaded = cloudinary.uploader.upload(image)
             
             validated_data['pic_url'] = uploaded['secure_url']
             
             return Instructor.objects.create(**validated_data)