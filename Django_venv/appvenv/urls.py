from django.urls import path

from . import views
from .views import TestingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(
    'TestingViewSet' , TestingViewSet , basename='Testing'
)
# urlpatterns = [
#     path('testingview', views.testingview, name='testingview'),
# ]

urlpatterns = [
    path('hello/' ,views.testingview, name='testingview'),
]+router.urls