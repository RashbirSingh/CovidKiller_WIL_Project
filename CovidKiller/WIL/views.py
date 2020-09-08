from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from CovidKiller import settings

import os

TEMPLATE_DIR_PDFSCANNER = os.path.join(settings.TEMPLATES_DIR, 'CovidKiller')

# Create your views here.

def index(request):
    return render(request, os.path.join(TEMPLATE_DIR_PDFSCANNER, 'index.html'))