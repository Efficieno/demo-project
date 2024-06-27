from efficieno.old_ontologies.ontologyv3.base import Ontology
from efficieno.old_ontologies.ontologyv3.columns import Column, ManyToOne
from demo_project.ontology.planmax_lines import PlanMaxLines


class PlanMaxHeader(Ontology):
    database_table_name = "XXPLAN_MAX_ORDER_HEADER_DTLS_VIEW"

    insert_allowed = False
    update_allowed = False
    delete_allowed = False

    business_division = Column(database_column_name="business_division", order=1)
    # sales_order_number = Column(database_column_name="sales_order_number", order=1)
    sales_order_number = ManyToOne(database_column_name="sales_order_number", relation_table_cols=PlanMaxLines.sales_order, order=2)
    # model_line_so = Column(database_column_name="model_line_so", order=2)
    model_line_so = ManyToOne(database_column_name="model_line_so", relation_table_cols=PlanMaxLines.reference_line_number, order=3)
    project_number = Column(database_column_name="project_number", order=4)
    sos_item = Column(database_column_name="sos_item", order=5)
    sos_revision = Column(database_column_name="sos_revision", order=6)
    mfg_organization = Column(database_column_name="mfg_organization", order=7)
    std_nstd = Column(database_column_name="std_nstd", order=8)

    # Order Information
    order_category = Column(database_column_name="order_category", order=9)
    oc_status = Column(database_column_name="oc_status", order=10)
    dpr_pending = Column(database_column_name="dpr_pending", order=11)
    mds_status = Column(database_column_name="mds_status", order=12)
    order_type = Column(database_column_name="order_type", order=13)
    order_cancelled = Column(database_column_name="order_cancelled", order=14)
    system_order_status = Column(database_column_name="system_order_status", order=15)
    line_item_on_model = Column(database_column_name="line_item_on_model", order=16)
    order_sub_category = Column(database_column_name="order_sub_category", order=17)
    sales_order_type = Column(database_column_name="sales_order_type", order=18)
    order_unit_value = Column(database_column_name="order_unit_value", order=19)
    order_fulfilled_status = Column(database_column_name="order_fulfilled_status", order=20)

    # Customer Details
    customer_name = Column(database_column_name="customer_name", order=21)
    bill_to_country = Column(database_column_name="bill_to_country", order=22)
    ship_to_state = Column(database_column_name="ship_to_state", order=23)
    ship_to_country = Column(database_column_name="ship_to_country", order=24)
    region = Column(database_column_name="region", order=25)
    bill_to_city = Column(database_column_name="bill_to_city", order=26)

    # Dates
    planned_del_month = Column(database_column_name="planned_del_month", order=27)
    prn_delivery_date = Column(database_column_name="prn_delivery_date", order=28)
    last_drp_date = Column(database_column_name="last_drp_date", order=29)
    original_contract_delivery_dt = Column(database_column_name="original_contract_delivery_dt", order=30)
    oc_date = Column(database_column_name="oc_date", order=31)
    first_mds_date = Column(database_column_name="first_mds_date", order=32)
    prn_date = Column(database_column_name="prn_date", order=33)
    plan_eol_mech_date = Column(database_column_name="plan_eol_mech_date", order=34)
    commission_date = Column(database_column_name="commission_date", order=35)
    so_date = Column(database_column_name="so_date", order=36)
    customer_po_date = Column(database_column_name="customer_po_date", order=37)
    original_contract_del_month = Column(database_column_name="original_contract_del_month", order=37)
    engg_commt_date = Column(database_column_name="engg_commt_date", order=38)
    last_mds_date = Column(database_column_name="last_mds_date", order=39)
    sos_revision_date = Column(database_column_name="sos_revision_date", order=40)
    di_date = Column(database_column_name="di_date", order=41)
    fg_date = Column(database_column_name="fg_date", order=42)
    llbom_release_date = Column(database_column_name="llbom_release_date", order=43)
    first_drp_date = Column(database_column_name="first_drp_date", order=44)
    current_cust_cont_del_date = Column(database_column_name="current_cust_cont_del_date", order=45)
    current_cust_cont_del_month = Column(database_column_name="current_cust_cont_del_month", order=46)
    orig_commited_del_dt = Column(database_column_name="orig_commited_del_dt", order=47)
    invoice_date = Column(database_column_name="invoice_date", order=48)
    site_release_date = Column(database_column_name="site_release_date", order=49)
    fg_pp_date = Column(database_column_name="fg_pp_date", order=50)
    planned_eol_eni_date = Column(database_column_name="planned_eol_eni_date", order=51)
    suggested_plan_date = Column(database_column_name="suggested_plan_date", order=52)

    # Invocie Data
    invoice_number = Column(database_column_name="invoice_number", order=53)
    planned_invoice_date = Column(database_column_name="planned_invoice_date", order=54)
    regional_commercial = Column(database_column_name="regional_commercial", order=55)
    insurance_by = Column(database_column_name="insurance_by", order=56)
    abp_percent = Column(database_column_name="abp_percent", order=57)
    pgb_percent = Column(database_column_name="pgb_percent", order=58)
    penalty = Column(database_column_name="penalty", order=59)
    invoiced_value = Column(database_column_name="invoiced_value", order=60)
    order_currency = Column(database_column_name="order_currency", order=61)
    transport_scope = Column(database_column_name="transport_scope", order=62)
    freight_pay = Column(database_column_name="freight_pay", order=63)
    planned_invoice_value = Column(database_column_name="planned_invoice_value", order=64)
    total_order_value = Column(database_column_name="total_order_value", order=65)

    # Thermax Details
    ho_order_to_sales_order = Column(database_column_name="ho_order_to_sales_order", order=66)
    project_specific_llbom = Column(database_column_name="project_specific_llbom", order=67)
    job_folder_release_date = Column(database_column_name="job_folder_release_date", order=68)
    dpr_planned_items = Column(database_column_name="dpr_planned_items", order=69)
    contract_plan_otp = Column(database_column_name="contract_plan_otp", order=70)
    ho_order_commited_to = Column(database_column_name="ho_order_commited_to", order=71)
    di_value = Column(database_column_name="di_value", order=72)
    brief_scope = Column(database_column_name="brief_scope", order=73)
    sales_engineer = Column(database_column_name="sales_engineer", order=74)
    prn_applicable = Column(database_column_name="prn_applicable", order=75)
    oc_required = Column(database_column_name="oc_required", order=76)
    ld_applicable = Column(database_column_name="ld_applicable", order=77)
    fg_month_change_remarks = Column(database_column_name="fg_month_change_remarks", order=78)
    inco_terms = Column(database_column_name="inco_terms", order=79)
    technical_ocl = Column(database_column_name="technical_ocl", order=80)
    product_model = Column(database_column_name="product_model", order=81)
    oc_closure_date = Column(database_column_name="oc_closure_date", order=82)
    prn_no = Column(database_column_name="prn_no", order=83)
    shop_sub_contract = Column(database_column_name="shop_sub_contract", order=84)
    total_payment = Column(database_column_name="total_payment", order=85)

    # Other info
    per_po_closed = Column(database_column_name="per_po_closed", order=86)
    reason_for_otp = Column(database_column_name="reason_for_otp", order=87)
    original_project_number = Column(database_column_name="original_project_number", order=88)
    bonus = Column(database_column_name="bonus", order=89)
    planner = Column(database_column_name="planner", order=90)
    curr_order_execution_status = Column(database_column_name="curr_order_execution_status", order=91)
    oc_number = Column(database_column_name="oc_number", order=92)
    per_dj_closed = Column(database_column_name="per_dj_closed", order=93)
    di_number = Column(database_column_name="di_number", order=94)
    send_mail = Column(database_column_name="send_mail", order=95)
    fuel_type = Column(database_column_name="fuel_type", order=96)
    tech_clarity_date = Column(database_column_name="tech_clarity_date", order=97)
    ll_pr = Column(database_column_name="ll_pr", order=98)
    sos_item_count = Column(database_column_name="sos_item_count", order=99)
    inspection_required = Column(database_column_name="inspection_required", order=100)
    tca = Column(database_column_name="tca", order=101)
    shell_boiler_appr_authority = Column(database_column_name="shell_boiler_appr_authority", order=102)
    rated_standard_man_hrs = Column(database_column_name="rated_standard_man_hrs", order=103)
    folder_status = Column(database_column_name="folder_status", order=104)
    delivery_otp = Column(database_column_name="delivery_otp", order=105)

    @classmethod
    def insert(cls, record: dict):
        pass

    @classmethod
    def update(cls, old_record: dict, updated_columns: list):
        pass

    @classmethod
    def delete(cls, record: dict):
        pass
