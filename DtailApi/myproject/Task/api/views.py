from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Task.models import MyObject
from Task.api.serializers import MyObjectSerializer

class MyObjectView(APIView):
    def post(self, request):
        number = request.data.get('number')
        id = request.headers.get('id')

        try:
            obj = MyObject.objects.get(number=number, id=id)
            serializer = MyObjectSerializer(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except MyObject.DoesNotExist:
            return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)