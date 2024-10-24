from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata

if TYPE_CHECKING:
    from ..ont.oe_order_lines_all import OeOrderLinesAll
    from ..ont.oe_order_headers_all import OeOrderHeadersAll
    from ..wsh.wsh_delivery_assignments import WshDeliveryAssignments


class WshDeliveryDetails(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "wsh_delivery_details"
    __table_args__ = {"schema": "wsh", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 2099.790771484375, "ui_y_pos": 315.3807678222656, "colour": "#F2F3F5"}

    delivery_detail_id: Mapped[str] = mapped_column('delivery_detail_id', Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    source_code: Mapped[str] = mapped_column('source_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_header_id: Mapped[str] = mapped_column('source_header_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_line_id: Mapped[str] = mapped_column('source_line_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_header_type_id: Mapped[str] = mapped_column('source_header_type_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_header_type_name: Mapped[str] = mapped_column('source_header_type_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cust_po_number: Mapped[str] = mapped_column('cust_po_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer_id: Mapped[str] = mapped_column('customer_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sold_to_contact_id: Mapped[str] = mapped_column('sold_to_contact_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    inventory_item_id: Mapped[str] = mapped_column('inventory_item_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    item_description: Mapped[str] = mapped_column('item_description', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_set_id: Mapped[str] = mapped_column('ship_set_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    arrival_set_id: Mapped[str] = mapped_column('arrival_set_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    top_model_line_id: Mapped[str] = mapped_column('top_model_line_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ato_line_id: Mapped[str] = mapped_column('ato_line_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    hold_code: Mapped[str] = mapped_column('hold_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_model_complete_flag: Mapped[str] = mapped_column('ship_model_complete_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    hazard_class_id: Mapped[str] = mapped_column('hazard_class_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    country_of_origin: Mapped[str] = mapped_column('country_of_origin', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    classification: Mapped[str] = mapped_column('classification', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_from_location_id: Mapped[str] = mapped_column('ship_from_location_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    organization_id: Mapped[str] = mapped_column('organization_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_to_location_id: Mapped[str] = mapped_column('ship_to_location_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_to_contact_id: Mapped[str] = mapped_column('ship_to_contact_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    deliver_to_location_id: Mapped[str] = mapped_column('deliver_to_location_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    deliver_to_contact_id: Mapped[str] = mapped_column('deliver_to_contact_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    intmed_ship_to_location_id: Mapped[str] = mapped_column('intmed_ship_to_location_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    intmed_ship_to_contact_id: Mapped[str] = mapped_column('intmed_ship_to_contact_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_tolerance_above: Mapped[str] = mapped_column('ship_tolerance_above', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_tolerance_below: Mapped[str] = mapped_column('ship_tolerance_below', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    src_requested_quantity: Mapped[str] = mapped_column('src_requested_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    src_requested_quantity_uom: Mapped[str] = mapped_column('src_requested_quantity_uom', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cancelled_quantity: Mapped[str] = mapped_column('cancelled_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    requested_quantity: Mapped[str] = mapped_column('requested_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    requested_quantity_uom: Mapped[str] = mapped_column('requested_quantity_uom', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shipped_quantity: Mapped[str] = mapped_column('shipped_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    delivered_quantity: Mapped[str] = mapped_column('delivered_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quality_control_quantity: Mapped[str] = mapped_column('quality_control_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cycle_count_quantity: Mapped[str] = mapped_column('cycle_count_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    move_order_line_id: Mapped[str] = mapped_column('move_order_line_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    subinventory: Mapped[str] = mapped_column('subinventory', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    revision: Mapped[str] = mapped_column('revision', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lot_number: Mapped[str] = mapped_column('lot_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    released_status: Mapped[str] = mapped_column('released_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer_requested_lot_flag: Mapped[str] = mapped_column('customer_requested_lot_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    serial_number: Mapped[str] = mapped_column('serial_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    locator_id: Mapped[str] = mapped_column('locator_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    date_requested: Mapped[str] = mapped_column('date_requested', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    date_scheduled: Mapped[str] = mapped_column('date_scheduled', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    master_container_item_id: Mapped[str] = mapped_column('master_container_item_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    detail_container_item_id: Mapped[str] = mapped_column('detail_container_item_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    load_seq_number: Mapped[str] = mapped_column('load_seq_number', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_method_code: Mapped[str] = mapped_column('ship_method_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    carrier_id: Mapped[str] = mapped_column('carrier_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    freight_terms_code: Mapped[str] = mapped_column('freight_terms_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shipment_priority_code: Mapped[str] = mapped_column('shipment_priority_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    fob_code: Mapped[str] = mapped_column('fob_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer_item_id: Mapped[str] = mapped_column('customer_item_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    dep_plan_required_flag: Mapped[str] = mapped_column('dep_plan_required_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer_prod_seq: Mapped[str] = mapped_column('customer_prod_seq', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer_dock_code: Mapped[str] = mapped_column('customer_dock_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    net_weight: Mapped[str] = mapped_column('net_weight', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    weight_uom_code: Mapped[str] = mapped_column('weight_uom_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    volume: Mapped[str] = mapped_column('volume', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    volume_uom_code: Mapped[str] = mapped_column('volume_uom_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shipping_instructions: Mapped[str] = mapped_column('shipping_instructions', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    packing_instructions: Mapped[str] = mapped_column('packing_instructions', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_id: Mapped[str] = mapped_column('project_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    task_id: Mapped[str] = mapped_column('task_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    org_id: Mapped[str] = mapped_column('org_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    oe_interfaced_flag: Mapped[str] = mapped_column('oe_interfaced_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mvt_stat_status: Mapped[str] = mapped_column('mvt_stat_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tracking_number: Mapped[str] = mapped_column('tracking_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    transaction_temp_id: Mapped[str] = mapped_column('transaction_temp_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute_category: Mapped[str] = mapped_column('tp_attribute_category', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute1: Mapped[str] = mapped_column('tp_attribute1', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute2: Mapped[str] = mapped_column('tp_attribute2', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute3: Mapped[str] = mapped_column('tp_attribute3', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute4: Mapped[str] = mapped_column('tp_attribute4', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute5: Mapped[str] = mapped_column('tp_attribute5', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute6: Mapped[str] = mapped_column('tp_attribute6', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute7: Mapped[str] = mapped_column('tp_attribute7', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute8: Mapped[str] = mapped_column('tp_attribute8', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute9: Mapped[str] = mapped_column('tp_attribute9', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute10: Mapped[str] = mapped_column('tp_attribute10', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute11: Mapped[str] = mapped_column('tp_attribute11', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute12: Mapped[str] = mapped_column('tp_attribute12', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute13: Mapped[str] = mapped_column('tp_attribute13', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute14: Mapped[str] = mapped_column('tp_attribute14', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_attribute15: Mapped[str] = mapped_column('tp_attribute15', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute_category: Mapped[str] = mapped_column('attribute_category', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute1: Mapped[str] = mapped_column('attribute1', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute2: Mapped[str] = mapped_column('attribute2', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute3: Mapped[str] = mapped_column('attribute3', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute4: Mapped[str] = mapped_column('attribute4', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute5: Mapped[str] = mapped_column('attribute5', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute6: Mapped[str] = mapped_column('attribute6', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute7: Mapped[str] = mapped_column('attribute7', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute8: Mapped[str] = mapped_column('attribute8', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute9: Mapped[str] = mapped_column('attribute9', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute10: Mapped[str] = mapped_column('attribute10', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute11: Mapped[str] = mapped_column('attribute11', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute12: Mapped[str] = mapped_column('attribute12', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute13: Mapped[str] = mapped_column('attribute13', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute14: Mapped[str] = mapped_column('attribute14', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute15: Mapped[str] = mapped_column('attribute15', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column('created_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column('last_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column('last_updated_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column('last_update_login', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_application_id: Mapped[str] = mapped_column('program_application_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_id: Mapped[str] = mapped_column('program_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_update_date: Mapped[str] = mapped_column('program_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    request_id: Mapped[str] = mapped_column('request_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    movement_id: Mapped[str] = mapped_column('movement_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    split_from_delivery_detail_id: Mapped[str] = mapped_column('split_from_delivery_detail_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    inv_interfaced_flag: Mapped[str] = mapped_column('inv_interfaced_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    seal_code: Mapped[str] = mapped_column('seal_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    minimum_fill_percent: Mapped[str] = mapped_column('minimum_fill_percent', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    maximum_volume: Mapped[str] = mapped_column('maximum_volume', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    maximum_load_weight: Mapped[str] = mapped_column('maximum_load_weight', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    master_serial_number: Mapped[str] = mapped_column('master_serial_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gross_weight: Mapped[str] = mapped_column('gross_weight', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    fill_percent: Mapped[str] = mapped_column('fill_percent', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    container_name: Mapped[str] = mapped_column('container_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    container_type_code: Mapped[str] = mapped_column('container_type_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    container_flag: Mapped[str] = mapped_column('container_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    preferred_grade: Mapped[str] = mapped_column('preferred_grade', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    src_requested_quantity2: Mapped[str] = mapped_column('src_requested_quantity2', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    src_requested_quantity_uom2: Mapped[str] = mapped_column('src_requested_quantity_uom2', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    requested_quantity2: Mapped[str] = mapped_column('requested_quantity2', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shipped_quantity2: Mapped[str] = mapped_column('shipped_quantity2', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    delivered_quantity2: Mapped[str] = mapped_column('delivered_quantity2', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cancelled_quantity2: Mapped[str] = mapped_column('cancelled_quantity2', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quality_control_quantity2: Mapped[str] = mapped_column('quality_control_quantity2', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cycle_count_quantity2: Mapped[str] = mapped_column('cycle_count_quantity2', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    requested_quantity_uom2: Mapped[str] = mapped_column('requested_quantity_uom2', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sublot_number: Mapped[str] = mapped_column('sublot_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    unit_price: Mapped[str] = mapped_column('unit_price', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    currency_code: Mapped[str] = mapped_column('currency_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    unit_number: Mapped[str] = mapped_column('unit_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    freight_class_cat_id: Mapped[str] = mapped_column('freight_class_cat_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    commodity_code_cat_id: Mapped[str] = mapped_column('commodity_code_cat_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lpn_content_id: Mapped[str] = mapped_column('lpn_content_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lpn_id: Mapped[str] = mapped_column('lpn_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    inspection_flag: Mapped[str] = mapped_column('inspection_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_to_site_use_id: Mapped[str] = mapped_column('ship_to_site_use_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    deliver_to_site_use_id: Mapped[str] = mapped_column('deliver_to_site_use_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    original_subinventory: Mapped[str] = mapped_column('original_subinventory', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    pickable_flag: Mapped[str] = mapped_column('pickable_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_header_number: Mapped[str] = mapped_column('source_header_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_line_number: Mapped[str] = mapped_column('source_line_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    to_serial_number: Mapped[str] = mapped_column('to_serial_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    picked_quantity: Mapped[str] = mapped_column('picked_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    picked_quantity2: Mapped[str] = mapped_column('picked_quantity2', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer_production_line: Mapped[str] = mapped_column('customer_production_line', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer_job: Mapped[str] = mapped_column('customer_job', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cust_model_serial_number: Mapped[str] = mapped_column('cust_model_serial_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    received_quantity: Mapped[str] = mapped_column('received_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    received_quantity2: Mapped[str] = mapped_column('received_quantity2', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_line_set_id: Mapped[str] = mapped_column('source_line_set_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    batch_id: Mapped[str] = mapped_column('batch_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    transaction_id: Mapped[str] = mapped_column('transaction_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    service_level: Mapped[str] = mapped_column('service_level', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mode_of_transport: Mapped[str] = mapped_column('mode_of_transport', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    earliest_pickup_date: Mapped[str] = mapped_column('earliest_pickup_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    latest_pickup_date: Mapped[str] = mapped_column('latest_pickup_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    earliest_dropoff_date: Mapped[str] = mapped_column('earliest_dropoff_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    latest_dropoff_date: Mapped[str] = mapped_column('latest_dropoff_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    request_date_type_code: Mapped[str] = mapped_column('request_date_type_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tp_delivery_detail_id: Mapped[str] = mapped_column('tp_delivery_detail_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_document_type_id: Mapped[str] = mapped_column('source_document_type_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    vendor_id: Mapped[str] = mapped_column('vendor_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_from_site_id: Mapped[str] = mapped_column('ship_from_site_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ignore_for_planning: Mapped[str] = mapped_column('ignore_for_planning', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    line_direction: Mapped[str] = mapped_column('line_direction', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    party_id: Mapped[str] = mapped_column('party_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    routing_req_id: Mapped[str] = mapped_column('routing_req_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shipping_control: Mapped[str] = mapped_column('shipping_control', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_blanket_reference_id: Mapped[str] = mapped_column('source_blanket_reference_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_blanket_reference_num: Mapped[str] = mapped_column('source_blanket_reference_num', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_shipment_line_id: Mapped[str] = mapped_column('po_shipment_line_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_shipment_line_number: Mapped[str] = mapped_column('po_shipment_line_number', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    scheduled_quantity: Mapped[str] = mapped_column('scheduled_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    returned_quantity: Mapped[str] = mapped_column('returned_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    scheduled_quantity2: Mapped[str] = mapped_column('scheduled_quantity2', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    returned_quantity2: Mapped[str] = mapped_column('returned_quantity2', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_line_type_code: Mapped[str] = mapped_column('source_line_type_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    rcv_shipment_line_id: Mapped[str] = mapped_column('rcv_shipment_line_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    supplier_item_number: Mapped[str] = mapped_column('supplier_item_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    filled_volume: Mapped[str] = mapped_column('filled_volume', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    unit_weight: Mapped[str] = mapped_column('unit_weight', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    unit_volume: Mapped[str] = mapped_column('unit_volume', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wv_frozen_flag: Mapped[str] = mapped_column('wv_frozen_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_revision_number: Mapped[str] = mapped_column('po_revision_number', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    release_revision_number: Mapped[str] = mapped_column('release_revision_number', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    replenishment_status: Mapped[str] = mapped_column('replenishment_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    original_lot_number: Mapped[str] = mapped_column('original_lot_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    original_revision: Mapped[str] = mapped_column('original_revision', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    original_locator_id: Mapped[str] = mapped_column('original_locator_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    reference_number: Mapped[str] = mapped_column('reference_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    reference_line_number: Mapped[str] = mapped_column('reference_line_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    reference_line_quantity: Mapped[str] = mapped_column('reference_line_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    reference_line_quantity_uom: Mapped[str] = mapped_column('reference_line_quantity_uom', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    client_id: Mapped[str] = mapped_column('client_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shipment_batch_id: Mapped[str] = mapped_column('shipment_batch_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shipment_line_number: Mapped[str] = mapped_column('shipment_line_number', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    reference_line_id: Mapped[str] = mapped_column('reference_line_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    consignee_flag: Mapped[str] = mapped_column('consignee_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    equipment_id: Mapped[str] = mapped_column('equipment_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mcc_code: Mapped[str] = mapped_column('mcc_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tms_sub_batch_id: Mapped[str] = mapped_column('tms_sub_batch_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tms_sub_batch_line_num: Mapped[str] = mapped_column('tms_sub_batch_line_num', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tms_interface_flag: Mapped[str] = mapped_column('tms_interface_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tms_sshipunit_id: Mapped[str] = mapped_column('tms_sshipunit_id', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    verification_status: Mapped[str] = mapped_column('verification_status', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    reason_id: Mapped[str] = mapped_column('reason_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    group_attribute1: Mapped[str] = mapped_column('group_attribute1', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    group_attribute2: Mapped[str] = mapped_column('group_attribute2', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    group_attribute3: Mapped[str] = mapped_column('group_attribute3', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    group_attribute4: Mapped[str] = mapped_column('group_attribute4', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    group_attribute5: Mapped[str] = mapped_column('group_attribute5', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    group_attribute6: Mapped[str] = mapped_column('group_attribute6', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    group_attribute7: Mapped[str] = mapped_column('group_attribute7', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    group_attribute8: Mapped[str] = mapped_column('group_attribute8', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    group_attribute9: Mapped[str] = mapped_column('group_attribute9', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    group_attribute10: Mapped[str] = mapped_column('group_attribute10', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    group_attribute11: Mapped[str] = mapped_column('group_attribute11', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    group_attribute12: Mapped[str] = mapped_column('group_attribute12', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    group_attribute13: Mapped[str] = mapped_column('group_attribute13', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    group_attribute14: Mapped[str] = mapped_column('group_attribute14', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    group_attribute15: Mapped[str] = mapped_column('group_attribute15', String, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    OeOrderLinesAll_line_id: Mapped["OeOrderLinesAll"] = relationship(back_populates="WshDeliveryDetails_source_line_id", primaryjoin="OeOrderLinesAll.line_id==WshDeliveryDetails.source_line_id", foreign_keys="[OeOrderLinesAll.line_id]", viewonly=True)
        

    

    OeOrderHeadersAll_header_id: Mapped["OeOrderHeadersAll"] = relationship(back_populates="WshDeliveryDetails_source_header_id", primaryjoin="OeOrderHeadersAll.header_id==WshDeliveryDetails.source_header_id", foreign_keys="[OeOrderHeadersAll.header_id]", viewonly=True)
        

    

    WshDeliveryAssignments_delivery_detail_id: Mapped["WshDeliveryAssignments"] = relationship(back_populates="WshDeliveryDetails_delivery_detail_id", primaryjoin="WshDeliveryAssignments.delivery_detail_id==WshDeliveryDetails.delivery_detail_id", foreign_keys="[WshDeliveryAssignments.delivery_detail_id]", viewonly=True)



