from efficieno.old_components.components.table_views.base import TableView
from efficieno.old_components.components.table_views.columns import TableColumn
from demo_project.ontology.planmax_wip_details import PlanMaxWipDetails


class WipDetailPlan(TableView):
    table_header = "Plan Max WIP Detail Plan"
    table_description = "PLan Max WIP Detail Plan"

    organization_code = TableColumn(PlanMaxWipDetails.organization_code, order=1, display_name="Organization Code")
    project_number = TableColumn(PlanMaxWipDetails.project_number, order=2, display_name="Project Number")
    task_number = TableColumn(PlanMaxWipDetails.task_number, order=3, display_name="Task Number")
    wip_entity_name = TableColumn(PlanMaxWipDetails.wip_entity_name, order=4, display_name="WIP Job Name")
    wip_entity_id = TableColumn(PlanMaxWipDetails.wip_entity_id, order=5, display_name="WIP Entity ID")
    # wip_entity_id = OneToMany(database_column_name="wip_entity_id", relation_table_cols=PlanMaxLines.wip_job_id, order=5)
    wip_job_type = TableColumn(PlanMaxWipDetails.wip_job_type, order=6, display_name="WIP Job Type")
    wip_job_class = TableColumn(PlanMaxWipDetails.wip_job_class, order=7, display_name="WIP Job Class")
    wip_job_status = TableColumn(PlanMaxWipDetails.wip_job_status, order=8, display_name="WIP Job Status")
    wip_job_qty = TableColumn(PlanMaxWipDetails.wip_job_qty, order=9, display_name="WIP Job Qty")
    assembly_item = TableColumn(PlanMaxWipDetails.assembly_item, order=10, display_name="Assembly Item")

    component_item = TableColumn(PlanMaxWipDetails.component_item, order=11, display_name="Component Item")
    component_description = TableColumn(PlanMaxWipDetails.component_description, order=12, display_name="Component Description")
    item_type = TableColumn(PlanMaxWipDetails.item_type, order=13, display_name="Item Type")
    primary_uom_code = TableColumn(PlanMaxWipDetails.primary_uom_code, order=14, display_name="Primary UOM Code")
    department_id = TableColumn(PlanMaxWipDetails.department_id, order=15, display_name="Sales Department ID")
    operation_seq_num = TableColumn(PlanMaxWipDetails.operation_seq_num, order=16, display_name="Operation Seq No")
    required_quantity = TableColumn(PlanMaxWipDetails.required_quantity, order=17, display_name="Quantity Required")
    quantity_issued = TableColumn(PlanMaxWipDetails.quantity_issued, order=18, display_name="Quantity Issued")
    quantity_pending = TableColumn(PlanMaxWipDetails.quantity_pending, order=19, display_name="Quantity Pending")
    component_reservation = TableColumn(PlanMaxWipDetails.component_reservation, order=20, display_name="Component Reservation")
    component_oh_proj_locator = TableColumn(PlanMaxWipDetails.component_oh_proj_locator, order=21, display_name="Component Onhand Proj loc")
    curr_proj_plan_dt = TableColumn(PlanMaxWipDetails.curr_proj_plan_dt, order=22, display_name="Curr Proj Plan Date")

    customer = TableColumn(PlanMaxWipDetails.customer, order=23, display_name="Customer")
    component_po = TableColumn(PlanMaxWipDetails.component_po, order=24, display_name="Component PO")
    component_pr = TableColumn(PlanMaxWipDetails.component_pr, order=25, display_name="Component PR")
    po_buyer = TableColumn(PlanMaxWipDetails.po_buyer, order=26, display_name="PO Buyer")