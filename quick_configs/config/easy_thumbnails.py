

class EasyThumbnails(object):

    @property
    def THUMBNAIL_DEBUG(self):
        return self.DEBUG

    THUMBNAIL_PROCESSORS = (
        'easy_thumbnails.processors.colorspace',
        'easy_thumbnails.processors.autocrop',
        'filer.thumbnail_processors.scale_and_crop_with_subject_location',
        'easy_thumbnails.processors.filters'
    )
    # For easy_thumbnails to support retina displays (recent MacBooks, iOS)
    THUMBNAIL_HIGH_RESOLUTION = True
