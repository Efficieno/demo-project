from efficieno.old_ontologies.ontologyv3.base import Ontology
from efficieno.old_ontologies.ontologyv3.columns import Column, ManyToOne


class Department(Ontology):
    database_table_name = "scott.dept"

    insert_allowed = False
    update_allowed = False
    delete_allowed = False

    dept_id = Column(database_column_name="deptno", data_type="Integer", column_description="Department ID", order=1)
    dept_name = Column(database_column_name="dname", data_type="String", column_description="Department Name", order=2)
    dept_location = Column(database_column_name="loc", data_type="Integer", column_description="Department Location", order=3)

    @classmethod
    def insert(cls, record: dict):
        pass

    @classmethod
    def update(cls, old_record: dict, updated_columns: list):
        pass

    @classmethod
    def delete(cls, record: dict):
        pass
