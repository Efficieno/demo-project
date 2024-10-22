from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata

if TYPE_CHECKING:
    from ..ar.hz_cust_acct_sites_all import HzCustAcctSitesAll


class HzCustSiteUsesAll(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "hz_cust_site_uses_all"
    __table_args__ = {"schema": "ar", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 1717.9072875976562, "ui_y_pos": 1744.198486328125, "colour": "#F2F3F5"}

    site_use_id: Mapped[str] = mapped_column('site_use_id', Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    cust_acct_site_id: Mapped[str] = mapped_column('cust_acct_site_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column('last_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column('last_updated_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column('created_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    site_use_code: Mapped[str] = mapped_column('site_use_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    primary_flag: Mapped[str] = mapped_column('primary_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    status: Mapped[str] = mapped_column('status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    location: Mapped[str] = mapped_column('location', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column('last_update_login', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    contact_id: Mapped[str] = mapped_column('contact_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bill_to_site_use_id: Mapped[str] = mapped_column('bill_to_site_use_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    orig_system_reference: Mapped[str] = mapped_column('orig_system_reference', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sic_code: Mapped[str] = mapped_column('sic_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    payment_term_id: Mapped[str] = mapped_column('payment_term_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gsa_indicator: Mapped[str] = mapped_column('gsa_indicator', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_partial: Mapped[str] = mapped_column('ship_partial', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_via: Mapped[str] = mapped_column('ship_via', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    fob_point: Mapped[str] = mapped_column('fob_point', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    order_type_id: Mapped[str] = mapped_column('order_type_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    price_list_id: Mapped[str] = mapped_column('price_list_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    freight_term: Mapped[str] = mapped_column('freight_term', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    warehouse_id: Mapped[str] = mapped_column('warehouse_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    territory_id: Mapped[str] = mapped_column('territory_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
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
    request_id: Mapped[str] = mapped_column('request_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_application_id: Mapped[str] = mapped_column('program_application_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_id: Mapped[str] = mapped_column('program_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_update_date: Mapped[str] = mapped_column('program_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tax_reference: Mapped[str] = mapped_column('tax_reference', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sort_priority: Mapped[str] = mapped_column('sort_priority', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tax_code: Mapped[str] = mapped_column('tax_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute11: Mapped[str] = mapped_column('attribute11', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute12: Mapped[str] = mapped_column('attribute12', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute13: Mapped[str] = mapped_column('attribute13', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute14: Mapped[str] = mapped_column('attribute14', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute15: Mapped[str] = mapped_column('attribute15', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
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
    last_accrue_charge_date: Mapped[str] = mapped_column('last_accrue_charge_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    second_last_accrue_charge_date: Mapped[str] = mapped_column('second_last_accrue_charge_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_unaccrue_charge_date: Mapped[str] = mapped_column('last_unaccrue_charge_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    second_last_unaccrue_chrg_date: Mapped[str] = mapped_column('second_last_unaccrue_chrg_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    demand_class_code: Mapped[str] = mapped_column('demand_class_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    org_id: Mapped[str] = mapped_column('org_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tax_header_level_flag: Mapped[str] = mapped_column('tax_header_level_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tax_rounding_rule: Mapped[str] = mapped_column('tax_rounding_rule', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wh_update_date: Mapped[str] = mapped_column('wh_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
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
    global_attribute_category: Mapped[str] = mapped_column('global_attribute_category', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    primary_salesrep_id: Mapped[str] = mapped_column('primary_salesrep_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    finchrg_receivables_trx_id: Mapped[str] = mapped_column('finchrg_receivables_trx_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    dates_negative_tolerance: Mapped[str] = mapped_column('dates_negative_tolerance', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    dates_positive_tolerance: Mapped[str] = mapped_column('dates_positive_tolerance', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    date_type_preference: Mapped[str] = mapped_column('date_type_preference', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    over_shipment_tolerance: Mapped[str] = mapped_column('over_shipment_tolerance', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    under_shipment_tolerance: Mapped[str] = mapped_column('under_shipment_tolerance', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    item_cross_ref_pref: Mapped[str] = mapped_column('item_cross_ref_pref', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    over_return_tolerance: Mapped[str] = mapped_column('over_return_tolerance', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    under_return_tolerance: Mapped[str] = mapped_column('under_return_tolerance', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ship_sets_include_lines_flag: Mapped[str] = mapped_column('ship_sets_include_lines_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    arrivalsets_include_lines_flag: Mapped[str] = mapped_column('arrivalsets_include_lines_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sched_date_push_flag: Mapped[str] = mapped_column('sched_date_push_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    invoice_quantity_rule: Mapped[str] = mapped_column('invoice_quantity_rule', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    pricing_event: Mapped[str] = mapped_column('pricing_event', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_id_rec: Mapped[str] = mapped_column('gl_id_rec', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_id_rev: Mapped[str] = mapped_column('gl_id_rev', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_id_tax: Mapped[str] = mapped_column('gl_id_tax', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_id_freight: Mapped[str] = mapped_column('gl_id_freight', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_id_clearing: Mapped[str] = mapped_column('gl_id_clearing', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_id_unbilled: Mapped[str] = mapped_column('gl_id_unbilled', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_id_unearned: Mapped[str] = mapped_column('gl_id_unearned', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_id_unpaid_rec: Mapped[str] = mapped_column('gl_id_unpaid_rec', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_id_remittance: Mapped[str] = mapped_column('gl_id_remittance', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_id_factor: Mapped[str] = mapped_column('gl_id_factor', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tax_classification: Mapped[str] = mapped_column('tax_classification', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    object_version_number: Mapped[str] = mapped_column('object_version_number', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by_module: Mapped[str] = mapped_column('created_by_module', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    application_id: Mapped[str] = mapped_column('application_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    HzCustAcctSitesAll_cust_acct_site_id: Mapped["HzCustAcctSitesAll"] = relationship(back_populates="HzCustSiteUsesAll_cust_acct_site_id", primaryjoin="HzCustAcctSitesAll.cust_acct_site_id==HzCustSiteUsesAll.cust_acct_site_id", foreign_keys="[HzCustSiteUsesAll.cust_acct_site_id]", viewonly=True)



