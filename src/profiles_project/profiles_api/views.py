from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response

# Create your views here.

class HelloApiView(APIView):
  """Test API"""
  def get(self, request, format=None):
    """Returns a list of APIview features"""
    apiview_list=[
      'uses HTTP methods as functions',
      'similar to traditional Django Views',
      'Gives you the most control over your logic',
      'is mapped manually to URL',
    ]

    return Response({'message':'Hello!', 'apiview_list':apiview_list})
