from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class DemoView(APIView):
    def get(self, request):
        content = {'message': 'Hello! This is a Demo!'}
        return Response(content)