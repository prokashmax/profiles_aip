from rest_framework import serializers

class HelloApiSerializer(serializers.Serializer):
    """" serializers a name field for testing Apiview"""
    name = serializers.CharField(max_length=10)