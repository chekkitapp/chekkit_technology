from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
# from django.utils import simplejson
from psycopg2.extensions import JSON

from .import models
from .includes import code as cd
import hashlib, uuid

# Create your views here.
def codes(request):
    # Asked for codes to be generated
    if(request.method == "GET"):
        #
        GET = request.GET
        # codes will hold a list os generated codes
        codes = cd.generate_codes(GET["company_code"], GET["product_line_code"], GET["quantity"])


        return JsonResponse({"codes" : codes})

    #   codes now contains the hashed versions them selves
    #   TODO handle the writing of the hashed codes to the database




    if(request.method == "POST"):
        POST = request.POST
        codes = cd.generate_codes(POST["company_code"], POST["product_line_code"], POST["quantity"])

