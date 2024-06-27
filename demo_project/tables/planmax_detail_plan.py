from efficieno.old_components.components.table_views.base import TableView
from efficieno.old_components.components.table_views.columns import TableColumn
from demo_project.ontology.planmax_lines import PlanMaxLines


class DetailPlan(TableView):
    table_header = "Plan Max Detail Plan"
    table_description = "PLan Max Detail Plan"

    project_number = TableColumn(PlanMaxLines.project_number, order=1, display_name="Project Number")
    sales_order = TableColumn(PlanMaxLines.sales_order, order=1.5, display_name="Sales Order Number")
    reference_line_number = TableColumn(PlanMaxLines.reference_line_number, order=2, display_name="Reference Line Number")
    need_on_order = TableColumn(PlanMaxLines.need_on_order, order=3, display_name="Line Classification")
    line_number = TableColumn(PlanMaxLines.line_number, order=4, display_name="Line Number")

    ordered_item = TableColumn(PlanMaxLines.ordered_item, order=5, display_name="Item")
    ordered_quantity = TableColumn(PlanMaxLines.ordered_quantity, order=6, display_name="Ordered Quantity")
    # task_number = TableColumn(PlanMaxLines.task_number, order=7, display_name="Task Number")
    # sos_item = TableColumn(PlanMaxLines.sos_item, order=8, display_name="SOS Item")
    # sos_revision_date = TableColumn(PlanMaxLines.sos_revision_date, order=9, display_name="SOS Revision Date")
    # sos_revision = TableColumn(PlanMaxLines.sos_revision, order=10, display_name="SOS Revision")
    system_sch_ship_date = TableColumn(PlanMaxLines.system_sch_ship_date, order=7, display_name="Scheduled Ship Date")
    mrp_planned = TableColumn(PlanMaxLines.mrp_planned, order=8, display_name="MRP Planned")
    user_item_type = TableColumn(PlanMaxLines.user_item_type, order=9, display_name="Item Type")
    warehouse_org_exists = TableColumn(PlanMaxLines.warehouse_org_exists, order=10, display_name="Exists in MFG Org")
    engg_org_exists = TableColumn(PlanMaxLines.engg_org_exists, order=11, display_name="Exists in ENG Org")

    # Wip Details
    wip_job_no = TableColumn(PlanMaxLines.wip_job_no, order=12, display_name="WIP Job Number")
    current_dj_status = TableColumn(PlanMaxLines.current_dj_status, order=13, display_name="WIP Job Current Status")
    # wip_job_type = TableColumn(PlanMaxLines.wip_job_type, order=14, display_name="WIP Job Type")
    # wip_job_class = TableColumn(PlanMaxLines.wip_job_class, order=15, display_name="WIP Job Class")
    # wip_completion_qty = TableColumn(PlanMaxLines.wip_completion_qty, order=16, display_name="WIP Completion Quantity")
    # pending_wdj_qty = TableColumn(PlanMaxLines.pending_wdj_qty, order=18, display_name="WIP Pending Quantity")
    # wip_job_id = Column(database_column_name="wip_job_id", order=19)
    wip_job_id = TableColumn(PlanMaxLines.wip_job_id, order=13.1, display_name="WIP Job ID")
    # wdj_doc_qty = TableColumn(PlanMaxLines.wdj_doc_qty, order=20, display_name="WIP Job Start Quantity")

    # PO / PR Details
    pr_no = TableColumn(PlanMaxLines.pr_no, order=14, display_name="PR Number")
    current_pr_status = TableColumn(PlanMaxLines.current_pr_status, order=15, display_name="PR Status")

    po_number = TableColumn(PlanMaxLines.po_number, order=16, display_name="PO Number")
    po_line_number = TableColumn(PlanMaxLines.po_line_number, order=17, display_name="PO Line Number")
    po_status = TableColumn(PlanMaxLines.po_status, order=18, display_name="PO Status")

    non_proj_reserved_qty = TableColumn(PlanMaxLines.non_proj_reserved_qty, order=19, display_name="Reserved Quantity")

    # po_uom = TableColumn(PlanMaxLines.po_uom, order=27, display_name="PO UOM")
    # po_doc_qty = TableColumn(PlanMaxLines.po_doc_qty, order=28, display_name="PO Doc Quantity")
    # pending_po_qty = TableColumn(PlanMaxLines.pending_po_qty, order=29, display_name="PO Pending Quantity")
    # qty_inspected = TableColumn(PlanMaxLines.qty_inspected, order=30, display_name="PO Inspected Quantity")
    # po_received_qty = TableColumn(PlanMaxLines.po_received_qty, order=31, display_name="PO Received Quantity")
    # completed_supply_qty = TableColumn(PlanMaxLines.completed_supply_qty, order=32, display_name="Completed Supply Quantity")
    # buyer_code = TableColumn(PlanMaxLines.buyer_code, order=33, display_name="PO Buyer Code")
    # receipt_qty = TableColumn(PlanMaxLines.receipt_qty, order=34, display_name="PO Receipt Quantity")
    # po_approval_date = TableColumn(PlanMaxLines.po_approval_date, order=35, display_name="PO Approval Date")
    # item_req_date_opseq = TableColumn(PlanMaxLines.item_req_date_opseq, order=36, display_name="Item Requisition Date Op Seq")


    task_name = TableColumn(PlanMaxLines.task_name, order=20, display_name="Task Name")
    system_line_status = TableColumn(PlanMaxLines.system_line_status, order=21, display_name="Line Status")
