from django.http import JsonResponse

def index(request):
    dict = {
        "value1": 1,
        "value2": 2,
        "value3": 3,
        "value4": 4,
        "value5": 5
    }

    return JsonResponse(request, dict)