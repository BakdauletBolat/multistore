from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from photo.actions.PhotoCreateAction import PhotoCreateAction
from photo.ui.api.transformers.PhotoTransformer import PhotoTransformer
from rest_framework.exceptions import ValidationError

class PhotoCreateController(APIView):
    def post(self,request):
        try:
            photo = PhotoCreateAction(request.data).run()
            return Response(data=PhotoTransformer(photo,context={
                'request':request
            }).data,status=status.HTTP_200_OK)
        except ValidationError as validationError:
            return Response(data=validationError.get_full_details(),status=validationError.status_code)
        except Exception as e:
            return Response(data=str(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)