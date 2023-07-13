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


class TransactionStream(ChargebeeStream):

    name = "transactions"
    path = "/transactions"
    primary_keys = ["id"]
    replication_key = "updated_at"
    records_jsonpath = "$.list[*].transaction"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("customer_id", th.StringType),
        th.Property("subscription_id", th.StringType),
        th.Property("gateway_account_id", th.StringType),
        th.Property("payment_source_id", th.StringType),
        th.Property("payment_method", th.StringType),
        th.Property("gateway", th.StringType),
        th.Property("type", th.StringType),
        th.Property("date", th.IntegerType),
        th.Property("settled_at", th.IntegerType),
        th.Property("exchange_rate", th.NumberType),
        th.Property("amount", th.IntegerType),
        th.Property("id_at_gateway", th.StringType),
        th.Property("status", th.StringType),
        th.Property("updated_at", th.IntegerType),
        th.Property("resource_version", th.IntegerType),
        th.Property("deleted", th.BooleanType),
        th.Property("object", th.StringType),
        th.Property("masked_card_number", th.StringType),
        th.Property("currency_code", th.StringType),
        th.Property("base_currency_code", th.StringType),
        th.Property("amount_unused", th.NumberType),
        th.Property("linked_invoices", th.ArrayType(th.ObjectType())),
        th.Property("linked_refunds", th.ArrayType(th.ObjectType())),
        th.Property("business_entity_id", th.StringType),
        th.Property("payment_method_details", th.ObjectType()),
    ).to_dict()


class BusinessEntitiesStream(ChargebeeStream):

    name = "business_entities"
    path = "/business_entities"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$.list[*].business_entity"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("status", th.StringType),
        th.Property("deleted", th.BooleanType),
        th.Property("created_at", th.IntegerType),
        th.Property("updated_at", th.IntegerType),
        th.Property("timezone", th.StringType),
        th.Property("resource_version", th.IntegerType),
        th.Property("object", th.StringType),
    ).to_dict()


class CouponsStream(ChargebeeStream):

    name = "coupons"
    path = "/coupons"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$.list[*].coupon"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("invoice_name", th.StringType),
        th.Property("discount_type", th.IntegerType),
        th.Property("discount_percentage", th.NumberType),
        th.Property("discount_amount", th.NumberType),
        th.Property("currency_code", th.StringType),
        th.Property("duration_type", th.StringType),
        th.Property("duration_month", th.IntegerType),
        th.Property("max_redemptions", th.IntegerType),
        th.Property("status", th.StringType),
        th.Property("apply_discount_on", th.StringType),
        th.Property("apply_on", th.StringType),
        th.Property("plan_constraint", th.StringType),
        th.Property("addon_constraint", th.StringType),
        th.Property("created_at", th.DateTimeType),
        th.Property("archived_at", th.DateTimeType),
        th.Property("resource_version", th.IntegerType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("object", th.StringType),
        th.Property("redemptions", th.IntegerType),
        th.Property("plan_ids", th.ArrayType(th.StringType)),
        th.Property("addon_ids", th.ArrayType(th.StringType)),
        th.Property("invoice_notes", th.StringType),
        th.Property("meta_data", th.ObjectType()),
    ).to_dict()


class CreditNotesStream(ChargebeeStream):

    name = "credit_notes"
    path = "/credit_notes"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$.list[*].credit_note"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("customer_id", th.StringType),
        th.Property("subscription_id", th.StringType),
        th.Property("reference_invoice_id", th.StringType),
        th.Property("type", th.StringType),
        th.Property("reason_code", th.StringType),
        th.Property("status", th.StringType),
        th.Property("date", th.IntegerType),
        th.Property("price_type", th.StringType),
        th.Property("exchange_rate", th.NumberType),
        th.Property("total", th.NumberType),
        th.Property("amount_allocated", th.NumberType),
        th.Property("amount_refunded", th.NumberType),
        th.Property("amount_available", th.NumberType),
        th.Property("generated_at", th.IntegerType),
        th.Property("updated_at", th.IntegerType),
        th.Property("channel", th.StringType),
        th.Property("resource_version", th.IntegerType),
        th.Property("deleted", th.BooleanType),
        th.Property("object", th.StringType),
        th.Property("create_reason_code", th.StringType),
        th.Property("currency_code", th.StringType),
        th.Property("round_off_amount", th.NumberType),
        th.Property("fractional_correction", th.NumberType),
        th.Property("is_digital", th.BooleanType),
        th.Property("base_currency_code", th.StringType),
        th.Property("sub_total", th.NumberType),
        th.Property("line_items", th.ArrayType(th.ObjectType())),
        th.Property("taxes", th.ArrayType(th.ObjectType())),
        th.Property("line_item_taxes", th.ArrayType(th.ObjectType())),
        th.Property("line_item_discounts", th.ArrayType(th.ObjectType())),
        th.Property("linked_refunds", th.ArrayType(th.ObjectType())),
        th.Property("allocations", th.ArrayType(th.ObjectType())),
        th.Property("billing_address", th.ObjectType()),
    ).to_dict()


