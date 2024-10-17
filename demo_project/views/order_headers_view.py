from cookiecutter.main import cookiecutter
from sqlalchemy import Select
from efficieno.components.view_objects import View, ColumnProperty

from demo_project.data_objects.ont.oe_order_headers_all import OeOrderHeadersAll
from demo_project.data_objects.apps.org_organization_definitions import OrgOrganizationDefinitions
from demo_project.view_actions.independent_action import IndependentAction
from demo_project.view_actions.inline_order_header_update import InlineOrderHeaderUpdate


class OrderHeadersView(View):
    __query__ = (Select(OeOrderHeadersAll, OrgOrganizationDefinitions)
                 .join(OeOrderHeadersAll.OrgOrganizationDefinitions_organization_id))
    __table_header__ = "Order Headers View"
    __table_description__ = "Order Headers View"

    __inline_action__ = InlineOrderHeaderUpdate
    __actions__ = [InlineOrderHeaderUpdate, IndependentAction]

    header_id = ColumnProperty(OeOrderHeadersAll.header_id, display_name="Header ID", primary_key=True, visible=False)
    organization_code = ColumnProperty(OrgOrganizationDefinitions.organization_code, display_name="Organization Code", primary_key=False, visible=True)
    org_id = ColumnProperty(OeOrderHeadersAll.org_id, primary_key=False, visible=True)
    order_type_id = ColumnProperty(OeOrderHeadersAll.order_type_id, primary_key=False, visible=True)
    order_number = ColumnProperty(OeOrderHeadersAll.order_number, primary_key=False, visible=True)
    version_number = ColumnProperty(OeOrderHeadersAll.version_number, primary_key=False, visible=True)
    ordered_date = ColumnProperty(OeOrderHeadersAll.ordered_date, primary_key=False, visible=True)
    request_date = ColumnProperty(OeOrderHeadersAll.request_date, primary_key=False, visible=True)
    pricing_date = ColumnProperty(OeOrderHeadersAll.pricing_date, primary_key=False, visible=True)
    shipment_priority_code = ColumnProperty(OeOrderHeadersAll.shipment_priority_code, primary_key=False, visible=True)
    demand_class_code = ColumnProperty(OeOrderHeadersAll.demand_class_code, primary_key=False, visible=True)
    price_list_id = ColumnProperty(OeOrderHeadersAll.price_list_id, primary_key=False, visible=True)
    tax_exempt_flag = ColumnProperty(OeOrderHeadersAll.tax_exempt_flag, primary_key=False, visible=True)
    tax_exempt_number = ColumnProperty(OeOrderHeadersAll.tax_exempt_number, primary_key=False, visible=True)
    tax_exempt_reason_code = ColumnProperty(OeOrderHeadersAll.tax_exempt_reason_code, primary_key=False, visible=True)
    conversion_rate = ColumnProperty(OeOrderHeadersAll.conversion_rate, primary_key=False, visible=True)
    conversion_type_code = ColumnProperty(OeOrderHeadersAll.conversion_type_code, primary_key=False, visible=True)
    conversion_rate_date = ColumnProperty(OeOrderHeadersAll.conversion_rate_date, primary_key=False, visible=True)
    partial_shipments_allowed = ColumnProperty(OeOrderHeadersAll.partial_shipments_allowed, primary_key=False, visible=True)
    ship_tolerance_above = ColumnProperty(OeOrderHeadersAll.ship_tolerance_above, primary_key=False, visible=True)
    ship_tolerance_below = ColumnProperty(OeOrderHeadersAll.ship_tolerance_below, primary_key=False, visible=True)
    transactional_curr_code = ColumnProperty(OeOrderHeadersAll.transactional_curr_code, primary_key=False, visible=True)
    agreement_id = ColumnProperty(OeOrderHeadersAll.agreement_id, primary_key=False, visible=True)
    tax_point_code = ColumnProperty(OeOrderHeadersAll.tax_point_code, primary_key=False, visible=True)
    cust_po_number = ColumnProperty(OeOrderHeadersAll.cust_po_number, primary_key=False, visible=True)
    shipping_method_code = ColumnProperty(OeOrderHeadersAll.shipping_method_code, primary_key=False, visible=True)
    freight_carrier_code = ColumnProperty(OeOrderHeadersAll.freight_carrier_code, primary_key=False, visible=True)
    fob_point_code = ColumnProperty(OeOrderHeadersAll.fob_point_code, primary_key=False, visible=True)
    freight_terms_code = ColumnProperty(OeOrderHeadersAll.freight_terms_code, primary_key=False, visible=True)
    cancelled_flag = ColumnProperty(OeOrderHeadersAll.cancelled_flag, primary_key=False, visible=True)
    open_flag = ColumnProperty(OeOrderHeadersAll.open_flag, primary_key=False, visible=True)
    booked_flag = ColumnProperty(OeOrderHeadersAll.booked_flag, primary_key=False, visible=True)
    transaction_phase_code = ColumnProperty(OeOrderHeadersAll.transaction_phase_code, primary_key=False, visible=True)
