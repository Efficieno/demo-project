from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase,  ColumnMetadata

if TYPE_CHECKING:
    from ..ar.ra_customer_trx_lines_all import RaCustomerTrxLinesAll
    from ..ar.ra_customer_trx_lines_all import RaCustomerTrxLinesAll
    from ..ont.oe_order_headers_all import OeOrderHeadersAll
    from ..ont.oe_order_lines_all import OeOrderLinesAll
    from ..ont.oe_order_lines_all import OeOrderLinesAll
    from ..wip.wip_requirement_operations import WipRequirementOperations
    from ..wip.wip_requirement_operations import WipRequirementOperations
    from ..wip.wip_discrete_jobs import WipDiscreteJobs
    from ..wip.wip_discrete_jobs import WipDiscreteJobs
    from ..apps.org_organization_definitions import OrgOrganizationDefinitions
    from ..inv.mtl_onhand_quantities_detail import MtlOnhandQuantitiesDetail
    from ..inv.mtl_onhand_quantities_detail import MtlOnhandQuantitiesDetail
    from ..inv.mtl_reservations import MtlReservations
    from ..inv.mtl_reservations import MtlReservations
    from ..inv.mtl_safety_stocks import MtlSafetyStocks
    from ..inv.mtl_safety_stocks import MtlSafetyStocks
    from ..inv.mtl_item_revisions_b import MtlItemRevisionsB
    from ..inv.mtl_item_revisions_b import MtlItemRevisionsB


