"""stone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from rest_framework.routers import DefaultRouter
from django.conf.urls import include, url
from . import views

router = DefaultRouter()
router.register(r'course',views.CourseViewSet)
router.register(r'course/(?P<id>\d+)', views.CourseViewSet)

course_list = views.CourseViewSet.as_view({'get': 'list', 'post': 'create'})

urlpatterns = [
    url(r'^course/$', course_list, name='model-list'),
]