class OrdersStream(ChargebeeStream):

    name = "orders"
    path = "/orders"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$.list[*].order"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("document_number", th.StringType),
        th.Property("invoice_id", th.StringType),
        th.Property("subscription_id", th.StringType),
        th.Property("customer_id", th.StringType),
        th.Property("status", th.StringType),
        th.Property("cancellation_reason", th.StringType),
        th.Property("payment_status", th.StringType),
        th.Property("order_type", th.StringType),
        th.Property("price_type", th.StringType),
        th.Property("reference_id", th.StringType),
        th.Property("fulfillment_status", th.StringType),
        th.Property("order_date", th.DateTimeType),
        th.Property("shipping_date", th.DateTimeType),
        th.Property("note", th.StringType),
        th.Property("tracking_id", th.StringType),
        th.Property("batch_id", th.StringType),
        th.Property("created_by", th.StringType),
        th.Property("shipment_carrier", th.StringType),
        th.Property("invoice_round_off_amount", th.IntegerType),
        th.Property("tax", th.IntegerType),
        th.Property("amount_paid", th.IntegerType),
        th.Property("amount_adjusted", th.IntegerType),
        th.Property("refundable_credits_issued", th.IntegerType),
        th.Property("refundable_credits", th.IntegerType),
        th.Property("rounding_adjustement", th.IntegerType),
        th.Property("paid_on", th.DateTimeType),
        th.Property("shipping_cut_off_date", th.DateTimeType),
        th.Property("created_at", th.DateTimeType),
        th.Property("status_update_at", th.DateTimeType),
        th.Property("delivered_at", th.DateTimeType),
        th.Property("shipped_at", th.DateTimeType),
        th.Property("resource_version", th.IntegerType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("cancelled_at", th.DateTimeType),
        th.Property("discount", th.IntegerType),
        th.Property("sub_total", th.IntegerType),
        th.Property("total", th.IntegerType),
        th.Property("deleted", th.BooleanType),
        th.Property("currency_code", th.StringType),
        th.Property("is_gifted", th.BooleanType),
        th.Property("gift_note", th.StringType),
        th.Property("gift_id", th.StringType),
        th.Property("order_line_items", th.ArrayType(th.ObjectType())),
        th.Property("shipping_address", th.ObjectType()),
        th.Property("billing_address", th.ObjectType()),
        th.Property("line_item_taxes", th.ArrayType(th.ObjectType())),
        th.Property("line_item_discounts", th.ArrayType(th.ObjectType())),
        th.Property("linked_credit_notes", th.ArrayType(th.ObjectType())),
    ).to_dict()


class PaymentSourcesStream(ChargebeeStream):

    name = "payment_sources"
    path = "/payment_sources"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$.list[*].payment_source"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("updated_at", th.IntegerType),
        th.Property("resource_version", th.IntegerType),
        th.Property("deleted", th.BooleanType),
        th.Property("object", th.StringType),
        th.Property("customer_id", th.StringType),
        th.Property("type", th.StringType),
        th.Property("reference_id", th.StringType),
        th.Property("status", th.StringType),
        th.Property("gateway", th.StringType),
        th.Property("gateway_account_id", th.StringType),
        th.Property("created_at", th.IntegerType),
        th.Property("card", th.ObjectType()),
        th.Property("business_entity_id", th.StringType),
    ).to_dict()


class GiftsStream(ChargebeeStream):

    name = "gifts"
    path = "/gifts"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$.list[*].gift"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("status", th.StringType),
        th.Property("scheduled_at", th.DateTimeType),
        th.Property("auto_claim", th.BooleanType),
        th.Property("claim_expiry_date", th.DateTimeType),
        th.Property("resource_version", th.IntegerType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("gifter", th.ObjectType()),
        th.Property("gift_receiver", th.ObjectType()),
        th.Property("gift_timelines", th.ObjectType()),
    ).to_dict()


