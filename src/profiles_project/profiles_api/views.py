from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.views import status
from . import serializers

# Create your views here.

class HelloApiView(APIView):
  """Test API"""

  serializer_class = serializers.HelloSerializer

  def get(self, request, format=None):
    """Returns a list of APIview features"""
    apiview_list=[
      'uses HTTP methods as functions',
      'similar to traditional Django Views',
      'Gives you the most control over your logic',
      'is mapped manually to URL',
    ]

    return Response({'message':'Hello!', 'apiview_list':apiview_list})

  def post(self, request):
    """Create hello message with a name"""

    serializer=serializers.HelloSerializer(data=request.data)

    if serializer.is_valid():
      name = serializer.data.get('name')
      message = "Hello {0}".format(name)

      return Response({'message':message})
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk=None):
    """Updates an object"""

    #serializer=serializers.HelloSerializer(data=request.data)

    return Response({'method':'put'})

  def patch(self, request, pk=None):
    """Partially updates an object"""

    #serializer=serializers.HelloSerializer(data=request.data)

    return Response({'method':'patch'})

  def delete(self, request, pk=None):
    """Deletes an object"""

    #serializer=serializers.HelloSerializer(data=request.data)

    return Response({'method':'delete'})
