from django.http import JsonResponse
from .tasks import send_email_task

def trigger_email(request):
    send_email_task.delay(
        "Test Subject",
        "This is a test email sent asynchronously via Celery!",
        ["xyz@gmail.com"]
    )
    return JsonResponse({"status": "Email task has been queued!"})