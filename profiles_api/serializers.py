from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serliaizes a name field for testing our APIView."""
    name = serializers.CharField(max_length=10)
