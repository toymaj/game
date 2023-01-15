from enum import Enum


class HTTPMethod(str, Enum):
    OPTIONS = "OPTIONS"
    GET = "GET"
    HEAD = "HEAD"
    PUT = "PUT"
    POST = "POST"
    DELETE = "DELETE"
    PATCH = "PATCH"
