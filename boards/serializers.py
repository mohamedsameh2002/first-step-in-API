from rest_framework import serializers
from .models import *



class BoardSerializers(serializers.ModelSerializer):
    class Meta:
        model=Board
        fields=['name','description']


class TopicSerializers(serializers.ModelSerializer):
    boards=BoardSerializers(many=True,read_only=True)
    border_name=serializers.CharField(source="board.name",required=False)
    creater_name=serializers.CharField(source="created_by.username",required=False)
    class Meta:
        model=Topic
        fields='__all__'


class PostSerializers(serializers.ModelSerializer):
    topics=TopicSerializers(many=True,read_only=True,required=False)
    class Meta:
        model=Post
        fields='__all__'