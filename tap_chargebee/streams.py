"""Stream type classes for tap-chargebee."""

from __future__ import annotations

from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_chargebee.client import ChargebeeStream


class SubscriptionsStream(ChargebeeStream):

    name = "subscriptions"
    path = "/subscriptions"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$.list[*].subscription"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("billing_period", th.IntegerType),
        th.Property("billing_period_unit", th.StringType),
        th.Property("remaining_billing_cycles", th.IntegerType),
        th.Property("customer_id", th.StringType),
        th.Property("status", th.StringType),
        th.Property("current_term_start", th.IntegerType),
        th.Property("current_term_end", th.IntegerType),
        th.Property("next_billing_at", th.IntegerType),
        th.Property("created_at", th.IntegerType),
        th.Property("started_at", th.IntegerType),
        th.Property("activated_at", th.IntegerType),
        th.Property("updated_at", th.IntegerType),
        th.Property("has_scheduled_changes", th.BooleanType),
        th.Property("channel", th.StringType),
        th.Property("resource_version", th.IntegerType),
        th.Property("deleted", th.BooleanType),
        th.Property("object", th.StringType),
        th.Property("currency_code", th.StringType),
        th.Property("due_invoices_count", th.IntegerType),
        th.Property("mrr", th.NumberType),
        th.Property("exchange_rate", th.NumberType),
        th.Property("base_currency_code", th.StringType),
        th.Property("cf_is_migrated", th.StringType),
        th.Property("has_scheduled_advance_invoices", th.BooleanType),
        th.Property("business_entity_id", th.StringType),
        th.Property("meta_data", th.ObjectType()),
        th.Property("subscription_items", th.ArrayType(
            th.ObjectType()
        )),
    ).to_dict()


class EventsStream(ChargebeeStream):

    name = "events"
    path = "/events"
    primary_keys = ["id"]
    replication_key = "occurred_at"
    records_jsonpath = "$.list[*].event"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("occurred_at", th.IntegerType),
        th.Property("source", th.StringType),
        th.Property("user", th.StringType),
        th.Property("object", th.StringType),
        th.Property("api_version", th.StringType),
        th.Property("content", th.ObjectType(
            th.Property("subscription", th.ObjectType()),
            th.Property("customer", th.ObjectType()),
        )),
        th.Property("event_type", th.StringType),
        th.Property("webhook_status", th.StringType),
        th.Property("webhooks", th.ArrayType(
            th.ObjectType(
                th.Property("id", th.StringType),
                th.Property("webhook_status", th.StringType),
                th.Property("object", th.StringType),
            )
        )),
    ).to_dict()


class CustomerStream(ChargebeeStream):

    name = "customers"
    path = "/customers"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$.list[*].customer"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("first_name", th.StringType),
        th.Property("last_name", th.StringType),
        th.Property("auto_collection", th.StringType),
        th.Property("net_term_days", th.IntegerType),
        th.Property("allow_direct_debit", th.BooleanType),
        th.Property("created_at", th.IntegerType),
        th.Property("taxability", th.StringType),
        th.Property("updated_at", th.IntegerType),
        th.Property("pii_cleared", th.StringType),
        th.Property("channel", th.StringType),
        th.Property("resource_version", th.IntegerType),
        th.Property("deleted", th.BooleanType),
        th.Property("object", th.StringType),
        th.Property("billing_address", th.ObjectType()),
        th.Property("card_status", th.StringType),
        th.Property("promotional_credits", th.IntegerType),
        th.Property("refundable_credits", th.IntegerType),
        th.Property("excess_payments", th.IntegerType),
        th.Property("unbilled_charges", th.IntegerType),
        th.Property("preferred_currency_code", th.StringType),
        th.Property("primary_payment_source_id", th.StringType),
        th.Property("payment_method", th.ObjectType()),
        th.Property("business_entity_id", th.StringType),
        th.Property("tax_providers_fields", th.ArrayType(th.ObjectType())),
        th.Property("cf_is_migrated", th.StringType),
    ).to_dict()
