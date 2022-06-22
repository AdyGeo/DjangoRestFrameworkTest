
from xml.etree.ElementInclude import include
from django.urls import path
from rest_framework import routers
from . import views
router = routers.DefaultRouter()

router.register('tasks', views.TaskViewSet, 'tasks')
router.register('complete-task', views.TaskUpdatetView, 'complete-task')
router.register('notes', views.NoteViewSet, 'notes')


urlpatterns = router.urls