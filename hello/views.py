# import re
# from django.shortcuts import render
from django.utils.timezone import datetime
from .models import LogMessage

# Rest Framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import LogMessageSerializer
from rest_framework import status


@api_view(['GET', 'POST'])
def get_all(request):
    "get all avielable logs"
    if request.method == 'GET':
        logs = LogMessage.objects.all()
        serializer = LogMessageSerializer(logs, many=True)
        return Response({'status': True, 'data': serializer.data, 'message': 'Success'})

    if request.method == 'POST':
        data = request.data
        data['log_date'] = datetime.now()
        serializer = LogMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'data': serializer.data, 'message': 'Data created'}, status=status.HTTP_201_CREATED)
