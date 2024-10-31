from rest_framework import serializers

class MemoryInfoSerializer(serializers.Serializer):
    total = serializers.IntegerField()
    available = serializers.IntegerField()
    percent = serializers.FloatField()
    used = serializers.IntegerField()
    free = serializers.IntegerField()
    active = serializers.IntegerField()
    inactive = serializers.IntegerField()
    buffers = serializers.IntegerField()
    cached = serializers.IntegerField()
    shared = serializers.IntegerField()
    
    
class CpuInfoSerializer(serializers.Serializer):
    info = serializers.FloatField()

class HardInfoSerializer(serializers.Serializer):
    total = serializers.IntegerField()
    used = serializers.IntegerField()
    free = serializers.IntegerField()
    percent = serializers.FloatField()
    
