from rest_framework import serializers
from .models import Category,Course


class CategorySerializer(serializers.Serializer):
    class Meta:
           model = Category
           fields = {'id','created','sort','isDisabled','cid','pid','creater'}


class CourseSerializer(serializers.Serializer):
    class Meta:
           model = Course
           fields = {'id','created','name','linkSrc','pirce','level','sort','isDisabled','categoryId','creater'}

    def create(self, validated_data):
        return Course.objects.create(**validated_data)