class MtlSystemItemsB(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "mtl_system_items_b"
    __table_args__ = {"schema": "inv", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 894.5002365112305, "ui_y_pos": 742.5576133728027, "colour": "#F2F3F5"}

    inventory_item_id: Mapped[str] = mapped_column('inventory_item_id', Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    organization_id: Mapped[str] = mapped_column('organization_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column('last_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column('last_updated_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column('created_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column('last_update_login', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    summary_flag: Mapped[str] = mapped_column('summary_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    enabled_flag: Mapped[str] = mapped_column('enabled_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    start_date_active: Mapped[str] = mapped_column('start_date_active', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    end_date_active: Mapped[str] = mapped_column('end_date_active', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    description: Mapped[str] = mapped_column('description', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    buyer_id: Mapped[str] = mapped_column('buyer_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    accounting_rule_id: Mapped[str] = mapped_column('accounting_rule_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    invoicing_rule_id: Mapped[str] = mapped_column('invoicing_rule_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment1: Mapped[str] = mapped_column('segment1', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment2: Mapped[str] = mapped_column('segment2', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment3: Mapped[str] = mapped_column('segment3', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment4: Mapped[str] = mapped_column('segment4', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment5: Mapped[str] = mapped_column('segment5', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment6: Mapped[str] = mapped_column('segment6', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment7: Mapped[str] = mapped_column('segment7', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment8: Mapped[str] = mapped_column('segment8', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment9: Mapped[str] = mapped_column('segment9', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment10: Mapped[str] = mapped_column('segment10', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment11: Mapped[str] = mapped_column('segment11', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment12: Mapped[str] = mapped_column('segment12', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment13: Mapped[str] = mapped_column('segment13', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment14: Mapped[str] = mapped_column('segment14', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment15: Mapped[str] = mapped_column('segment15', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment16: Mapped[str] = mapped_column('segment16', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment17: Mapped[str] = mapped_column('segment17', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment18: Mapped[str] = mapped_column('segment18', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment19: Mapped[str] = mapped_column('segment19', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    segment20: Mapped[str] = mapped_column('segment20', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
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
    purchasing_item_flag: Mapped[str] = mapped_column('purchasing_item_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shippable_item_flag: Mapped[str] = mapped_column('shippable_item_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer_order_flag: Mapped[str] = mapped_column('customer_order_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    internal_order_flag: Mapped[str] = mapped_column('internal_order_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    service_item_flag: Mapped[str] = mapped_column('service_item_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    inventory_item_flag: Mapped[str] = mapped_column('inventory_item_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    eng_item_flag: Mapped[str] = mapped_column('eng_item_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    inventory_asset_flag: Mapped[str] = mapped_column('inventory_asset_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    purchasing_enabled_flag: Mapped[str] = mapped_column('purchasing_enabled_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer_order_enabled_flag: Mapped[str] = mapped_column('customer_order_enabled_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    internal_order_enabled_flag: Mapped[str] = mapped_column('internal_order_enabled_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    so_transactions_flag: Mapped[str] = mapped_column('so_transactions_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mtl_transactions_enabled_flag: Mapped[str] = mapped_column('mtl_transactions_enabled_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    stock_enabled_flag: Mapped[str] = mapped_column('stock_enabled_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bom_enabled_flag: Mapped[str] = mapped_column('bom_enabled_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    build_in_wip_flag: Mapped[str] = mapped_column('build_in_wip_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    revision_qty_control_code: Mapped[str] = mapped_column('revision_qty_control_code', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    item_catalog_group_id: Mapped[str] = mapped_column('item_catalog_group_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    catalog_status_flag: Mapped[str] = mapped_column('catalog_status_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    returnable_flag: Mapped[str] = mapped_column('returnable_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    default_shipping_org: Mapped[str] = mapped_column('default_shipping_org', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    collateral_flag: Mapped[str] = mapped_column('collateral_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    taxable_flag: Mapped[str] = mapped_column('taxable_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    qty_rcv_exception_code: Mapped[str] = mapped_column('qty_rcv_exception_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    allow_item_desc_update_flag: Mapped[str] = mapped_column('allow_item_desc_update_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    inspection_required_flag: Mapped[str] = mapped_column('inspection_required_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    receipt_required_flag: Mapped[str] = mapped_column('receipt_required_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    market_price: Mapped[str] = mapped_column('market_price', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    hazard_class_id: Mapped[str] = mapped_column('hazard_class_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    rfq_required_flag: Mapped[str] = mapped_column('rfq_required_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    qty_rcv_tolerance: Mapped[str] = mapped_column('qty_rcv_tolerance', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    list_price_per_unit: Mapped[str] = mapped_column('list_price_per_unit', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    un_number_id: Mapped[str] = mapped_column('un_number_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    price_tolerance_percent: Mapped[str] = mapped_column('price_tolerance_percent', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    asset_category_id: Mapped[str] = mapped_column('asset_category_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    rounding_factor: Mapped[str] = mapped_column('rounding_factor', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    unit_of_issue: Mapped[str] = mapped_column('unit_of_issue', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    enforce_ship_to_location_code: Mapped[str] = mapped_column('enforce_ship_to_location_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    allow_substitute_receipts_flag: Mapped[str] = mapped_column('allow_substitute_receipts_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    allow_unordered_receipts_flag: Mapped[str] = mapped_column('allow_unordered_receipts_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    allow_express_delivery_flag: Mapped[str] = mapped_column('allow_express_delivery_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    days_early_receipt_allowed: Mapped[str] = mapped_column('days_early_receipt_allowed', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    days_late_receipt_allowed: Mapped[str] = mapped_column('days_late_receipt_allowed', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    receipt_days_exception_code: Mapped[str] = mapped_column('receipt_days_exception_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    receiving_routing_id: Mapped[str] = mapped_column('receiving_routing_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    invoice_close_tolerance: Mapped[str] = mapped_column('invoice_close_tolerance', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    receive_close_tolerance: Mapped[str] = mapped_column('receive_close_tolerance', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    auto_lot_alpha_prefix: Mapped[str] = mapped_column('auto_lot_alpha_prefix', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    start_auto_lot_number: Mapped[str] = mapped_column('start_auto_lot_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lot_control_code: Mapped[str] = mapped_column('lot_control_code', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shelf_life_code: Mapped[str] = mapped_column('shelf_life_code', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shelf_life_days: Mapped[str] = mapped_column('shelf_life_days', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    serial_number_control_code: Mapped[str] = mapped_column('serial_number_control_code', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    start_auto_serial_number: Mapped[str] = mapped_column('start_auto_serial_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    auto_serial_alpha_prefix: Mapped[str] = mapped_column('auto_serial_alpha_prefix', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_type: Mapped[str] = mapped_column('source_type', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_organization_id: Mapped[str] = mapped_column('source_organization_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_subinventory: Mapped[str] = mapped_column('source_subinventory', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    expense_account: Mapped[str] = mapped_column('expense_account', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    encumbrance_account: Mapped[str] = mapped_column('encumbrance_account', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    restrict_subinventories_code: Mapped[str] = mapped_column('restrict_subinventories_code', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    unit_weight: Mapped[str] = mapped_column('unit_weight', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    weight_uom_code: Mapped[str] = mapped_column('weight_uom_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    volume_uom_code: Mapped[str] = mapped_column('volume_uom_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    unit_volume: Mapped[str] = mapped_column('unit_volume', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    restrict_locators_code: Mapped[str] = mapped_column('restrict_locators_code', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    location_control_code: Mapped[str] = mapped_column('location_control_code', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    shrinkage_rate: Mapped[str] = mapped_column('shrinkage_rate', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    acceptable_early_days: Mapped[str] = mapped_column('acceptable_early_days', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    planning_time_fence_code: Mapped[str] = mapped_column('planning_time_fence_code', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    demand_time_fence_code: Mapped[str] = mapped_column('demand_time_fence_code', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lead_time_lot_size: Mapped[str] = mapped_column('lead_time_lot_size', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    std_lot_size: Mapped[str] = mapped_column('std_lot_size', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cum_manufacturing_lead_time: Mapped[str] = mapped_column('cum_manufacturing_lead_time', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    overrun_percentage: Mapped[str] = mapped_column('overrun_percentage', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mrp_calculate_atp_flag: Mapped[str] = mapped_column('mrp_calculate_atp_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    acceptable_rate_increase: Mapped[str] = mapped_column('acceptable_rate_increase', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    acceptable_rate_decrease: Mapped[str] = mapped_column('acceptable_rate_decrease', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cumulative_total_lead_time: Mapped[str] = mapped_column('cumulative_total_lead_time', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    planning_time_fence_days: Mapped[str] = mapped_column('planning_time_fence_days', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    demand_time_fence_days: Mapped[str] = mapped_column('demand_time_fence_days', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    end_assembly_pegging_flag: Mapped[str] = mapped_column('end_assembly_pegging_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    repetitive_planning_flag: Mapped[str] = mapped_column('repetitive_planning_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    planning_exception_set: Mapped[str] = mapped_column('planning_exception_set', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bom_item_type: Mapped[str] = mapped_column('bom_item_type', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    pick_components_flag: Mapped[str] = mapped_column('pick_components_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    replenish_to_order_flag: Mapped[str] = mapped_column('replenish_to_order_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    base_item_id: Mapped[str] = mapped_column('base_item_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    atp_components_flag: Mapped[str] = mapped_column('atp_components_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    atp_flag: Mapped[str] = mapped_column('atp_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    fixed_lead_time: Mapped[str] = mapped_column('fixed_lead_time', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    variable_lead_time: Mapped[str] = mapped_column('variable_lead_time', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_supply_locator_id: Mapped[str] = mapped_column('wip_supply_locator_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_supply_type: Mapped[str] = mapped_column('wip_supply_type', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_supply_subinventory: Mapped[str] = mapped_column('wip_supply_subinventory', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    primary_uom_code: Mapped[str] = mapped_column('primary_uom_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    primary_unit_of_measure: Mapped[str] = mapped_column('primary_unit_of_measure', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    allowed_units_lookup_code: Mapped[str] = mapped_column('allowed_units_lookup_code', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cost_of_sales_account: Mapped[str] = mapped_column('cost_of_sales_account', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sales_account: Mapped[str] = mapped_column('sales_account', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    default_include_in_rollup_flag: Mapped[str] = mapped_column('default_include_in_rollup_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    inventory_item_status_code: Mapped[str] = mapped_column('inventory_item_status_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    inventory_planning_code: Mapped[str] = mapped_column('inventory_planning_code', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    planner_code: Mapped[str] = mapped_column('planner_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    planning_make_buy_code: Mapped[str] = mapped_column('planning_make_buy_code', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    fixed_lot_multiplier: Mapped[str] = mapped_column('fixed_lot_multiplier', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    rounding_control_type: Mapped[str] = mapped_column('rounding_control_type', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    carrying_cost: Mapped[str] = mapped_column('carrying_cost', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    postprocessing_lead_time: Mapped[str] = mapped_column('postprocessing_lead_time', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    preprocessing_lead_time: Mapped[str] = mapped_column('preprocessing_lead_time', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    full_lead_time: Mapped[str] = mapped_column('full_lead_time', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_cost: Mapped[str] = mapped_column('order_cost', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mrp_safety_stock_percent: Mapped[str] = mapped_column('mrp_safety_stock_percent', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mrp_safety_stock_code: Mapped[str] = mapped_column('mrp_safety_stock_code', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    min_minmax_quantity: Mapped[str] = mapped_column('min_minmax_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    max_minmax_quantity: Mapped[str] = mapped_column('max_minmax_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    minimum_order_quantity: Mapped[str] = mapped_column('minimum_order_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    fixed_order_quantity: Mapped[str] = mapped_column('fixed_order_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    fixed_days_supply: Mapped[str] = mapped_column('fixed_days_supply', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    maximum_order_quantity: Mapped[str] = mapped_column('maximum_order_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    atp_rule_id: Mapped[str] = mapped_column('atp_rule_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    picking_rule_id: Mapped[str] = mapped_column('picking_rule_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    reservable_type: Mapped[str] = mapped_column('reservable_type', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    positive_measurement_error: Mapped[str] = mapped_column('positive_measurement_error', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    negative_measurement_error: Mapped[str] = mapped_column('negative_measurement_error', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    engineering_ecn_code: Mapped[str] = mapped_column('engineering_ecn_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    engineering_item_id: Mapped[str] = mapped_column('engineering_item_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    engineering_date: Mapped[str] = mapped_column('engineering_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    service_starting_delay: Mapped[str] = mapped_column('service_starting_delay', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    vendor_warranty_flag: Mapped[str] = mapped_column('vendor_warranty_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    serviceable_component_flag: Mapped[str] = mapped_column('serviceable_component_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    serviceable_product_flag: Mapped[str] = mapped_column('serviceable_product_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    base_warranty_service_id: Mapped[str] = mapped_column('base_warranty_service_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    payment_terms_id: Mapped[str] = mapped_column('payment_terms_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    preventive_maintenance_flag: Mapped[str] = mapped_column('preventive_maintenance_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    primary_specialist_id: Mapped[str] = mapped_column('primary_specialist_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    secondary_specialist_id: Mapped[str] = mapped_column('secondary_specialist_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    serviceable_item_class_id: Mapped[str] = mapped_column('serviceable_item_class_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    time_billable_flag: Mapped[str] = mapped_column('time_billable_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    material_billable_flag: Mapped[str] = mapped_column('material_billable_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    expense_billable_flag: Mapped[str] = mapped_column('expense_billable_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    prorate_service_flag: Mapped[str] = mapped_column('prorate_service_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    coverage_schedule_id: Mapped[str] = mapped_column('coverage_schedule_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    service_duration_period_code: Mapped[str] = mapped_column('service_duration_period_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    service_duration: Mapped[str] = mapped_column('service_duration', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    warranty_vendor_id: Mapped[str] = mapped_column('warranty_vendor_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    max_warranty_amount: Mapped[str] = mapped_column('max_warranty_amount', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    response_time_period_code: Mapped[str] = mapped_column('response_time_period_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    response_time_value: Mapped[str] = mapped_column('response_time_value', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    new_revision_code: Mapped[str] = mapped_column('new_revision_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    invoiceable_item_flag: Mapped[str] = mapped_column('invoiceable_item_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tax_code: Mapped[str] = mapped_column('tax_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    invoice_enabled_flag: Mapped[str] = mapped_column('invoice_enabled_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    must_use_approved_vendor_flag: Mapped[str] = mapped_column('must_use_approved_vendor_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    request_id: Mapped[str] = mapped_column('request_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_application_id: Mapped[str] = mapped_column('program_application_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_id: Mapped[str] = mapped_column('program_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_update_date: Mapped[str] = mapped_column('program_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    outside_operation_flag: Mapped[str] = mapped_column('outside_operation_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    outside_operation_uom_type: Mapped[str] = mapped_column('outside_operation_uom_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    safety_stock_bucket_days: Mapped[str] = mapped_column('safety_stock_bucket_days', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    auto_reduce_mps: Mapped[str] = mapped_column('auto_reduce_mps', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    costing_enabled_flag: Mapped[str] = mapped_column('costing_enabled_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    auto_created_config_flag: Mapped[str] = mapped_column('auto_created_config_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cycle_count_enabled_flag: Mapped[str] = mapped_column('cycle_count_enabled_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    item_type: Mapped[str] = mapped_column('item_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    model_config_clause_name: Mapped[str] = mapped_column('model_config_clause_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_model_complete_flag: Mapped[str] = mapped_column('ship_model_complete_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mrp_planning_code: Mapped[str] = mapped_column('mrp_planning_code', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    return_inspection_requirement: Mapped[str] = mapped_column('return_inspection_requirement', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ato_forecast_control: Mapped[str] = mapped_column('ato_forecast_control', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    release_time_fence_code: Mapped[str] = mapped_column('release_time_fence_code', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    release_time_fence_days: Mapped[str] = mapped_column('release_time_fence_days', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    container_item_flag: Mapped[str] = mapped_column('container_item_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    vehicle_item_flag: Mapped[str] = mapped_column('vehicle_item_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    maximum_load_weight: Mapped[str] = mapped_column('maximum_load_weight', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    minimum_fill_percent: Mapped[str] = mapped_column('minimum_fill_percent', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    container_type_code: Mapped[str] = mapped_column('container_type_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    internal_volume: Mapped[str] = mapped_column('internal_volume', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wh_update_date: Mapped[str] = mapped_column('wh_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    product_family_item_id: Mapped[str] = mapped_column('product_family_item_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute_category: Mapped[str] = mapped_column('global_attribute_category', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute1: Mapped[str] = mapped_column('global_attribute1', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute2: Mapped[str] = mapped_column('global_attribute2', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute3: Mapped[str] = mapped_column('global_attribute3', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute4: Mapped[str] = mapped_column('global_attribute4', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute5: Mapped[str] = mapped_column('global_attribute5', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute6: Mapped[str] = mapped_column('global_attribute6', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute7: Mapped[str] = mapped_column('global_attribute7', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute8: Mapped[str] = mapped_column('global_attribute8', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute9: Mapped[str] = mapped_column('global_attribute9', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute10: Mapped[str] = mapped_column('global_attribute10', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    purchasing_tax_code: Mapped[str] = mapped_column('purchasing_tax_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    overcompletion_tolerance_type: Mapped[str] = mapped_column('overcompletion_tolerance_type', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    overcompletion_tolerance_value: Mapped[str] = mapped_column('overcompletion_tolerance_value', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    effectivity_control: Mapped[str] = mapped_column('effectivity_control', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    check_shortages_flag: Mapped[str] = mapped_column('check_shortages_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    over_shipment_tolerance: Mapped[str] = mapped_column('over_shipment_tolerance', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    under_shipment_tolerance: Mapped[str] = mapped_column('under_shipment_tolerance', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    over_return_tolerance: Mapped[str] = mapped_column('over_return_tolerance', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    under_return_tolerance: Mapped[str] = mapped_column('under_return_tolerance', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    equipment_type: Mapped[str] = mapped_column('equipment_type', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    recovered_part_disp_code: Mapped[str] = mapped_column('recovered_part_disp_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    defect_tracking_on_flag: Mapped[str] = mapped_column('defect_tracking_on_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    usage_item_flag: Mapped[str] = mapped_column('usage_item_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    event_flag: Mapped[str] = mapped_column('event_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    electronic_flag: Mapped[str] = mapped_column('electronic_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    downloadable_flag: Mapped[str] = mapped_column('downloadable_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    vol_discount_exempt_flag: Mapped[str] = mapped_column('vol_discount_exempt_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    coupon_exempt_flag: Mapped[str] = mapped_column('coupon_exempt_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    comms_nl_trackable_flag: Mapped[str] = mapped_column('comms_nl_trackable_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    asset_creation_code: Mapped[str] = mapped_column('asset_creation_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    comms_activation_reqd_flag: Mapped[str] = mapped_column('comms_activation_reqd_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    orderable_on_web_flag: Mapped[str] = mapped_column('orderable_on_web_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    back_orderable_flag: Mapped[str] = mapped_column('back_orderable_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    web_status: Mapped[str] = mapped_column('web_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    indivisible_flag: Mapped[str] = mapped_column('indivisible_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    dimension_uom_code: Mapped[str] = mapped_column('dimension_uom_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    unit_length: Mapped[str] = mapped_column('unit_length', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    unit_width: Mapped[str] = mapped_column('unit_width', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    unit_height: Mapped[str] = mapped_column('unit_height', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bulk_picked_flag: Mapped[str] = mapped_column('bulk_picked_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lot_status_enabled: Mapped[str] = mapped_column('lot_status_enabled', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    default_lot_status_id: Mapped[str] = mapped_column('default_lot_status_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    serial_status_enabled: Mapped[str] = mapped_column('serial_status_enabled', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    default_serial_status_id: Mapped[str] = mapped_column('default_serial_status_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lot_split_enabled: Mapped[str] = mapped_column('lot_split_enabled', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lot_merge_enabled: Mapped[str] = mapped_column('lot_merge_enabled', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    inventory_carry_penalty: Mapped[str] = mapped_column('inventory_carry_penalty', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    operation_slack_penalty: Mapped[str] = mapped_column('operation_slack_penalty', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    financing_allowed_flag: Mapped[str] = mapped_column('financing_allowed_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    eam_item_type: Mapped[str] = mapped_column('eam_item_type', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    eam_activity_type_code: Mapped[str] = mapped_column('eam_activity_type_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    eam_activity_cause_code: Mapped[str] = mapped_column('eam_activity_cause_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    eam_act_notification_flag: Mapped[str] = mapped_column('eam_act_notification_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    eam_act_shutdown_status: Mapped[str] = mapped_column('eam_act_shutdown_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    dual_uom_control: Mapped[str] = mapped_column('dual_uom_control', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    secondary_uom_code: Mapped[str] = mapped_column('secondary_uom_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    dual_uom_deviation_high: Mapped[str] = mapped_column('dual_uom_deviation_high', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    dual_uom_deviation_low: Mapped[str] = mapped_column('dual_uom_deviation_low', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    contract_item_type_code: Mapped[str] = mapped_column('contract_item_type_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    subscription_depend_flag: Mapped[str] = mapped_column('subscription_depend_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    serv_req_enabled_code: Mapped[str] = mapped_column('serv_req_enabled_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    serv_billing_enabled_flag: Mapped[str] = mapped_column('serv_billing_enabled_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    serv_importance_level: Mapped[str] = mapped_column('serv_importance_level', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    planned_inv_point_flag: Mapped[str] = mapped_column('planned_inv_point_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lot_translate_enabled: Mapped[str] = mapped_column('lot_translate_enabled', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    default_so_source_type: Mapped[str] = mapped_column('default_so_source_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    create_supply_flag: Mapped[str] = mapped_column('create_supply_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    substitution_window_code: Mapped[str] = mapped_column('substitution_window_code', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    substitution_window_days: Mapped[str] = mapped_column('substitution_window_days', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ib_item_instance_class: Mapped[str] = mapped_column('ib_item_instance_class', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    config_model_type: Mapped[str] = mapped_column('config_model_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lot_substitution_enabled: Mapped[str] = mapped_column('lot_substitution_enabled', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    minimum_license_quantity: Mapped[str] = mapped_column('minimum_license_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    eam_activity_source_code: Mapped[str] = mapped_column('eam_activity_source_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lifecycle_id: Mapped[str] = mapped_column('lifecycle_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    current_phase_id: Mapped[str] = mapped_column('current_phase_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    object_version_number: Mapped[str] = mapped_column('object_version_number', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tracking_quantity_ind: Mapped[str] = mapped_column('tracking_quantity_ind', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ont_pricing_qty_source: Mapped[str] = mapped_column('ont_pricing_qty_source', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    secondary_default_ind: Mapped[str] = mapped_column('secondary_default_ind', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    option_specific_sourced: Mapped[str] = mapped_column('option_specific_sourced', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    approval_status: Mapped[str] = mapped_column('approval_status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    vmi_minimum_units: Mapped[str] = mapped_column('vmi_minimum_units', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    vmi_minimum_days: Mapped[str] = mapped_column('vmi_minimum_days', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    vmi_maximum_units: Mapped[str] = mapped_column('vmi_maximum_units', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    vmi_maximum_days: Mapped[str] = mapped_column('vmi_maximum_days', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    vmi_fixed_order_quantity: Mapped[str] = mapped_column('vmi_fixed_order_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    so_authorization_flag: Mapped[str] = mapped_column('so_authorization_flag', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    consigned_flag: Mapped[str] = mapped_column('consigned_flag', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    asn_autoexpire_flag: Mapped[str] = mapped_column('asn_autoexpire_flag', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    vmi_forecast_type: Mapped[str] = mapped_column('vmi_forecast_type', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    forecast_horizon: Mapped[str] = mapped_column('forecast_horizon', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    exclude_from_budget_flag: Mapped[str] = mapped_column('exclude_from_budget_flag', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    days_tgt_inv_supply: Mapped[str] = mapped_column('days_tgt_inv_supply', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    days_tgt_inv_window: Mapped[str] = mapped_column('days_tgt_inv_window', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    days_max_inv_supply: Mapped[str] = mapped_column('days_max_inv_supply', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    days_max_inv_window: Mapped[str] = mapped_column('days_max_inv_window', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    drp_planned_flag: Mapped[str] = mapped_column('drp_planned_flag', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    critical_component_flag: Mapped[str] = mapped_column('critical_component_flag', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    continous_transfer: Mapped[str] = mapped_column('continous_transfer', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    convergence: Mapped[str] = mapped_column('convergence', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    divergence: Mapped[str] = mapped_column('divergence', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    config_orgs: Mapped[str] = mapped_column('config_orgs', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    config_match: Mapped[str] = mapped_column('config_match', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute16: Mapped[str] = mapped_column('attribute16', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute17: Mapped[str] = mapped_column('attribute17', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute18: Mapped[str] = mapped_column('attribute18', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute19: Mapped[str] = mapped_column('attribute19', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute20: Mapped[str] = mapped_column('attribute20', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute21: Mapped[str] = mapped_column('attribute21', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute22: Mapped[str] = mapped_column('attribute22', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute23: Mapped[str] = mapped_column('attribute23', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute24: Mapped[str] = mapped_column('attribute24', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute25: Mapped[str] = mapped_column('attribute25', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute26: Mapped[str] = mapped_column('attribute26', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute27: Mapped[str] = mapped_column('attribute27', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute28: Mapped[str] = mapped_column('attribute28', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute29: Mapped[str] = mapped_column('attribute29', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute30: Mapped[str] = mapped_column('attribute30', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cas_number: Mapped[str] = mapped_column('cas_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    child_lot_flag: Mapped[str] = mapped_column('child_lot_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    child_lot_prefix: Mapped[str] = mapped_column('child_lot_prefix', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    child_lot_starting_number: Mapped[str] = mapped_column('child_lot_starting_number', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    child_lot_validation_flag: Mapped[str] = mapped_column('child_lot_validation_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    copy_lot_attribute_flag: Mapped[str] = mapped_column('copy_lot_attribute_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    default_grade: Mapped[str] = mapped_column('default_grade', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    expiration_action_code: Mapped[str] = mapped_column('expiration_action_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    expiration_action_interval: Mapped[str] = mapped_column('expiration_action_interval', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    grade_control_flag: Mapped[str] = mapped_column('grade_control_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    hazardous_material_flag: Mapped[str] = mapped_column('hazardous_material_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    hold_days: Mapped[str] = mapped_column('hold_days', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lot_divisible_flag: Mapped[str] = mapped_column('lot_divisible_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    maturity_days: Mapped[str] = mapped_column('maturity_days', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    parent_child_generation_flag: Mapped[str] = mapped_column('parent_child_generation_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    process_costing_enabled_flag: Mapped[str] = mapped_column('process_costing_enabled_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    process_execution_enabled_flag: Mapped[str] = mapped_column('process_execution_enabled_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    process_quality_enabled_flag: Mapped[str] = mapped_column('process_quality_enabled_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    process_supply_locator_id: Mapped[str] = mapped_column('process_supply_locator_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    process_supply_subinventory: Mapped[str] = mapped_column('process_supply_subinventory', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    process_yield_locator_id: Mapped[str] = mapped_column('process_yield_locator_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    process_yield_subinventory: Mapped[str] = mapped_column('process_yield_subinventory', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    recipe_enabled_flag: Mapped[str] = mapped_column('recipe_enabled_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    retest_interval: Mapped[str] = mapped_column('retest_interval', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    charge_periodicity_code: Mapped[str] = mapped_column('charge_periodicity_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    repair_leadtime: Mapped[str] = mapped_column('repair_leadtime', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    repair_yield: Mapped[str] = mapped_column('repair_yield', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    preposition_point: Mapped[str] = mapped_column('preposition_point', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    repair_program: Mapped[str] = mapped_column('repair_program', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    subcontracting_component: Mapped[str] = mapped_column('subcontracting_component', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    outsourced_assembly: Mapped[str] = mapped_column('outsourced_assembly', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ego_master_items_dff_ctx: Mapped[str] = mapped_column('ego_master_items_dff_ctx', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gdsn_outbound_enabled_flag: Mapped[str] = mapped_column('gdsn_outbound_enabled_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    trade_item_descriptor: Mapped[str] = mapped_column('trade_item_descriptor', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    style_item_id: Mapped[str] = mapped_column('style_item_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    style_item_flag: Mapped[str] = mapped_column('style_item_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_submitted_nir_id: Mapped[str] = mapped_column('last_submitted_nir_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    default_material_status_id: Mapped[str] = mapped_column('default_material_status_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute11: Mapped[str] = mapped_column('global_attribute11', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute12: Mapped[str] = mapped_column('global_attribute12', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute13: Mapped[str] = mapped_column('global_attribute13', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute14: Mapped[str] = mapped_column('global_attribute14', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute15: Mapped[str] = mapped_column('global_attribute15', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute16: Mapped[str] = mapped_column('global_attribute16', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute17: Mapped[str] = mapped_column('global_attribute17', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute18: Mapped[str] = mapped_column('global_attribute18', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute19: Mapped[str] = mapped_column('global_attribute19', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute20: Mapped[str] = mapped_column('global_attribute20', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    serial_tagging_flag: Mapped[str] = mapped_column('serial_tagging_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ib_item_tracking_level: Mapped[str] = mapped_column('ib_item_tracking_level', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mcc_classification_type: Mapped[str] = mapped_column('mcc_classification_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mcc_control_code: Mapped[str] = mapped_column('mcc_control_code', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mcc_tracking_code: Mapped[str] = mapped_column('mcc_tracking_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute21: Mapped[str] = mapped_column('global_attribute21', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute22: Mapped[str] = mapped_column('global_attribute22', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute23: Mapped[str] = mapped_column('global_attribute23', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute24: Mapped[str] = mapped_column('global_attribute24', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute25: Mapped[str] = mapped_column('global_attribute25', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute26: Mapped[str] = mapped_column('global_attribute26', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute27: Mapped[str] = mapped_column('global_attribute27', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute28: Mapped[str] = mapped_column('global_attribute28', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute29: Mapped[str] = mapped_column('global_attribute29', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute30: Mapped[str] = mapped_column('global_attribute30', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute31: Mapped[str] = mapped_column('global_attribute31', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute32: Mapped[str] = mapped_column('global_attribute32', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute33: Mapped[str] = mapped_column('global_attribute33', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute34: Mapped[str] = mapped_column('global_attribute34', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute35: Mapped[str] = mapped_column('global_attribute35', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute36: Mapped[str] = mapped_column('global_attribute36', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute37: Mapped[str] = mapped_column('global_attribute37', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute38: Mapped[str] = mapped_column('global_attribute38', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute39: Mapped[str] = mapped_column('global_attribute39', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute40: Mapped[str] = mapped_column('global_attribute40', String, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    RaCustomerTrxLinesAll_inventory_item_id: Mapped["RaCustomerTrxLinesAll"] = relationship(back_populates="MtlSystemItemsB_inventory_item_id", primaryjoin="RaCustomerTrxLinesAll.inventory_item_id==MtlSystemItemsB.inventory_item_id", foreign_keys="[RaCustomerTrxLinesAll.inventory_item_id]", viewonly=True)
        

    

    RaCustomerTrxLinesAll_warehouse_id: Mapped["RaCustomerTrxLinesAll"] = relationship(back_populates="MtlSystemItemsB_organization_id", primaryjoin="RaCustomerTrxLinesAll.warehouse_id==MtlSystemItemsB.organization_id", foreign_keys="[RaCustomerTrxLinesAll.warehouse_id]", viewonly=True)
        

    

    OeOrderHeadersAll_ship_from_org_id: Mapped["OeOrderHeadersAll"] = relationship(back_populates="MtlSystemItemsB_organization_id", primaryjoin="OeOrderHeadersAll.ship_from_org_id==MtlSystemItemsB.organization_id", foreign_keys="[MtlSystemItemsB.organization_id]", viewonly=True)
        

    

    OeOrderLinesAll_ship_from_org_id: Mapped["OeOrderLinesAll"] = relationship(back_populates="MtlSystemItemsB_organization_id", primaryjoin="OeOrderLinesAll.ship_from_org_id==MtlSystemItemsB.organization_id", foreign_keys="[MtlSystemItemsB.organization_id]", viewonly=True)
        

    

    OeOrderLinesAll_inventory_item_id: Mapped["OeOrderLinesAll"] = relationship(back_populates="MtlSystemItemsB_inventory_item_id", primaryjoin="OeOrderLinesAll.inventory_item_id==MtlSystemItemsB.inventory_item_id", foreign_keys="[MtlSystemItemsB.inventory_item_id]", viewonly=True)
        

    

    WipRequirementOperations_organization_id: Mapped["WipRequirementOperations"] = relationship(back_populates="MtlSystemItemsB_organization_id", primaryjoin="WipRequirementOperations.organization_id==MtlSystemItemsB.organization_id", foreign_keys="[MtlSystemItemsB.organization_id]", viewonly=True)
        

    

    WipRequirementOperations_inventory_item_id: Mapped["WipRequirementOperations"] = relationship(back_populates="MtlSystemItemsB_inventory_item_id", primaryjoin="WipRequirementOperations.inventory_item_id==MtlSystemItemsB.inventory_item_id", foreign_keys="[MtlSystemItemsB.inventory_item_id]", viewonly=True)
        

    

    WipDiscreteJobs_organization_id: Mapped["WipDiscreteJobs"] = relationship(back_populates="MtlSystemItemsB_organization_id", primaryjoin="WipDiscreteJobs.organization_id==MtlSystemItemsB.organization_id", foreign_keys="[MtlSystemItemsB.organization_id]", viewonly=True)
        

    

    WipDiscreteJobs_primary_item_id: Mapped["WipDiscreteJobs"] = relationship(back_populates="MtlSystemItemsB_inventory_item_id", primaryjoin="WipDiscreteJobs.primary_item_id==MtlSystemItemsB.inventory_item_id", foreign_keys="[MtlSystemItemsB.inventory_item_id]", viewonly=True)
        

    

    OrgOrganizationDefinitions_organization_id: Mapped["OrgOrganizationDefinitions"] = relationship(back_populates="MtlSystemItemsB_organization_id", primaryjoin="OrgOrganizationDefinitions.organization_id==MtlSystemItemsB.organization_id", foreign_keys="[OrgOrganizationDefinitions.organization_id]", viewonly=True)
        

    

    MtlOnhandQuantitiesDetail_organization_id: Mapped["MtlOnhandQuantitiesDetail"] = relationship(back_populates="MtlSystemItemsB_organization_id", primaryjoin="MtlOnhandQuantitiesDetail.organization_id==MtlSystemItemsB.organization_id", foreign_keys="[MtlOnhandQuantitiesDetail.organization_id]", viewonly=True)
        

    

    MtlOnhandQuantitiesDetail_inventory_item_id: Mapped["MtlOnhandQuantitiesDetail"] = relationship(back_populates="MtlSystemItemsB_inventory_item_id", primaryjoin="MtlOnhandQuantitiesDetail.inventory_item_id==MtlSystemItemsB.inventory_item_id", foreign_keys="[MtlOnhandQuantitiesDetail.inventory_item_id]", viewonly=True)
        

    

    MtlReservations_organization_id: Mapped["MtlReservations"] = relationship(back_populates="MtlSystemItemsB_organization_id", primaryjoin="MtlReservations.organization_id==MtlSystemItemsB.organization_id", foreign_keys="[MtlReservations.organization_id]", viewonly=True)
        

    

    MtlReservations_inventory_item_id: Mapped["MtlReservations"] = relationship(back_populates="MtlSystemItemsB_inventory_item_id", primaryjoin="MtlReservations.inventory_item_id==MtlSystemItemsB.inventory_item_id", foreign_keys="[MtlReservations.inventory_item_id]", viewonly=True)
        

    

    MtlSafetyStocks_organization_id: Mapped["MtlSafetyStocks"] = relationship(back_populates="MtlSystemItemsB_organization_id", primaryjoin="MtlSafetyStocks.organization_id==MtlSystemItemsB.organization_id", foreign_keys="[MtlSafetyStocks.organization_id]", viewonly=True)
        

    

    MtlSafetyStocks_inventory_item_id: Mapped["MtlSafetyStocks"] = relationship(back_populates="MtlSystemItemsB_inventory_item_id", primaryjoin="MtlSafetyStocks.inventory_item_id==MtlSystemItemsB.inventory_item_id", foreign_keys="[MtlSafetyStocks.inventory_item_id]", viewonly=True)
        

    

    MtlItemRevisionsB_organization_id: Mapped["MtlItemRevisionsB"] = relationship(back_populates="MtlSystemItemsB_organization_id", primaryjoin="MtlItemRevisionsB.organization_id==MtlSystemItemsB.organization_id", foreign_keys="[MtlItemRevisionsB.organization_id]", viewonly=True)
        

    

    MtlItemRevisionsB_inventory_item_id: Mapped["MtlItemRevisionsB"] = relationship(back_populates="MtlSystemItemsB_inventory_item_id", primaryjoin="MtlItemRevisionsB.inventory_item_id==MtlSystemItemsB.inventory_item_id", foreign_keys="[MtlItemRevisionsB.inventory_item_id]", viewonly=True)



