from typing import TYPE_CHECKING
from sqlalchemy import Select
from sqlalchemy.orm import relationship

from efficieno.ontology.base import ObjectBase

from demo_project.data_objects.department import Department


class DepartmentView(ObjectBase):
    __data_object_type__ = "data_view"
    __table__ = Select(Department.deptno, Department.dname, Department.loc).subquery()

    view_name = "Department View"
    view_description = "Department View Desc"

    # dept_number = column_property(Employee.deptno, Department.dept_no)
    dept_no = Department.deptno

