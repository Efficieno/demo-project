from sqlalchemy import Select
from efficieno.components.view_objects import View, ColumnProperty

from demo_project.data_objects.inv.mtl_system_items_b import MtlSystemItemsB
from demo_project.data_objects.ont.oe_order_lines_all import OeOrderLinesAll
from demo_project.data_objects.apps.org_organization_definitions import OrgOrganizationDefinitions
from demo_project.view_actions.independent_action import IndependentAction
from demo_project.view_actions.inline_order_line_update import InlineOrderLineUpdate


class OrderLinesView(View):
    __query__ = (Select(OeOrderLinesAll, OrgOrganizationDefinitions, MtlSystemItemsB)
                 .join(OeOrderLinesAll.OrgOrganizationDefinitions_organization_id)
                 .join(OeOrderLinesAll.MtlSystemItemsB_organization_id)
                 .join(OeOrderLinesAll.MtlSystemItemsB_inventory_item_id))
    __table_header__ = "Order Headers View"
    __table_description__ = "Order Headers View"

    __inline_action__ = InlineOrderLineUpdate
    __actions__ = [InlineOrderLineUpdate, IndependentAction]

    line_id = ColumnProperty(OeOrderLinesAll.line_id, display_name="Line ID", primary_key=True, visible=False)
    organization_code = ColumnProperty(OrgOrganizationDefinitions.organization_code, display_name="Organization Code", primary_key=False, visible=True)
    segment1 = ColumnProperty(MtlSystemItemsB.segment1, display_name="Ordered Item", primary_key=False, visible=True)
    org_id = ColumnProperty(OeOrderLinesAll.org_id, primary_key=False, visible=True)
    header_id = ColumnProperty(OeOrderLinesAll.header_id, primary_key=False, visible=True)
    line_type_id = ColumnProperty(OeOrderLinesAll.line_type_id, primary_key=False, visible=True)
    line_number = ColumnProperty(OeOrderLinesAll.line_number, primary_key=False, visible=True)
    ordered_item = ColumnProperty(OeOrderLinesAll.ordered_item, primary_key=False, visible=True)
    request_date = ColumnProperty(OeOrderLinesAll.request_date, primary_key=False, visible=True)
    promise_date = ColumnProperty(OeOrderLinesAll.promise_date, primary_key=False, visible=True)
    schedule_ship_date = ColumnProperty(OeOrderLinesAll.schedule_ship_date, primary_key=False, visible=True)
    order_quantity_uom = ColumnProperty(OeOrderLinesAll.order_quantity_uom, primary_key=False, visible=True)
    pricing_quantity = ColumnProperty(OeOrderLinesAll.pricing_quantity, primary_key=False, visible=True)
    pricing_quantity_uom = ColumnProperty(OeOrderLinesAll.pricing_quantity_uom, primary_key=False, visible=True)
    cancelled_quantity = ColumnProperty(OeOrderLinesAll.cancelled_quantity, primary_key=False, visible=True)
    shipped_quantity = ColumnProperty(OeOrderLinesAll.shipped_quantity, primary_key=False, visible=True)
    ordered_quantity = ColumnProperty(OeOrderLinesAll.ordered_quantity, primary_key=False, visible=True)
    fulfilled_quantity = ColumnProperty(OeOrderLinesAll.fulfilled_quantity, primary_key=False, visible=True)
    shipping_quantity = ColumnProperty(OeOrderLinesAll.shipping_quantity, primary_key=False, visible=True)
    shipping_quantity_uom = ColumnProperty(OeOrderLinesAll.shipping_quantity_uom, primary_key=False, visible=True)
    delivery_lead_time = ColumnProperty(OeOrderLinesAll.delivery_lead_time, primary_key=False, visible=True)
    tax_exempt_flag = ColumnProperty(OeOrderLinesAll.tax_exempt_flag, primary_key=False, visible=True)
    tax_exempt_number = ColumnProperty(OeOrderLinesAll.tax_exempt_number, primary_key=False, visible=True)
    tax_exempt_reason_code = ColumnProperty(OeOrderLinesAll.tax_exempt_reason_code, primary_key=False, visible=True)
    project_id = ColumnProperty(OeOrderLinesAll.project_id, primary_key=False, visible=True)
    task_id = ColumnProperty(OeOrderLinesAll.task_id, primary_key=False, visible=True)
    inventory_item_id = ColumnProperty(OeOrderLinesAll.inventory_item_id, primary_key=False, visible=True)
    shipping_method_code = ColumnProperty(OeOrderLinesAll.shipping_method_code, primary_key=False, visible=True)
    freight_carrier_code = ColumnProperty(OeOrderLinesAll.freight_carrier_code, primary_key=False, visible=True)
    freight_terms_code = ColumnProperty(OeOrderLinesAll.freight_terms_code, primary_key=False, visible=True)
    fob_point_code = ColumnProperty(OeOrderLinesAll.fob_point_code, primary_key=False, visible=True)
    tax_point_code = ColumnProperty(OeOrderLinesAll.tax_point_code, primary_key=False, visible=True)
    item_revision = ColumnProperty(OeOrderLinesAll.item_revision, primary_key=False, visible=True)
    unit_selling_price = ColumnProperty(OeOrderLinesAll.unit_selling_price, primary_key=False, visible=True)
    unit_list_price = ColumnProperty(OeOrderLinesAll.unit_list_price, primary_key=False, visible=True)
    actual_shipment_date = ColumnProperty(OeOrderLinesAll.actual_shipment_date, primary_key=False, visible=True)
    cancelled_flag = ColumnProperty(OeOrderLinesAll.cancelled_flag, primary_key=False, visible=True)
    open_flag = ColumnProperty(OeOrderLinesAll.open_flag, primary_key=False, visible=True)
    booked_flag = ColumnProperty(OeOrderLinesAll.booked_flag, primary_key=False, visible=True)
