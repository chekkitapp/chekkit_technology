import random, datetime

from math import floor


def rand_string (config = {"length" : 5}):
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
    while (i < config["length"]):
        result_string += (str)(random.randint(0, 9))

        i += 1
    return (result_string)


def get_timestamp():
    return datetime.datetime.timestamp(datetime.datetime.now())

# one_time = (str) (get_timestamp())
# print(one_time)


def generate_codes(company_code, product_line, quantity = 10) :
    """
    This fn generates a number (quantity) of random codes with repeating parts
    The repeating parts are created by concatenating the company_code and the product_line code
    They are prepended to the randomly generated code
    :param company_code: {String<Number>}
    :param product_line: {String<Number>}
    :param quantity: Number
    :return:
    """
    i = 0
    codes = []
    common_code = company_code + product_line
    while i < quantity :
        # get the timestamp {Float} and cast it to a string
        time_stamp = (str)(get_timestamp())

        if (len(time_stamp) == 17) :
            codes.append(common_code + rand_string({"length" : 7}) + time_stamp[14 :])
        else :
            codes.append(common_code + rand_string({"length" : 7}) + time_stamp[14 :] + "0")
        i += 1
    return codes

# TODO ask what else is associated with a specific code

print(generate_codes( "2342", "04", ))