from rest_framework import serializers
from .models import Lecture
import cloudinary.uploader
from instructor.serializer import InstructorSerializer  


class LectureSerializer(serializers.ModelSerializer):
    file = serializers.FileField(write_only=True, required=True)  
    instructor = InstructorSerializer(read_only=True)

    class Meta:
        model = Lecture
        fields = ['file', 'lecture_url', 'subject_name','instructor', 'published_on']
        
        extra_kwargs = {
            'lecture_url': {'read_only': True}
        }

    def create(self, validated_data):
        file = validated_data.pop('file', None)

        if file:
            uploaded = cloudinary.uploader.upload(file, resource_type="auto")  
            
            validated_data['lecture_url'] = uploaded['secure_url']
        
        return Lecture.objects.create(**validated_data)
