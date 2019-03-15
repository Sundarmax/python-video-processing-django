from django.shortcuts import render
# Create your views here.
from rest_framework import parsers
from rest_framework import response
from rest_framework import status
from rest_framework import viewsets

from .models import Profile,FileUpload
from .serializers import ProfilePicSerializer
from .serializers import ProfileSerializer,FileUploadSerializer

from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet
from moviepy.editor import *
from pathlib import Path
import magic
import os
import datetime
from moviepy.editor import VideoFileClip

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "example.mp4"
file_to_open = os.path.join(script_dir, rel_path)

class FileUploadViewSet(viewsets.ModelViewSet):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = (MultiPartParser, FormParser,)
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(owner=self.request.user,
                       datafile=self.request.data.get('datafile'))
            return response.Response(serializer.data)
        return response.Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    def pic(self, request, pk):
        obj = self.get_object()
        serializer = self.serializer_class(obj, data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors,
                                 status.HTTP_400_BAD_REQUEST)
def VideoThumbnail():
    clip = VideoFileClip(file_to_open)
    clip.save_frame("thumbnail.jpg",t=1.00)

def getVideoDuration():
    clip = VideoFileClip(file_to_open)
    VideoSec = clip.duration 
    print(VideoSec)
    VideoStr= str(datetime.timedelta(seconds=VideoSec))
    print(VideoStr)

def getMimetype():
    mime = magic.Magic(mime=True)
    mtype = mime.from_file(file_to_open)
    print(mtype)
getMimetype()
getVideoDuration()