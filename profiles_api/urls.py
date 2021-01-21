from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'hello-viewset', views.HelloViewSet, basename='hello-viewset')

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]
urlpatterns += router.urls