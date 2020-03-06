import json
import requests

from .utils import _get_updated_headers
from .subscription import Subscription


class GraphQLClient:
    def __init__(self, endpoint, headers=None):
        self.endpoint = endpoint
        if not headers or not isinstance(headers, dict):
            headers = {}

        self.headers = headers

    def execute(self, query, variables=None, headers=None):
        h = _get_updated_headers(self.headers, headers)

        if not variables:
            variables = {}

        data = {"query": query, "variables": variables}

        try:
            return requests.post(self.endpoint, json=data, headers=h).json()
        except:
            # TODO need to have proper exception
            # TODO need to log this error
            print("errored")
            pass

    def subscription(self, query, variables=None, headers=None):
        return Subscription(self, query, variables, headers)
