from django.urls import path, include
from .views import *


urlpatterns = [
    path("", index, name="index"),
    path("update-task/<int:pk>",updatetask, name="update"),
    path("delete-task/<int:pk>",deleteTask, name="delete"),
    
]
