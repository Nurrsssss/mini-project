from django.http import JsonResponse

def notification_list(request):
    return JsonResponse({"message": "Notifications endpoint"})
