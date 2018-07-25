# Author Kobina G. Koomson
#

import hashlib
import random, datetime
import uuid

from math import floor


# from ussdapp.models import ProductLine, Product, ProductCode, User, UserCheck, FactoryCheck


def rand_string(config = {"length" : 5}) :
    ###
    """
    This fn generates very random numbers config["length"] is created
    then the current microsecond timestamp is appended to the string
    Firstly a sequence of numbers with length
    :param config: {Dict}
    :return: {String}
    """
    i = 0
    result_string = ""
    while (i < config["length"]) :
        result_string += (str)(random.randint(0, 9))

        i += 1
    return (result_string)


def get_timestamp() :
    return datetime.datetime.timestamp(datetime.datetime.now())


# one_time = (str) (get_timestamp())
# print(one_time)


def generate_codes(company_code: str, product_line: str, quantity: int = 100) :
    """
    Unique code generation engine
    In future the rand_string function maybe replaced by uuid

    This fn generates a number (quantity) of random codes with repeating parts
    The repeating parts are created by concatenating the company_code and the product_line code
    They are prepended to the randomly generated code
    :param company_code: {String<Number>} must have a length of 4
    :param product_line: {String<Number>} must have a length of 2
    :param quantity: Number defaults to 100 codes FIXME set this to a discussed number
    :return:
    """
    # TODO check lengths of company_code and product_line before continuing else throw an error
    # TODO Do Duck-typing on company and product_line codes
    i = 0
    # using a set so that there's no duplicate
    codes = set()
    # create the repeating part of the code one in the lifetime of the function call
    common_code = company_code + product_line
    # make a new code as long as we haven't made the required quantity and
    # the number of codes less than the quantity
    # P.S. making the second check because the codes set will not allow duplicates
    while i < quantity and len(codes) < quantity :
        # get the timestamp {Float}(micro-seconds) and cast it to a string
        time_stamp = (str)(get_timestamp())
        # start code string by adding a randomly string to
        new_code = common_code + rand_string({"length" : 7}) + time_stamp[14 :]
        # make the right string length of each new code if we don't get 16 digits
        # this block will mostly be ignored
        if (len(new_code) < 16) :
            new_code += ("0" * (16 - len(new_code)))

        i = i + 1
        codes.add(new_code)
        # TODO Don't forget to hash codes before saving list to database
        # cast the codes set to a list so it can easily be dealt with in JSON
    return list(codes)


def split_code(code: str) :
    """
    company_code = code[ : 3]
    product_line = code[4 : 5]
    product_code = code[6 : ]
    :param code:
    :return:
    """
    return code[: 3], code[4 : 5], code[6 :]


def check_code(code: str) :
    """

    :param code:
    :return:
    """
    hashed_code = hash_code(code)
    if check_hash_code(hashed_code, code) :
        codes = split_code(code)
        company_code = codes[0]
        product_line = codes[1]
        product_code = codes[2]


def hash_code(code) :
    # uuid is used to generate a random number (salt) to prevent rainbow table attacks
    salt = uuid.uuid4().hex
    hash = hashlib.sha256(salt.encode() + code.encode()).hexdigest() + ':' + salt
    return hash


def check_hash_code(hashed_code, code) :
    password, salt = hashed_code.split(':')
    return password == hashlib.sha256(salt.encode() + code.encode()).hexdigest()


#   TODO write the logic for

# TODO ask what else is associated with a specific code
print(generate_codes("2342", "04", 10))
