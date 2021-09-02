from django.http import HttpResponse


class StripeWH_Handler:
    """Handling stripe webhooks"""

    def __init__(self, request):
        self.request = request
    
    def handle_event(self, event):
        """
        This handles a generic or unknown webhook event"
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200
)