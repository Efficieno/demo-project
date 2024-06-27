from efficieno.old_components.components.table_views.base import TableView
from efficieno.old_components.components.table_views.columns import TableColumn
from demo_project.ontology.planmax_lines import PlanMaxLines


class DetailPlanAllColumns(TableView):
    table_header = "Plan Max Detail Plan"
    table_description = "PLan Max Detail Plan"

    sales_order = TableColumn(PlanMaxLines.sales_order, order=1)
    reference_line_number = TableColumn(PlanMaxLines.reference_line_number, order=2)
    line_number = TableColumn(PlanMaxLines.line_number, order=3)
    ordered_item = TableColumn(PlanMaxLines.ordered_item, order=4)
    ordered_quantity = TableColumn(PlanMaxLines.ordered_quantity, order=5)
    project_number = TableColumn(PlanMaxLines.project_number, order=6)
    task_number = TableColumn(PlanMaxLines.task_number, order=7)
    sos_item = TableColumn(PlanMaxLines.sos_item, order=8)
    sos_revision_date = TableColumn(PlanMaxLines.sos_revision_date, order=9)
    sos_revision = TableColumn(PlanMaxLines.sos_revision, order=10)
    system_line_status = TableColumn(PlanMaxLines.system_line_status, order=11)
    line_request_date = TableColumn(PlanMaxLines.line_request_date, order=12)
    task_name = TableColumn(PlanMaxLines.task_name, order=13)

    # wip Details
    wip_job_type = TableColumn(PlanMaxLines.wip_job_type, order=14)
    wip_job_class = TableColumn(PlanMaxLines.wip_job_class, order=15)
    wip_completion_qty = TableColumn(PlanMaxLines.wip_completion_qty, order=16)
    wip_job_no = TableColumn(PlanMaxLines.wip_job_no, order=17)
    pending_wdj_qty = TableColumn(PlanMaxLines.pending_wdj_qty, order=18)
    wip_job_id = TableColumn(PlanMaxLines.wip_job_id, order=19)
    wdj_doc_qty = TableColumn(PlanMaxLines.wdj_doc_qty, order=20)
    current_dj_status = TableColumn(PlanMaxLines.current_dj_status, order=21)

    # PO Details
    buyer_code = TableColumn(PlanMaxLines.buyer_code, order=22)
    po_line_number = TableColumn(PlanMaxLines.po_line_number, order=23)
    po_status = TableColumn(PlanMaxLines.po_status, order=24)
    receipt_qty = TableColumn(PlanMaxLines.receipt_qty, order=25)
    po_uom = TableColumn(PlanMaxLines.po_uom, order=26)
    po_number = TableColumn(PlanMaxLines.po_number, order=27)
    pr_no = TableColumn(PlanMaxLines.pr_no, order=28)
    po_doc_qty = TableColumn(PlanMaxLines.po_doc_qty, order=29)
    item_req_date_opseq = TableColumn(PlanMaxLines.item_req_date_opseq, order=30)
    pending_po_qty = TableColumn(PlanMaxLines.pending_po_qty, order=31)
    current_pr_status = TableColumn(PlanMaxLines.current_pr_status, order=32)
    po_approval_date = TableColumn(PlanMaxLines.po_approval_date, order=33)
    completed_supply_qty = TableColumn(PlanMaxLines.completed_supply_qty, order=34)
    po_received_qty = TableColumn(PlanMaxLines.po_received_qty, order=35)
    qty_inspected = TableColumn(PlanMaxLines.qty_inspected, order=36)

    # Lead Time
    postprocessing_lt = TableColumn(PlanMaxLines.postprocessing_lt, order=37)
    full_lt = TableColumn(PlanMaxLines.full_lt, order=38)
    mfg_lt = TableColumn(PlanMaxLines.mfg_lt, order=39)
    fixed_lt = TableColumn(PlanMaxLines.fixed_lt, order=40)
    preprocessing_lt = TableColumn(PlanMaxLines.preprocessing_lt, order=41)
    variable_lt = TableColumn(PlanMaxLines.variable_lt, order=42)

    # Metadata
    parent_item = TableColumn(PlanMaxLines.parent_item, order=43)
    parent_item_desc = TableColumn(PlanMaxLines.parent_item_desc, order=44)
    item_description = TableColumn(PlanMaxLines.item_description, order=45)
    inv_planning_method = TableColumn(PlanMaxLines.inv_planning_method, order=46)
    weight_uom = TableColumn(PlanMaxLines.weight_uom, order=47)
    item_weight = TableColumn(PlanMaxLines.item_weight, order=48)
    item_uom = TableColumn(PlanMaxLines.item_uom, order=49)
    need_on_order = TableColumn(PlanMaxLines.need_on_order, order=50)
    user_item_type = TableColumn(PlanMaxLines.user_item_type, order=51)
    mrp_planned = TableColumn(PlanMaxLines.mrp_planned, order=52)
    order_uom = TableColumn(PlanMaxLines.order_uom, order=53)
    osp = TableColumn(PlanMaxLines.osp, order=54)
    avg_cost = TableColumn(PlanMaxLines.avg_cost, order=55)
    item_dim_uom = TableColumn(PlanMaxLines.item_dim_uom, order=56)
    unit_selling_price = TableColumn(PlanMaxLines.unit_selling_price, order=57)
    item_dim_lxwxh = TableColumn(PlanMaxLines.item_dim_lxwxh, order=58)
    warehouse_org_exists = TableColumn(PlanMaxLines.warehouse_org_exists, order=59)
    make_buy = TableColumn(PlanMaxLines.make_buy, order=60)

    # Reservations
    non_proj_reserved_qty = TableColumn(PlanMaxLines.non_proj_reserved_qty, order=61)
    project_inventory = TableColumn(PlanMaxLines.project_inventory, order=62)
    pegging = TableColumn(PlanMaxLines.pegging, order=63)

    # Dates
    system_sch_ship_date = TableColumn(PlanMaxLines.system_sch_ship_date, order=64)
    commit_dt_mat_mfg = TableColumn(PlanMaxLines.commit_dt_mat_mfg, order=65)

    # BOM Data
    bom_uom = TableColumn(PlanMaxLines.bom_uom, order=66)
    bom_item_rev = TableColumn(PlanMaxLines.bom_item_rev, order=67)
    engg_org_exists = TableColumn(PlanMaxLines.engg_org_exists, order=68)
    indent_bom_fin_wt = TableColumn(PlanMaxLines.indent_bom_fin_wt, order=69)
    bom_so_comparison = TableColumn(PlanMaxLines.bom_so_comparison, order=70)
    item_fm_extd_bom = TableColumn(PlanMaxLines.item_fm_extd_bom, order=71)
    bom_level = TableColumn(PlanMaxLines.bom_level, order=72)
    routing = TableColumn(PlanMaxLines.routing, order=73)
    bom_qty = TableColumn(PlanMaxLines.bom_qty, order=74)

    # Customer
    ship_from_org = TableColumn(PlanMaxLines.ship_from_org, order=75)
    supplier = TableColumn(PlanMaxLines.supplier, order=76)

    # Status Flags
    complete_reflection = TableColumn(PlanMaxLines.complete_reflection, order=77)
    dpr_date = TableColumn(PlanMaxLines.dpr_date, order=78)
    ln_status_supply_persp = TableColumn(PlanMaxLines.ln_status_supply_persp, order=79)
