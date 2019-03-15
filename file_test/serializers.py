from rest_framework import serializers
from .models import Profile,FileUpload

class ProfileSerializer(serializers.ModelSerializer):
    def validate_pic(self,pic):
        limit = 5242880
        if pic.size >limit:
            raise serializers.ValidationError("File too large. Size should not exceed 50 MiB.")
        return pic
    class Meta:
        model = Profile
        fields = '__all__'

class ProfilePicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['pic']
class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        read_only_fields = ('created', 'datafile')