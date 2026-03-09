import core
import requests

class Http(core.module.Module):
    """lets the AI send/receive HTTP requests"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_headers = {
            'User-Agent': 'Mozilla/5.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate'
        }
        self.timeout = 30

    async def _make_request(self, func, url: str, **kwargs):
        headers = self.default_headers if not kwargs.get("headers") else kwargs.get("headers")
        kwargs["timeout"] = self.timeout

        include_content = kwargs.get("include_content")
        if "include_content" in kwargs.keys():
            del(kwargs["include_content"])

        try:
            result = func(url, **kwargs)
        except Exception as e:
            return self.result(e, False)

        response = {
            "status": f"{result.status_code} {result.reason}",
            "headers": result.headers,
            "cookies": result.cookies
        }
        if include_content:
            response["content"] = result.text

        return self.result(response)

    async def get(self, url: str, headers: dict = None, params: dict = None):
        """
        performs a HTTP GET request on url

        Args:
            url: the URL to target
            params: any parameters to add to the request (shows up as the ?q=blah&si=blah2 part of the url)
            headers: HTTP headers
        """
        return await self._make_request(requests.get, url, params=params, headers=headers, include_content=True)

    async def post(self, url: str, headers: dict = None, data: dict = None):
        """
        performs a HTTP POST on url

        Args:
            url: the URL to target
            data: the data to post to the url
            headers: HTTP headers
        """
        return await self._make_request(requests.post, url, data=data, headers=headers, include_content=True)

    async def head(self, url: str, params: dict = None, headers: dict = None):
        """
        performs a HTTP HEAD on url

        Args:
            url: the URL to target
            params: any parameters to add to the request (shows up as the ?q=blah&si=blah2 part of the url)
            headers: HTTP headers
        """
        return await self._make_request(requests.head, url, params=params, headers=headers)

    async def options(self, url: str, params: dict = None, headers: dict = None):
        """
        performs a HTTP OPTIONS on url

        Args:
            url: the URL to target
            params: any parameters to add to the request (shows up as the ?q=blah&si=blah2 part of the url)
            headers: HTTP headers
        """
        return await self._make_request(requests.options, url, params=params, headers=headers)

    async def put(self, url: str, data: dict, headers: dict = None):
        """
        performs a HTTP PJT on url

        Args:
            url: the URL to target
            data: the data to post to the url
            headers: HTTP headers
        """
        return await self._make_request(requests.put, url, data=data, headers=headers, include_content=True)

    async def patch(self, url: str, data: dict, headers: dict = None):
        """
        performs a HTTP PATCH on url

        Args:
            url: the URL to target
            data: the data to post to the url
            headers: HTTP headers
        """
        return await self._make_request(requests.patch, url, data=data, headers=headers, include_content=True)

    async def delete(self, url: str, params: dict = None, headers: dict = None):
        """
        performs a HTTP DELETE on url

        Args:
            url: the URL to target
            params: any parameters to add to the request (shows up as the ?q=blah&si=blah2 part of the url)
            headers: HTTP headers
        """
        return await self._make_request(requests.options, url, params=params, headers=headers, include_content=True)