class ItemsStream(ChargebeeStream):

    name = "items"
    path = "/items"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$.list[*].item"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("description", th.StringType),
        th.Property("status", th.StringType),
        th.Property("channel", th.StringType),
        th.Property("resource_version", th.IntegerType),
        th.Property("updated_at", th.IntegerType),
        th.Property("item_family_id", th.StringType),
        th.Property("type", th.StringType),
        th.Property("is_shippable", th.BooleanType),
        th.Property("is_giftable", th.BooleanType),
        th.Property("redirect_url", th.StringType),
        th.Property("enabled_for_checkout", th.BooleanType),
        th.Property("enabled_in_portal", th.BooleanType),
        th.Property("included_in_mrr", th.BooleanType),
        th.Property("item_applicability", th.StringType),
        th.Property("gift_claim_redirect_url", th.StringType),
        th.Property("unit", th.StringType),
        th.Property("metered", th.BooleanType),
        th.Property("usage_calculation", th.StringType),
        th.Property("metadata", th.ObjectType()),
        th.Property("custom_fields", th.ObjectType()),
        th.Property("applicable_items", th.ArrayType(th.ObjectType())),
    ).to_dict()


class ItemPricesStream(ChargebeeStream):

    name = "item_prices"
    path = "/item_prices"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$.list[*].item_price"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("item_family_id", th.StringType),
        th.Property("item_id", th.StringType),
        th.Property("description", th.StringType),
        th.Property("status", th.StringType),
        th.Property("external_name", th.StringType),
        th.Property("pricing_model", th.StringType),
        th.Property("price", th.IntegerType),
        th.Property("period", th.IntegerType),
        th.Property("currency_code", th.StringType),
        th.Property("period_unit", th.StringType),
        th.Property("trial_period", th.IntegerType),
        th.Property("trial_period_unit", th.StringType),
        th.Property("shipping_period_unit", th.StringType),
        th.Property("billing_cycles", th.IntegerType),
        th.Property("free_quantity", th.IntegerType),
        th.Property("resource_version", th.IntegerType),
        th.Property("updated_at", th.IntegerType),
        th.Property("created_at", th.IntegerType),
        th.Property("invoice_notes", th.StringType),
        th.Property("is_taxable", th.BooleanType),
        th.Property("metadata", th.ObjectType()),
        th.Property("item_type", th.StringType),
        th.Property("show_description_in_invoices", th.BooleanType),
        th.Property("show_description_in_quotes", th.BooleanType),
        th.Property("cf_product_code", th.StringType),
        th.Property("channel", th.StringType),
        th.Property("tiers", th.ArrayType(th.ObjectType())),
        th.Property("tax_detail", th.ObjectType()),
        th.Property("accounting_detail", th.ObjectType()),
    ).to_dict()


class ItemFamiliesStream(ChargebeeStream):

    name = "item_families"
    path = "/item_families"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$.list[*].item_family"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("description", th.StringType),
        th.Property("status", th.StringType),
        th.Property("resource_version", th.IntegerType),
        th.Property("updated_at", th.IntegerType),
        th.Property("object", th.StringType),
        th.Property("channel", th.StringType),
    ).to_dict()


class InvoicesStream(ChargebeeStream):

    name = "invoices"
    path = "/invoices"
    primary_keys = ["id"]
    replication_key = "updated_at"
    records_jsonpath = "$.list[*].invoice"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("customer_id", th.StringType),
        th.Property("subscription_id", th.StringType),
        th.Property("recurring", th.BooleanType),
        th.Property("status", th.StringType),
        th.Property("price_type", th.StringType),
        th.Property("date", th.IntegerType),
        th.Property("due_date", th.IntegerType),
        th.Property("net_term_days", th.IntegerType),
        th.Property("exchange_rate", th.NumberType),
        th.Property("total", th.NumberType),
        th.Property("amount_paid", th.NumberType),
        th.Property("amount_adjusted", th.NumberType),
        th.Property("write_off_amount", th.NumberType),
        th.Property("credits_applied", th.NumberType),
        th.Property("amount_due", th.NumberType),
        th.Property("paid_at", th.IntegerType),
        th.Property("updated_at", th.IntegerType),
        th.Property("resource_version", th.IntegerType),
        th.Property("deleted", th.BooleanType),
        th.Property("object", th.StringType),
        th.Property("first_invoice", th.BooleanType),
        th.Property("amount_to_collect", th.NumberType),
        th.Property("round_off_amount", th.NumberType),
        th.Property("new_sales_amount", th.NumberType),
        th.Property("has_advance_charges", th.BooleanType),
        th.Property("currency_code", th.StringType),
        th.Property("base_currency_code", th.StringType),
        th.Property("generated_at", th.IntegerType),
        th.Property("is_gifted", th.BooleanType),
        th.Property("term_finalized", th.BooleanType),
        th.Property("channel", th.StringType),
        th.Property("is_digital", th.BooleanType),
        th.Property("tax", th.NumberType),
        th.Property("line_items", th.ArrayType(th.ObjectType())),
        th.Property("taxes", th.ArrayType(th.ObjectType())),
        th.Property("line_item_taxes", th.ArrayType(th.ObjectType())),
        th.Property("sub_total", th.NumberType),
        th.Property("linked_payments", th.ArrayType(th.ObjectType())),
        th.Property("applied_credits", th.ArrayType(th.ObjectType())),
        th.Property("adjustment_credit_notes", th.ArrayType(th.ObjectType())),
        th.Property("issued_credit_notes", th.ArrayType(th.ObjectType())),
        th.Property("linked_orders", th.ArrayType(th.ObjectType())),
        th.Property("dunning_attempts", th.ArrayType(th.ObjectType())),
        th.Property("billing_address", th.ObjectType()),
        th.Property("business_entity_id", th.StringType),
    ).to_dict()


