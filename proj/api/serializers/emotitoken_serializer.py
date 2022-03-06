from rest_framework import serializers

class EmotitokenSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=512)
