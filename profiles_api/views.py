from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test api View """
    def get(self, request, format=None):
        """Return a list of api formate"""
        an_apiview = [
            'User HTTP methods as function (get, post, patch, put, delete)',
            'Is simeler to a treditional dejango views',
            'Gives you the most control over your application logic',
            'Is Mapped manually to Urls',
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

