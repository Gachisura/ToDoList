from django.urls import include, path
from .views import ToDoBoard, ToDoListDetail
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'ToDoList', ToDoBoard)
router.register(r'ToDoListDetail', ToDoListDetail, basename='todolistdetail')


urlpatterns = [
    path('api/', include(router.urls)),
]
