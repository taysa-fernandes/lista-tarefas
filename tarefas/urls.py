from django.urls import path, include
from rest_framework.routers import DefaultRouter
from listas.views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]