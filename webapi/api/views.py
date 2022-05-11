from django.shortcuts import render
from django.http import JsonResponse
import time
import logging

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'api/index.json')

def add(request):
    logger.error("Log on API dude!")
    time.sleep(0.5)
    return JsonResponse({'result':4})