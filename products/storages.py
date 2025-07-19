from storages.backends.s3boto3 import S3Boto3Storage


class OverwriteS3Storage(S3Boto3Storage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            self.delete(name)
        return name
