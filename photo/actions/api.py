from photo.serializers import PhotoSerializer
from photo.models import Photo


class PhotoCreateAction:

    def __init__(self, data) -> None:
        self.data = data

    def run(self):
        photo_transformer = PhotoSerializer(data=self.data)
        photo_transformer.is_valid(raise_exception=True)

        return Photo.objects.create(**photo_transformer.validated_data)
