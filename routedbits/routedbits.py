#
#
#

from requests import Session
from types import SimpleNamespace

from routedbits.exceptions import NotFound, TooManyArguments


class RoutedBits(object):
    BASE = "https://dn42.routedbits.io/api"

    def __init__(self):
        self._session = Session()

    def _request(self, method, path, params=None, data=None):
        url = f"{self.BASE}{path}"
        resp = self._session.request(method, url, params=params, json=data)
        if resp.status_code == 404:
            raise NotFound()
        resp.raise_for_status()
        return resp

    def nodes(self, sort_by="city"):
        path = "/routers.json"
        nodes = []

        for name, router in self._request("GET", path).json().items():
            router["name"] = name
            nodes.append(SimpleNamespace(**router))

        return sorted(nodes, key=lambda node: node.__dict__[sort_by])

    def node(self, hostname=None, name=None):
        if hostname and name:
            raise TooManyArguments()

        nodes = self.nodes()
        for node in nodes:
            if hostname:
                if node.hostname == hostname:
                    return node

            if name:
                if node.name == name:
                    return node

        raise NotFound()
