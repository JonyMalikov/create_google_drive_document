from django.urls import path

from myapp.views import create_google_drive_document

urlpatterns = [
    path(
        "create-google-drive-document/",
        create_google_drive_document,
        name="create-google-drive-document",
    ),
]
