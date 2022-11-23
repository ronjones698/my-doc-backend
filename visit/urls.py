from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('visits', views.VisitView,basename='user')
router.register('forms', views.FormScanView, basename='forms')

urlpatterns = [
    path('',include(router.urls)),
]