class PromotionalCreditsStream(ChargebeeStream):

    name = "promotional_credits"
    path = "/promotional_credits"
    primary_keys = ["id"]
    replication_key = "created_at"
    records_jsonpath = "$.list[*].promotional_credit"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("customer_id", th.StringType),
        th.Property("type", th.StringType),
        th.Property("amount", th.StringType),
        th.Property("currency_code", th.StringType),
        th.Property("description", th.StringType),
        th.Property("credit_type", th.StringType),
        th.Property("reference", th.StringType),
        th.Property("closing_balance", th.IntegerType),
        th.Property("done_by", th.StringType),
        th.Property("created_at", th.DateTimeType),
    ).to_dict()


class VirtualBankAccountsStream(ChargebeeStream):

    name = "virtual_bank_accounts"
    path = "/virtual_bank_accounts"
    primary_keys = ["id"]
    replication_key = "updated_at"
    records_jsonpath = "$.list[*].virtual_bank_account"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("customer_id", th.StringType),
        th.Property("email", th.StringType),
        th.Property("bank_name", th.StringType),
        th.Property("account_number", th.StringType),
        th.Property("routing_number", th.StringType),
        th.Property("swift_code", th.StringType),
        th.Property("gateway", th.StringType),
        th.Property("gateway_account_id", th.StringType),
        th.Property("resource_version", th.IntegerType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("created_at", th.DateTimeType),
        th.Property("reference_id", th.StringType),
        th.Property("deleted", th.BooleanType),
        th.Property("object", th.StringType),
    ).to_dict()


class UnbilledChargesStream(ChargebeeStream):

    name = "unbilled_charges"
    path = "/unbilled_charges"
    primary_keys = ["id"]
    replication_key = "updated_at"
    records_jsonpath = "$.list[*].unbilled_charge"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("customer_id", th.StringType),
        th.Property("subscription_id", th.StringType),
        th.Property("date_from", th.DateTimeType),
        th.Property("date_to", th.DateTimeType),
        th.Property("unit_amount", th.IntegerType),
        th.Property("pricing_model", th.StringType),
        th.Property("quantity", th.IntegerType),
        th.Property("amount", th.IntegerType),
        th.Property("currency_code", th.StringType),
        th.Property("discount_amount", th.IntegerType),
        th.Property("description", th.IntegerType),
        th.Property("entity_type", th.IntegerType),
        th.Property("entity_id", th.IntegerType),
        th.Property("is_voided", th.BooleanType),
        th.Property("voided_at", th.DateTimeType),
        th.Property("deleted", th.BooleanType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("tiers", th.ArrayType(th.ObjectType())),
        th.Property("unit_amount_in_decimal", th.StringType),
        th.Property("quantity_in_decimal", th.StringType),
        th.Property("amount_in_decimal", th.StringType),
    ).to_dict()


class InvoicedUnbilledChargesStream(ChargebeeStream):

    name = "invoiced_unbilled_charges"
    path = "/unbilled_charges/invoiced"
    primary_keys = ["id"]
    replication_key = "updated_at"
    records_jsonpath = "$.list[*].unbilled_charge"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("customer_id", th.StringType),
        th.Property("subscription_id", th.StringType),
        th.Property("date_from", th.DateTimeType),
        th.Property("date_to", th.DateTimeType),
        th.Property("unit_amount", th.IntegerType),
        th.Property("pricing_model", th.StringType),
        th.Property("quantity", th.IntegerType),
        th.Property("amount", th.IntegerType),
        th.Property("currency_code", th.StringType),
        th.Property("discount_amount", th.IntegerType),
        th.Property("description", th.IntegerType),
        th.Property("entity_type", th.IntegerType),
        th.Property("entity_id", th.IntegerType),
        th.Property("is_voided", th.BooleanType),
        th.Property("voided_at", th.DateTimeType),
        th.Property("deleted", th.BooleanType),
        th.Property("updated_at", th.DateTimeType),
        th.Property("tiers", th.ArrayType(th.ObjectType())),
    ).to_dict()
