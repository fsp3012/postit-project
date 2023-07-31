from rest_framework import serializers
from .models import Stories

class StoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stories
        # fields = ('author', 'tags') to serialize specific field
        fields = '__all__'
        depth = 2
