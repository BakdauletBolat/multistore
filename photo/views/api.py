from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from photo.actions.api import PhotoCreateAction
from photo.serializers import PhotoSerializer


class PhotoCreateView(APIView):

    @staticmethod
    def post(request):
        photo = PhotoCreateAction(request.data).run()
        return Response(data=PhotoSerializer(photo, context={
            'request': request
        }).data, status=status.HTTP_200_OK)
