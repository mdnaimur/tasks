from core import models
from rest_framework.serializers import ModelSerializer
from core.models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
