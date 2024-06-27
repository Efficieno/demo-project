from efficieno.old_ontologies.ontologyv3.base import Ontology
from efficieno.old_ontologies.ontologyv3.columns import Column, ManyToOne, OneToMany


class PlanMaxWipDetails(Ontology):
    database_table_name = "xxplan_max_wip_dtls_view"

    insert_allowed = False
    update_allowed = False
    delete_allowed = False

    organization_code = Column(database_column_name="organization_code", order=1)
    project_number = Column(database_column_name="project_number", order=2)
    task_number = Column(database_column_name="task_number", order=3)
    wip_entity_name = Column(database_column_name="wip_entity_name", order=4)
    wip_entity_id = Column(database_column_name="wip_entity_id", order=5)
    # wip_entity_id = OneToMany(database_column_name="wip_entity_id", relation_table_cols=PlanMaxLines.wip_job_id, order=5)
    wip_job_type = Column(database_column_name="wip_job_type", order=6)
    wip_job_class = Column(database_column_name="wip_job_class", order=7)
    wip_job_status = Column(database_column_name="wip_job_status", order=8)
    wip_job_qty = Column(database_column_name="wip_job_qty", order=9)
    assembly_item = Column(database_column_name="assembly_item", order=10)

    component_item = Column(database_column_name="component_item", order=11)
    component_description = Column(database_column_name="component_description", order=12)
    item_type = Column(database_column_name="item_type", order=13)
    primary_uom_code = Column(database_column_name="primary_uom_code", order=14)
    department_id = Column(database_column_name="department_id", order=15)
    operation_seq_num = Column(database_column_name="operation_seq_num", order=16)
    required_quantity = Column(database_column_name="required_quantity", order=17)
    quantity_issued = Column(database_column_name="quantity_issued", order=18)
    quantity_pending = Column(database_column_name="quantity_pending", order=19)
    component_reservation = Column(database_column_name="component_reservation", order=20)
    component_oh_proj_locator = Column(database_column_name="component_oh_proj_locator", order=21)
    curr_proj_plan_dt = Column(database_column_name="curr_proj_plan_dt", order=22)

    customer = Column(database_column_name="customer", order=23)
    component_po = Column(database_column_name="component_po", order=24)
    component_pr = Column(database_column_name="component_pr", order=25)
    po_buyer = Column(database_column_name="po_buyer", order=26)

    @classmethod
    def insert(cls, record: dict):
        pass

    @classmethod
    def update(cls, old_record: dict, updated_columns: list):
        pass

    @classmethod
    def delete(cls, record: dict):
        pass
