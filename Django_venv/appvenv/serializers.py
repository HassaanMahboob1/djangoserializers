from rest_framework import serializers
from appvenv.models import Testing

class TestingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Testing
        fields = '__all__'