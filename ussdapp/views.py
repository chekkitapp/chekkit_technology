from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
# from django.utils import simplejson
from psycopg2.extensions import JSON

from ussdapp.models import ProductCode
from ussdapp.includes import code as cd
import hashlib, uuid

# Create your views here.
def getcodes(request):
    # Asked for codes to be generated
    if (request.method == "GET") :
        # FIXME change GET to POST
        #
        POST = request.GET
        if POST :
            # codes will hold a list os generated codes
            codes = cd.generate_codes(POST["company_code"], POST["product_line_code"], (int)(POST["quantity"]))

            # for code in codes :
            #     # make a row of data and save it
            #     codes_set = cd.split_code(code)
            #     # TODO hash code first
            #     new_code = ProductCode(company_code = codes_set[0],
            #                            product_line_code = codes_set[1],
            #                            product_code = codes_set[2])
            #     new_code.save()
            #     pass
            # codes now contains the unhashed versions themselves
            # TODO handle the writing of the hashed codes to the database
            # Then return a response to the request

            return JsonResponse({"codes" : codes})

        else :
            return JsonResponse({"codes" : "No Codes available"})

    if (request.method == "POST") :
        POST = request.POST
        codes = cd.generate_codes(POST["company_code"], POST["product_line_code"], POST["quantity"])

    # TODO create 404 err for any wrong url


def checkcode(request):
    pass