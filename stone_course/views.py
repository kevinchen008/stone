from rest_framework import viewsets,authentication,permissions
from .models import Course
from .serializers import CourseSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import list_route,detail_route

# Create your views here.
# -*- coding:utf-8 -*-
# Create your models here.

User = get_user_model()

class DefaultMixin(object):
    authentication_classes = {
        authentication.TokenAuthentication
    }
    permissions_classes = {
        permissions.IsAuthenticated
    }
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100

class CourseViewSet(DefaultMixin,viewsets.ModelViewSet):
    queryset = Course.objects.order_by('created')
    serializer_class = CourseSerializer

    @list_route(url_path='getCourselist')
    def get_courses(self, request, *args, **kwargs):
        return Response({'succss':True,'msg':'success'})

    @detail_route(methods=['get'])
    def details_couse(self, request, pk=None):
        return Response({'succss': True, 'msg':'success'})

