from django.http import JsonResponse,HttpResponse
import requests
from django.views import View
from .models import CapturedRequests,CapturedResponses
import logging
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt



# Configure logging once
logger = logging.getLogger("proxy_logger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("proxy.log")  # log file in project root
formatter = logging.Formatter("%(asctime)s - %(message)s")
file_handler.setFormatter(formatter)

# Avoid duplicate handlers on reload
if not logger.handlers:
    logger.addHandler(file_handler)

# Create your views here.
@method_decorator(csrf_exempt, name="dispatch")
class Catch(View):
    def dispatch(self, request, *args, **kwargs):
        method = request.method
        headers = {k.lower(): str(v) for k, v in request.headers.items()}
        body = request.body.decode("utf-8") if request.body else None
        client_ip = request.META.get("REMOTE_ADDR")

        forward_url = headers.get("x-forward-url")
        response_data, status_code = None, 200
        response=None

        if forward_url:
            try:
                response = requests.request(
                    method=method,
                    url=forward_url,
                    headers=headers,
                    data=request.body
                )
                response_data = response.text
                status_code = response.status_code

                # Save response
                CapturedResponses.objects.create(
                    response_status=response.status_code,
                    response_headers=dict(response.headers),
                    response_body=response.text
                )
            except Exception as e:
                response_data = {"error": str(e)}
                status_code = 500

        # Save request
        CapturedRequests.objects.create(
            method=method,
            headers = headers
,
            body=body,
            forward_url=forward_url or "",
            client_ip=client_ip
        )

        log_entry = f"""
            === New Request ===
            Method: {method}
            Client IP: {client_ip}
            Forward URL: {forward_url}
            Headers: {headers}
            Body: {body}

            --- Response ---
            Status Code: {status_code}
            Headers: {dict(response.headers) if forward_url and response else None}
            Body: {str(response_data)[:500]}
            ====================
                """

        logger.info(log_entry)


        return HttpResponse(
            response_data if response_data else f"Captured {method} request",
            status=status_code,
            content_type = (
                response.headers.get("Content-Type", "text/plain")
                if forward_url and response else "text/plain"
            )

                    )
