from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import *


@api_view(['GET', 'POST'])
def post_create_read(request):
    if request.method == 'GET':
        post = Post.objects.all()
        serializer = PostSerializer(post,many=True)
        return Response(data=serializer.data)
    
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {"message":f"{serializer.data['writer']}님이 배포에 성공하셨습니다."}
            return Response(data=data)
        
