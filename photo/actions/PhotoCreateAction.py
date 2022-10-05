from photo.ui.api.transformers.PhotoTransformer import PhotoTransformer
from photo.models.Photo import Photo

class PhotoCreateAction:

    def __init__(self,data) -> None:
        self.data = data

    def run(self):

        photo_transformer = PhotoTransformer(data=self.data)
        photo_transformer.is_valid(raise_exception=True)

        return Photo.objects.create(**photo_transformer.validated_data)