from django.conf import settings
from django.core.files.storage import FileSystemStorage


def get_replay_storage():
    return FileSystemStorage(location=settings.REPLAY_ROOT)
