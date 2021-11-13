from rest_framework import serializers
from .models import PostApi


class PostAPISerializers(serializers.ModelSerializer):
    class Meta:
        model = PostApi
        fields = '__all__'
