from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
import psutil
import os
# Create your views here.

class MemoryInfoView(APIView):
    def get(self, request, *args, **kwargs):
        memo_info = psutil.virtual_memory()._asdict()
        seri = MemoryInfoSerializer(data=memo_info)
        if seri.is_valid():
            return Response(seri.data)
        return Response(seri.errors,status=400)


class CpuInfoView(APIView):
    def get(self, request, *args, **kwargs):
        cpu_info = psutil.cpu_percent()
        info = {"info":cpu_info}
        seri= CpuInfoSerializer(data=info)
        if seri.is_valid():
            return Response(seri.data)
        return Response(seri.errors,status=400)

class HardInfoView(APIView):
    def get(self,request,*args,**kwargs):
        hard_info = psutil.disk_usage(os.getcwd())._asdict()
        seri = HardInfoSerializer(data=hard_info)
        if seri.is_valid():
            return Response(seri.data)
        return Response(seri.errors,status=400)

