"""Chargebee tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_chargebee import streams


class TapChargebee(Tap):
    """Chargebee tap class."""

    name = "tap-chargebee"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="Chargebee API key",
        ),
        th.Property(
            "site_id",
            th.StringType,
            required=True,
            description="ID for your Chargebee site (first part of the URL)",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        ),
        th.Property(
            "include_deleted",
            th.BooleanType,
            description="Whether or not to include deleted records",
            default=True,
        ),
        th.Property(
            "limit",
            th.IntegerType,
            description="Page size limit for API calls",
            default=10,
        )
    ).to_dict()

    def discover_streams(self) -> list[streams.ChargebeeStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.BusinessEntitiesStream(self),
            streams.CreditNotesStream(self),
            streams.CouponsStream(self),
            streams.CustomerStream(self),
            streams.EventsStream(self),
            streams.GiftsStream(self),
            streams.InvoicedUnbilledChargesStream(self),
            streams.InvoicesStream(self),
            streams.ItemsStream(self),
            streams.ItemFamiliesStream(self),
            streams.ItemPricesStream(self),
            streams.OrdersStream(self),
            streams.PaymentSourcesStream(self),
            streams.PromotionalCreditsStream(self),
            streams.SubscriptionsStream(self),
            streams.TransactionStream(self),
            streams.UnbilledChargesStream(self),
            streams.VirtualBankAccountsStream(self),
        ]


if __name__ == "__main__":
    TapChargebee.cli()
