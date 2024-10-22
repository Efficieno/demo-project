from typing import TYPE_CHECKING

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from efficieno.components.erd_objects import ERDBase, ColumnMetadata

if TYPE_CHECKING:
    from ..ar.hz_party_sites import HzPartySites


class HzParties(ERDBase):
    __data_object_type__ = "data_object"
    __tablename__ = "hz_parties"
    __table_args__ = {"schema": "ar", "extend_existing": True}
    __table_properties__ = {"ui_x_pos": 1956.0704956054688, "ui_y_pos": 1336.0321044921875, "colour": "#F2F3F5"}

    party_id: Mapped[str] = mapped_column('party_id', Integer, primary_key=True, info={"column_metadata": ColumnMetadata()})
    party_number: Mapped[str] = mapped_column('party_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    party_name: Mapped[str] = mapped_column('party_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    party_type: Mapped[str] = mapped_column('party_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    validated_flag: Mapped[str] = mapped_column('validated_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_updated_by: Mapped[str] = mapped_column('last_updated_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    creation_date: Mapped[str] = mapped_column('creation_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_login: Mapped[str] = mapped_column('last_update_login', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    request_id: Mapped[str] = mapped_column('request_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_application_id: Mapped[str] = mapped_column('program_application_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by: Mapped[str] = mapped_column('created_by', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_update_date: Mapped[str] = mapped_column('last_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_id: Mapped[str] = mapped_column('program_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    program_update_date: Mapped[str] = mapped_column('program_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    wh_update_date: Mapped[str] = mapped_column('wh_update_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
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
    attribute16: Mapped[str] = mapped_column('attribute16', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute17: Mapped[str] = mapped_column('attribute17', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute18: Mapped[str] = mapped_column('attribute18', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute19: Mapped[str] = mapped_column('attribute19', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute20: Mapped[str] = mapped_column('attribute20', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute21: Mapped[str] = mapped_column('attribute21', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute22: Mapped[str] = mapped_column('attribute22', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute23: Mapped[str] = mapped_column('attribute23', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    attribute24: Mapped[str] = mapped_column('attribute24', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute_category: Mapped[str] = mapped_column('global_attribute_category', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute1: Mapped[str] = mapped_column('global_attribute1', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute2: Mapped[str] = mapped_column('global_attribute2', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute4: Mapped[str] = mapped_column('global_attribute4', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    global_attribute3: Mapped[str] = mapped_column('global_attribute3', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
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
    orig_system_reference: Mapped[str] = mapped_column('orig_system_reference', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sic_code: Mapped[str] = mapped_column('sic_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    hq_branch_ind: Mapped[str] = mapped_column('hq_branch_ind', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    customer_key: Mapped[str] = mapped_column('customer_key', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tax_reference: Mapped[str] = mapped_column('tax_reference', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    jgzz_fiscal_code: Mapped[str] = mapped_column('jgzz_fiscal_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    duns_number: Mapped[str] = mapped_column('duns_number', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    tax_name: Mapped[str] = mapped_column('tax_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    person_pre_name_adjunct: Mapped[str] = mapped_column('person_pre_name_adjunct', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    person_first_name: Mapped[str] = mapped_column('person_first_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    person_middle_name: Mapped[str] = mapped_column('person_middle_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    person_last_name: Mapped[str] = mapped_column('person_last_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    person_name_suffix: Mapped[str] = mapped_column('person_name_suffix', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    person_title: Mapped[str] = mapped_column('person_title', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    person_academic_title: Mapped[str] = mapped_column('person_academic_title', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    person_previous_last_name: Mapped[str] = mapped_column('person_previous_last_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    known_as: Mapped[str] = mapped_column('known_as', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    person_iden_type: Mapped[str] = mapped_column('person_iden_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    person_identifier: Mapped[str] = mapped_column('person_identifier', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    group_type: Mapped[str] = mapped_column('group_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    country: Mapped[str] = mapped_column('country', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    address1: Mapped[str] = mapped_column('address1', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    address2: Mapped[str] = mapped_column('address2', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    address3: Mapped[str] = mapped_column('address3', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    address4: Mapped[str] = mapped_column('address4', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    city: Mapped[str] = mapped_column('city', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    postal_code: Mapped[str] = mapped_column('postal_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    state: Mapped[str] = mapped_column('state', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    province: Mapped[str] = mapped_column('province', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    status: Mapped[str] = mapped_column('status', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    county: Mapped[str] = mapped_column('county', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    sic_code_type: Mapped[str] = mapped_column('sic_code_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    total_num_of_orders: Mapped[str] = mapped_column('total_num_of_orders', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    total_ordered_amount: Mapped[str] = mapped_column('total_ordered_amount', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    last_ordered_date: Mapped[str] = mapped_column('last_ordered_date', Date, primary_key=False, info={"column_metadata": ColumnMetadata()})
    url: Mapped[str] = mapped_column('url', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    email_address: Mapped[str] = mapped_column('email_address', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    do_not_mail_flag: Mapped[str] = mapped_column('do_not_mail_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    analysis_fy: Mapped[str] = mapped_column('analysis_fy', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    fiscal_yearend_month: Mapped[str] = mapped_column('fiscal_yearend_month', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    employees_total: Mapped[str] = mapped_column('employees_total', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    curr_fy_potential_revenue: Mapped[str] = mapped_column('curr_fy_potential_revenue', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    next_fy_potential_revenue: Mapped[str] = mapped_column('next_fy_potential_revenue', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    year_established: Mapped[str] = mapped_column('year_established', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    gsa_indicator_flag: Mapped[str] = mapped_column('gsa_indicator_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    mission_statement: Mapped[str] = mapped_column('mission_statement', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    organization_name_phonetic: Mapped[str] = mapped_column('organization_name_phonetic', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    person_first_name_phonetic: Mapped[str] = mapped_column('person_first_name_phonetic', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    person_last_name_phonetic: Mapped[str] = mapped_column('person_last_name_phonetic', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    language_name: Mapped[str] = mapped_column('language_name', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    category_code: Mapped[str] = mapped_column('category_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    reference_use_flag: Mapped[str] = mapped_column('reference_use_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    third_party_flag: Mapped[str] = mapped_column('third_party_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    competitor_flag: Mapped[str] = mapped_column('competitor_flag', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    salutation: Mapped[str] = mapped_column('salutation', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    known_as2: Mapped[str] = mapped_column('known_as2', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    known_as3: Mapped[str] = mapped_column('known_as3', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    known_as4: Mapped[str] = mapped_column('known_as4', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    known_as5: Mapped[str] = mapped_column('known_as5', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    duns_number_c: Mapped[str] = mapped_column('duns_number_c', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    object_version_number: Mapped[str] = mapped_column('object_version_number', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    created_by_module: Mapped[str] = mapped_column('created_by_module', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    application_id: Mapped[str] = mapped_column('application_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    certification_level: Mapped[str] = mapped_column('certification_level', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    cert_reason_code: Mapped[str] = mapped_column('cert_reason_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    primary_phone_contact_pt_id: Mapped[str] = mapped_column('primary_phone_contact_pt_id', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    primary_phone_purpose: Mapped[str] = mapped_column('primary_phone_purpose', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    primary_phone_line_type: Mapped[str] = mapped_column('primary_phone_line_type', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    primary_phone_country_code: Mapped[str] = mapped_column('primary_phone_country_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    primary_phone_area_code: Mapped[str] = mapped_column('primary_phone_area_code', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    primary_phone_number: Mapped[str] = mapped_column('primary_phone_number', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    primary_phone_extension: Mapped[str] = mapped_column('primary_phone_extension', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    preferred_contact_method: Mapped[str] = mapped_column('preferred_contact_method', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    home_country: Mapped[str] = mapped_column('home_country', String, primary_key=False, info={"column_metadata": ColumnMetadata()})
    person_bo_version: Mapped[str] = mapped_column('person_bo_version', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    org_bo_version: Mapped[str] = mapped_column('org_bo_version', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    person_cust_bo_version: Mapped[str] = mapped_column('person_cust_bo_version', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})
    org_cust_bo_version: Mapped[str] = mapped_column('org_cust_bo_version', Integer, primary_key=False, info={"column_metadata": ColumnMetadata()})

        

    

    HzPartySites_party_id: Mapped["HzPartySites"] = relationship(back_populates="HzParties_party_id", primaryjoin="HzPartySites.party_id==HzParties.party_id", foreign_keys="[HzPartySites.party_id]", viewonly=True)


