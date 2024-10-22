from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata

if TYPE_CHECKING:
    from ..po.po_req_distributions_all import PoReqDistributionsAll
    from ..po.po_lines_all import PoLinesAll


class PoDistributionsAll(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "po_distributions_all"
    __table_args__ = {"schema": "po", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 441.56317138671875, "ui_y_pos": 1578.3536376953125, "colour": "#F2F3F5"}

    po_distribution_id: Mapped[str] = mapped_column('po_distribution_id', Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column('last_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column('last_updated_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_header_id: Mapped[str] = mapped_column('po_header_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_line_id: Mapped[str] = mapped_column('po_line_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    line_location_id: Mapped[str] = mapped_column('line_location_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    set_of_books_id: Mapped[str] = mapped_column('set_of_books_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    code_combination_id: Mapped[str] = mapped_column('code_combination_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quantity_ordered: Mapped[str] = mapped_column('quantity_ordered', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column('last_update_login', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column('created_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    po_release_id: Mapped[str] = mapped_column('po_release_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quantity_delivered: Mapped[str] = mapped_column('quantity_delivered', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quantity_billed: Mapped[str] = mapped_column('quantity_billed', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quantity_cancelled: Mapped[str] = mapped_column('quantity_cancelled', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_header_reference_num: Mapped[str] = mapped_column('req_header_reference_num', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_line_reference_num: Mapped[str] = mapped_column('req_line_reference_num', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    req_distribution_id: Mapped[str] = mapped_column('req_distribution_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    deliver_to_location_id: Mapped[str] = mapped_column('deliver_to_location_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    deliver_to_person_id: Mapped[str] = mapped_column('deliver_to_person_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    rate_date: Mapped[str] = mapped_column('rate_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    rate: Mapped[str] = mapped_column('rate', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    amount_billed: Mapped[str] = mapped_column('amount_billed', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    accrued_flag: Mapped[str] = mapped_column('accrued_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    encumbered_flag: Mapped[str] = mapped_column('encumbered_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    encumbered_amount: Mapped[str] = mapped_column('encumbered_amount', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    unencumbered_quantity: Mapped[str] = mapped_column('unencumbered_quantity', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    unencumbered_amount: Mapped[str] = mapped_column('unencumbered_amount', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    failed_funds_lookup_code: Mapped[str] = mapped_column('failed_funds_lookup_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_encumbered_date: Mapped[str] = mapped_column('gl_encumbered_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_encumbered_period_name: Mapped[str] = mapped_column('gl_encumbered_period_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_cancelled_date: Mapped[str] = mapped_column('gl_cancelled_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    destination_type_code: Mapped[str] = mapped_column('destination_type_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    destination_organization_id: Mapped[str] = mapped_column('destination_organization_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    destination_subinventory: Mapped[str] = mapped_column('destination_subinventory', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
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
    wip_entity_id: Mapped[str] = mapped_column('wip_entity_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_operation_seq_num: Mapped[str] = mapped_column('wip_operation_seq_num', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_resource_seq_num: Mapped[str] = mapped_column('wip_resource_seq_num', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_repetitive_schedule_id: Mapped[str] = mapped_column('wip_repetitive_schedule_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wip_line_id: Mapped[str] = mapped_column('wip_line_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    bom_resource_id: Mapped[str] = mapped_column('bom_resource_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    budget_account_id: Mapped[str] = mapped_column('budget_account_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    accrual_account_id: Mapped[str] = mapped_column('accrual_account_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    variance_account_id: Mapped[str] = mapped_column('variance_account_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    prevent_encumbrance_flag: Mapped[str] = mapped_column('prevent_encumbrance_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    ussgl_transaction_code: Mapped[str] = mapped_column('ussgl_transaction_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    government_context: Mapped[str] = mapped_column('government_context', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    destination_context: Mapped[str] = mapped_column('destination_context', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    distribution_num: Mapped[str] = mapped_column('distribution_num', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    source_distribution_id: Mapped[str] = mapped_column('source_distribution_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    request_id: Mapped[str] = mapped_column('request_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_application_id: Mapped[str] = mapped_column('program_application_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_id: Mapped[str] = mapped_column('program_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_update_date: Mapped[str] = mapped_column('program_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_id: Mapped[str] = mapped_column('project_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    task_id: Mapped[str] = mapped_column('task_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    expenditure_type: Mapped[str] = mapped_column('expenditure_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    project_accounting_context: Mapped[str] = mapped_column('project_accounting_context', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    expenditure_organization_id: Mapped[str] = mapped_column('expenditure_organization_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gl_closed_date: Mapped[str] = mapped_column('gl_closed_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    accrue_on_receipt_flag: Mapped[str] = mapped_column('accrue_on_receipt_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    expenditure_item_date: Mapped[str] = mapped_column('expenditure_item_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    org_id: Mapped[str] = mapped_column('org_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    kanban_card_id: Mapped[str] = mapped_column('kanban_card_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    award_id: Mapped[str] = mapped_column('award_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mrc_rate_date: Mapped[str] = mapped_column('mrc_rate_date', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mrc_rate: Mapped[str] = mapped_column('mrc_rate', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mrc_encumbered_amount: Mapped[str] = mapped_column('mrc_encumbered_amount', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mrc_unencumbered_amount: Mapped[str] = mapped_column('mrc_unencumbered_amount', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    end_item_unit_number: Mapped[str] = mapped_column('end_item_unit_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tax_recovery_override_flag: Mapped[str] = mapped_column('tax_recovery_override_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    recoverable_tax: Mapped[str] = mapped_column('recoverable_tax', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    nonrecoverable_tax: Mapped[str] = mapped_column('nonrecoverable_tax', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    recovery_rate: Mapped[str] = mapped_column('recovery_rate', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    oke_contract_line_id: Mapped[str] = mapped_column('oke_contract_line_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    oke_contract_deliverable_id: Mapped[str] = mapped_column('oke_contract_deliverable_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    amount_ordered: Mapped[str] = mapped_column('amount_ordered', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    amount_delivered: Mapped[str] = mapped_column('amount_delivered', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    amount_cancelled: Mapped[str] = mapped_column('amount_cancelled', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    distribution_type: Mapped[str] = mapped_column('distribution_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    amount_to_encumber: Mapped[str] = mapped_column('amount_to_encumber', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    invoice_adjustment_flag: Mapped[str] = mapped_column('invoice_adjustment_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    dest_charge_account_id: Mapped[str] = mapped_column('dest_charge_account_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    dest_variance_account_id: Mapped[str] = mapped_column('dest_variance_account_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quantity_financed: Mapped[str] = mapped_column('quantity_financed', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    amount_financed: Mapped[str] = mapped_column('amount_financed', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quantity_recouped: Mapped[str] = mapped_column('quantity_recouped', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    amount_recouped: Mapped[str] = mapped_column('amount_recouped', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    retainage_withheld_amount: Mapped[str] = mapped_column('retainage_withheld_amount', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    retainage_released_amount: Mapped[str] = mapped_column('retainage_released_amount', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wf_item_key: Mapped[str] = mapped_column('wf_item_key', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    invoiced_val_in_ntfn: Mapped[str] = mapped_column('invoiced_val_in_ntfn', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tax_attribute_update_code: Mapped[str] = mapped_column('tax_attribute_update_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    event_id: Mapped[str] = mapped_column('event_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    interface_distribution_ref: Mapped[str] = mapped_column('interface_distribution_ref', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    lcm_flag: Mapped[str] = mapped_column('lcm_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    group_line_id: Mapped[str] = mapped_column('group_line_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    uda_template_id: Mapped[str] = mapped_column('uda_template_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    draft_id: Mapped[str] = mapped_column('draft_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    amount_funded: Mapped[str] = mapped_column('amount_funded', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    funded_value: Mapped[str] = mapped_column('funded_value', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    partial_funded_flag: Mapped[str] = mapped_column('partial_funded_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    quantity_funded: Mapped[str] = mapped_column('quantity_funded', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    clm_misc_loa: Mapped[str] = mapped_column('clm_misc_loa', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    clm_defence_funding: Mapped[str] = mapped_column('clm_defence_funding', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    clm_fms_case_number: Mapped[str] = mapped_column('clm_fms_case_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    clm_agency_acct_identifier: Mapped[str] = mapped_column('clm_agency_acct_identifier', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    change_in_funded_value: Mapped[str] = mapped_column('change_in_funded_value', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    acrn: Mapped[str] = mapped_column('acrn', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    revision_num: Mapped[str] = mapped_column('revision_num', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    amount_reversed: Mapped[str] = mapped_column('amount_reversed', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    clm_payment_sequence_num: Mapped[str] = mapped_column('clm_payment_sequence_num', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    amount_changed_flag: Mapped[str] = mapped_column('amount_changed_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
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

        

    

    PoReqDistributionsAll_distribution_id: Mapped["PoReqDistributionsAll"] = relationship(back_populates="PoDistributionsAll_req_distribution_id", primaryjoin="PoReqDistributionsAll.distribution_id==PoDistributionsAll.req_distribution_id", foreign_keys="[PoReqDistributionsAll.distribution_id]", viewonly=True)
        

    

    PoLinesAll_po_line_id: Mapped["PoLinesAll"] = relationship(back_populates="PoDistributionsAll_po_line_id", primaryjoin="PoLinesAll.po_line_id==PoDistributionsAll.po_line_id", foreign_keys="[PoDistributionsAll.po_line_id]", viewonly=True)


