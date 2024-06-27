from efficieno.old_ontologies.ontologyv3.base import Ontology
from efficieno.old_ontologies.ontologyv3.columns import Column, ManyToOne, OneToMany
from demo_project.ontology.planmax_wip_details import PlanMaxWipDetails


class PlanMaxLines(Ontology):
    database_table_name = "XXPLAN_MAX_ORDER_LINE_DTLS_VIEW"

    insert_allowed = False
    update_allowed = False
    delete_allowed = False

    sales_order = Column(database_column_name="sales_order", order=1)
    # sales_order = OneToMany(database_column_name="sales_order", relation_table_cols=PlanMaxHeader.sales_order_number, order=1)
    reference_line_number = Column(database_column_name="reference_line_number", order=2)
    # reference_line_number = OneToMany(database_column_name="reference_line_number", relation_table_cols=PlanMaxHeader.model_line_so, order=2)
    line_number = Column(database_column_name="line_number", order=3)
    ordered_item = Column(database_column_name="ordered_item", order=4)
    ordered_quantity = Column(database_column_name="ordered_quantity", order=5)
    project_number = Column(database_column_name="project_number", order=6)
    task_number = Column(database_column_name="task_number", order=7)
    sos_item = Column(database_column_name="sos_item", order=8)
    sos_revision_date = Column(database_column_name="sos_revision_date", order=9)
    sos_revision = Column(database_column_name="sos_revision", order=10)
    system_line_status = Column(database_column_name="system_line_status", order=11)
    line_request_date = Column(database_column_name="line_request_date", order=12)
    task_name = Column(database_column_name="task_name", order=13)
    need_on_order = Column(database_column_name="need_on_order", order=13.2)

    # wip Details
    wip_job_type = Column(database_column_name="wip_job_type", order=14)
    wip_job_class = Column(database_column_name="wip_job_class", order=15)
    wip_completion_qty = Column(database_column_name="wip_completion_qty", order=16)
    wip_job_no = Column(database_column_name="wip_job_no", order=17)
    pending_wdj_qty = Column(database_column_name="pending_wdj_qty", order=18)
    # wip_job_id = Column(database_column_name="wip_job_id", order=19)
    wip_job_id = ManyToOne(database_column_name="wip_job_id", relation_table_cols=PlanMaxWipDetails.wip_entity_id, order=19)
    wdj_doc_qty = Column(database_column_name="wdj_doc_qty", order=20)
    current_dj_status = Column(database_column_name="current_dj_status", order=21)

    # PO Details
    buyer_code = Column(database_column_name="buyer_code", order=22)
    po_line_number = Column(database_column_name="po_line_number", order=23)
    po_status = Column(database_column_name="po_status", order=24)
    receipt_qty = Column(database_column_name="receipt_qty", order=25)
    po_uom = Column(database_column_name="po_uom", order=26)
    po_number = Column(database_column_name="po_number", order=27)
    pr_no = Column(database_column_name="pr_no", order=28)
    po_doc_qty = Column(database_column_name="po_doc_qty", order=29)
    item_req_date_opseq = Column(database_column_name="item_req_date_opseq", order=30)
    pending_po_qty = Column(database_column_name="pending_po_qty", order=31)
    current_pr_status = Column(database_column_name="current_pr_status", order=32)
    po_approval_date = Column(database_column_name="po_approval_date", order=33)
    completed_supply_qty = Column(database_column_name="completed_supply_qty", order=34)
    po_received_qty = Column(database_column_name="po_received_qty", order=35)
    qty_inspected = Column(database_column_name="qty_inspected", order=36)

    # Lead Time
    postprocessing_lt = Column(database_column_name="postprocessing_lt", order=37)
    full_lt = Column(database_column_name="full_lt", order=38)
    mfg_lt = Column(database_column_name="mfg_lt", order=39)
    fixed_lt = Column(database_column_name="fixed_lt", order=40)
    preprocessing_lt = Column(database_column_name="preprocessing_lt", order=41)
    variable_lt = Column(database_column_name="variable_lt", order=42)

    # Metadata
    parent_item = Column(database_column_name="parent_item", order=43)
    parent_item_desc = Column(database_column_name="parent_item_desc", order=44)
    item_description = Column(database_column_name="item_description", order=45)
    inv_planning_method = Column(database_column_name="inv_planning_method", order=46)
    weight_uom = Column(database_column_name="weight_uom", order=47)
    item_weight = Column(database_column_name="item_weight", order=48)
    item_uom = Column(database_column_name="item_uom", order=49)
    user_item_type = Column(database_column_name="user_item_type", order=51)
    mrp_planned = Column(database_column_name="mrp_planned", order=52)
    order_uom = Column(database_column_name="order_uom", order=53)
    osp = Column(database_column_name="osp", order=54)
    avg_cost = Column(database_column_name="avg_cost", order=55)
    item_dim_uom = Column(database_column_name="item_dim_uom", order=56)
    unit_selling_price = Column(database_column_name="unit_selling_price", order=57)
    item_dim_lxwxh = Column(database_column_name="item_dim_lxwxh", order=58)
    warehouse_org_exists = Column(database_column_name="warehouse_org_exists", order=59)
    make_buy = Column(database_column_name="make_buy", order=60)

    # Reservations
    non_proj_reserved_qty = Column(database_column_name="non_proj_reserved_qty", order=61)
    project_inventory = Column(database_column_name="project_inventory", order=62)
    pegging = Column(database_column_name="pegging", order=63)

    # Dates
    system_sch_ship_date = Column(database_column_name="system_sch_ship_date", order=64)
    commit_dt_mat_mfg = Column(database_column_name="commit_dt_mat_mfg", order=65)

    # BOM Data
    bom_uom = Column(database_column_name="bom_uom", order=66)
    bom_item_rev = Column(database_column_name="bom_item_rev", order=67)
    engg_org_exists = Column(database_column_name="engg_org_exists", order=68)
    indent_bom_fin_wt = Column(database_column_name="indent_bom_fin_wt", order=69)
    bom_so_comparison = Column(database_column_name="bom_so_comparison", order=70)
    item_fm_extd_bom = Column(database_column_name="item_fm_extd_bom", order=71)
    bom_level = Column(database_column_name="bom_level", order=72)
    routing = Column(database_column_name="routing", order=73)
    bom_qty = Column(database_column_name="bom_qty", order=74)

    # Customer
    ship_from_org = Column(database_column_name="ship_from_org", order=75)
    supplier = Column(database_column_name="supplier", order=76)

    # Status Flags
    complete_reflection = Column(database_column_name="complete_reflection", order=77)
    dpr_date = Column(database_column_name="dpr_date", order=78)
    ln_status_supply_persp = Column(database_column_name="ln_status_supply_persp", order=79)

    @classmethod
    def insert(cls, record: dict):
        pass

    @classmethod
    def update(cls, old_record: dict, updated_columns: list):
        pass

    @classmethod
    def delete(cls, record: dict):
        pass
