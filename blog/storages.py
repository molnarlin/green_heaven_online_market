from storages.backends.s3boto3 import S3Boto3Storage


class OverwriteS3Storage(S3Boto3Storage):
    location = ''  # Use the root of the bucket
    default_acl = 'public-read'

    def get_available_name(self, name, max_length=None):
        self.delete(name)
        return name
