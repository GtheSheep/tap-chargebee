"""REST client handling, including ChargebeeStream base class."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Callable, Iterable

import requests
from singer_sdk.authenticators import BasicAuthenticator
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.helpers._typing import TypeConformanceLevel
from singer_sdk.pagination import BaseAPIPaginator  # noqa: TCH002
from singer_sdk.streams import RESTStream

_Auth = Callable[[requests.PreparedRequest], requests.PreparedRequest]


class ChargebeeStream(RESTStream):
    """Chargebee stream class."""

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return "https://{site_id}.chargebee.com/api/v2".format(site_id=self.config['site_id'])

    records_jsonpath = "$.list[*]"
    next_page_token_jsonpath = "$.next_offset"  # noqa: S105
    TYPE_CONFORMANCE_LEVEL = TypeConformanceLevel.ROOT_ONLY

    @property
    def authenticator(self) -> BasicAuthenticator:
        """Return a new authenticator object.

        Returns:
            An authenticator instance.
        """
        return BasicAuthenticator.create_for_stream(
            self,
            username=self.config.get("api_key", ""),
            password="",
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        return headers

    def get_new_paginator(self) -> BaseAPIPaginator:
        """Create a new pagination helper instance.

        If the source API can make use of the `next_page_token_jsonpath`
        attribute, or it contains a `X-Next-Page` header in the response
        then you can remove this method.

        If you need custom pagination that uses page numbers, "next" links, or
        other approaches, please read the guide: https://sdk.meltano.com/en/v0.25.0/guides/pagination-classes.html.

        Returns:
            A pagination helper instance.
        """
        return super().get_new_paginator()

    def get_url_params(
        self,
        context: dict | None,  # noqa: ARG002
        next_page_token: Any | None,
    ) -> dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization.

        Args:
            context: The stream context.
            next_page_token: The next page index or value.

        Returns:
            A dictionary of URL query parameters.
        """
        params: dict = {
            "include_deleted": self.config['include_deleted'],
            "limit": self.config['limit'],
        }
        if next_page_token:
            params["offset"] = next_page_token
        if self.replication_key:
            try:
                start_time = self.get_starting_timestamp(context)
                start_time_int = int(start_time.timestamp())
            except:
                start_time = self.get_starting_replication_key_value(context)
                try:
                    start_time_int = int(start_time)
                except:
                    import datetime
                    start_time_int = int(datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%SZ").timestamp())
            if start_time_int:
                params[self.replication_key + "[after]"] = str(start_time_int)
            params["sort_by"] = self.replication_key
        return params
