from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Activity
from .serializers import ActivitySerializer

@api_view(['GET'])
def getData(request):
    activities = Activity.objects.all()
    serializer = ActivitySerializer(activities, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addActivity(request):
    serializer = ActivitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
