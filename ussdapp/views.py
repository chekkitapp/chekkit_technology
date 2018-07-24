from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
# from django.utils import simplejson
from psycopg2.extensions import JSON

from .models import ProductCode
from .includes import code as cd
import hashlib, uuid

# Create your views here.
def codes(request):
    # Asked for codes to be generated
    if(request.method == "GET"):
        # FIXME change GET to POST
        #
        POST = request.GET
        # codes will hold a list os generated codes
        codes = cd.generate_codes(POST["company_code"], POST["product_line_code"], POST["quantity"])

        for code in codes:
            # make a row of data and save it
            codes_set = cd.split_code(code)
            new_code = ProductCode(company_code = codes_set[0],
                                   product_line_code =  codes_set[1],
                                   product_code = codes_set[2])
            new_code.save()
            pass
        # codes now contains the unhashed versions themselves
        # TODO handle the writing of the hashed codes to the database
        # Then return a response to the request

        return JsonResponse({"codes" : codes})






    if(request.method == "POST"):
        POST = request.POST
        # codes = cd.generate_codes(POST["company_code"], POST["product_line_code"], POST["quantity"])

