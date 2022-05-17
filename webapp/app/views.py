from django.shortcuts import render
import requests
import time
import logging

from opentelemetry import trace

logger = logging.getLogger(__name__)
tracer = trace.get_tracer(__name__)

def index(request):
    return render(request, 'app/index.html')

def service(request):

    logger.error("Log1 on Webapp!")

    with tracer.start_as_current_span("API call") as span:
        logger.error("Log2 on Webapp!")

        time.sleep(0.3)
        r = requests.get("http://webapi:8001/add")
        time.sleep(0.3)

        context = {
            'result': r.json()['result']
        }
        return render(request, 'app/service.html', context)