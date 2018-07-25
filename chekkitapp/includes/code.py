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


def generate_codes(company_code : str, product_line : str, quantity : int = 100) :
    """
    This fn generates a number (quantity) of random codes with repeating parts
    The repeating parts are created by concatenating the company_code and the product_line code
    They are prepended to the randomly generated code
    :param company_code: {String<Number>} must have a length of 4
    :param product_line: {String<Number>} must have a length of 2
    :param quantity: Number defaults to 100 codes FIXME set this to a discussed number
    :return:
    """

    # TODO check lengths of company_code and product_line before continuing else throw an error
    # TODO Do Duck Typing on
    i = 0
    codes = []
    common_code = company_code + product_line
    while i < quantity :
        # get the timestamp {Float}(micro-seconds) and cast it to a string
        time_stamp = (str)(get_timestamp())
        code = common_code + rand_string({"length" : 7})

        if (len(time_stamp) == 17) :
            code += time_stamp[14 :]
        else :
            codes += time_stamp[14 :] + "0"
        i += 1
        codes.append(code)
        # TODO Don't forget to hash passwords before saving list to database
    return codes


def split_code(code : str):
    """
    company_code = code[ : 3]
    product_line = code[4 : 5]
    product_code = code[6 : ]
    :param code:
    :return:
    """
    return  code[: 3], code[4 : 5], code[6 :]

def check_code(code : str):
    codes = split_code(code)
    company_code = codes[0]
    product_line = codes[1]
    product_code = codes[2]


#   TODO write the logic for

# TODO ask what else is associated with a specific code
# print(generate_codes( "2342", "04", ))