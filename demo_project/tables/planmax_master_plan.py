from efficieno.old_components.components.table_views.base import TableView
from efficieno.old_components.components.table_views.columns import TableColumn
from demo_project.ontology.planmax_header import PlanMaxHeader


class MasterPlan(TableView):
    table_header = "Plan Max Master Plan"
    table_description = "PLan Max Master Plan"

    sales_order_number = TableColumn(PlanMaxHeader.sales_order_number, order=1, display_name="Sales Order Number")
    model_line_so = TableColumn(PlanMaxHeader.model_line_so, order=2, display_name="Model Line SO")
    so_date = TableColumn(PlanMaxHeader.so_date, order=3, display_name="SO Date")
    region = TableColumn(PlanMaxHeader.region, order=4, display_name="Region")
    order_category = TableColumn(PlanMaxHeader.order_category, order=5, display_name="Order Category")
    customer_name = TableColumn(PlanMaxHeader.customer_name, order=6, display_name="Customer Name")
    order_currency = TableColumn(PlanMaxHeader.order_currency, order=7, display_name="Order Currency")
    order_unit_value = TableColumn(PlanMaxHeader.order_unit_value, order=8, display_name="Order unit value")
    project_number = TableColumn(PlanMaxHeader.project_number, order=9, display_name="Project Number")
    std_nstd = TableColumn(PlanMaxHeader.std_nstd, order=10, display_name="STD Non STD")
    sos_item = TableColumn(PlanMaxHeader.sos_item, order=11, display_name="SOS Item")
    sos_revision = TableColumn(PlanMaxHeader.sos_revision, order=12, display_name="SOS EN1 Rev")
    mfg_organization = TableColumn(PlanMaxHeader.mfg_organization, order=13, display_name="MFG Org")
    prn_no = TableColumn(PlanMaxHeader.prn_no, order=14, display_name="PRN No")
    prn_date = TableColumn(PlanMaxHeader.prn_date, order=15, display_name="PRN Date")
    current_cust_cont_del_month = TableColumn(PlanMaxHeader.current_cust_cont_del_month, order=16, display_name="Current Cust Del Month")
    planner = TableColumn(PlanMaxHeader.planner, order=17, display_name="Planner")
    fuel_type = TableColumn(PlanMaxHeader.fuel_type, order=18, display_name="Fuel Type")
    folder_status = TableColumn(PlanMaxHeader.folder_status, order=19, display_name="Folder Status")
    job_folder_release_date = TableColumn(PlanMaxHeader.job_folder_release_date, order=20, display_name="Job Folder Rel Date")
    technical_ocl = TableColumn(PlanMaxHeader.technical_ocl, order=21, display_name="Technical OCL")
    oc_date = TableColumn(PlanMaxHeader.oc_date, order=22, display_name="OC Date")

    di_date = TableColumn(PlanMaxHeader.di_date, order=23, display_name="DI Date")
    fg_date = TableColumn(PlanMaxHeader.fg_date, order=24, display_name="FG Date")
    orig_commited_del_dt = TableColumn(PlanMaxHeader.orig_commited_del_dt, order=25, display_name="Original Commit Del Date")
    invoiced_value = TableColumn(PlanMaxHeader.invoiced_value, order=26, display_name="Invoiced Value")
    freight_pay = TableColumn(PlanMaxHeader.freight_pay, order=27, display_name="Freight Pay")
    di_value = TableColumn(PlanMaxHeader.di_value, order=28, display_name="DI Value")
    inco_terms = TableColumn(PlanMaxHeader.inco_terms, order=29, display_name="INCO Terms")

    order_type = TableColumn(PlanMaxHeader.order_type, order=30, display_name="Order Type")
    order_sub_category = TableColumn(PlanMaxHeader.order_sub_category, order=31, display_name="Order Sub Category")
    sales_order_type = TableColumn(PlanMaxHeader.sales_order_type, order=32, display_name="Sales Order Type")
    ship_to_country = TableColumn(PlanMaxHeader.ship_to_country, order=33, display_name="Ship to Country")

    # dpr_pending = TableColumn(PlanMaxHeader.dpr_pending, order=9, display_name="DPR Pending")
    # prn_delivery_date = TableColumn(PlanMaxHeader.prn_delivery_date, order=17, display_name="PRN Delivery Date")
    # first_drp_date = TableColumn(PlanMaxHeader.first_drp_date, order=23, display_name="First DRP Date")
    # contract_plan_otp = TableColumn(PlanMaxHeader.contract_plan_otp, order=30, display_name="Contract Plan OTP")

    # business_division = OU