from rest_framework import serializers

class TestSerializer(serializers.Serializer):
    """Testing first serializer"""

    name = serializers.CharField(max_length=10)
