from django.urls import path,include
from .views import taskpage,updatetask,deletetask,TaskViewset
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('task', TaskViewset,basename='task')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('', taskpage, name = "taskpage"),
    path('update_task/<str:pk>/', updatetask, name = "update_task"),
    path('delete_task/<str:pk>/', deletetask, name = "delete_task"),
]