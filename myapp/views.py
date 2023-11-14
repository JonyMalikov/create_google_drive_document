import requests
from django.http import JsonResponse

# csrf_token = get_token(request)


def create_google_drive_document(request):
    """Создание документа в Google Drive"""
    data = request.POST.get("data")
    name = request.POST.get("name")

    # Отправляем POST запрос к Google Drive API для создания документа
    google_drive_api_url = "https://www.googleapis.com/drive/v3/files"
    headers = {
        "Authorization": "2eb5b2fc490d81908e4803e50f8bdc7b15601f7a",
        "X-CSRFToken": csrf_token,
    }
    payload = {"name": name, "mimeType": "text/plain"}
    files = {"data": data}
    response = requests.post(
        google_drive_api_url, headers=headers, data=payload, files=files
    )

    # Проверяем результат запроса и возвращаем ответ
    if response.status_code == 200:
        return JsonResponse(
            {"message": "Документ успешно создан в Google Drive"}, status=200
        )
    else:
        return JsonResponse(
            {
                "error": "Произошла ошибка при создании документа в Google Drive"
            },
            status=500,
        )
