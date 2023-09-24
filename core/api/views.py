from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from core.models import Task


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/tasks',
        'GET /api/tasks/:id',
    ]
    return Response(routes)


@api_view(['GET'])
def getTasks(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTask(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)
