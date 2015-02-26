from django.http import JsonResponse


def api_error(detail):
    response = JsonResponse({
        'success': False,
        'detail': detail
    })
    response.status_code = 400
    return response
