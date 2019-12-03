from flask_restful import reqparse

def page_value(value):
    if not int(value) > 0:
        raise ValueError('The page number has to be greater than 0.')
    return int(value)

pagination_parser = reqparse.RequestParser()
pagination_parser.add_argument('page', type=page_value, default=1)

