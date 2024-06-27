from efficieno.old_ontologies.ontologyv3.base import Ontology
from efficieno.old_ontologies.ontologyv3.columns import Column, ManyToOne
from demo_project.ontology.department import Department


class Employee(Ontology):
    database_table_name = "scott.emp"

    insert_allowed = False
    update_allowed = True
    delete_allowed = False

    emp_id = Column(database_column_name="empno", data_type="Integer", column_description="Employee Number", order=1)
    emp_name = Column(database_column_name="ename", data_type="String", column_description="Employee Name", order=2)
    job = Column(database_column_name="job", data_type="String", column_description="Job", order=3)
    manager = Column(database_column_name="mgr", data_type="Integer", column_description="Manager", order=4)
    hire_date = Column(database_column_name="hiredate", data_type="TimeStamp", column_description="Hire Date")
    salary = Column(database_column_name="sal", data_type="Integer", column_description="Salary", editable=True)
    comm = Column(database_column_name="comm", data_type="Integer", column_description="Comm", editable=True)
    dept_no = ManyToOne(database_column_name="deptno", relation_table_cols=Department.dept_id, column_description="Department Number")

    @classmethod
    def insert(cls, record: dict):
        pass

    @classmethod
    def update(cls, old_record: dict, updated_columns: list):
        pass

    @classmethod
    def delete(cls, record: dict):
        pass
