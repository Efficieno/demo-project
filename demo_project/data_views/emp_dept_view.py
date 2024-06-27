from typing import TYPE_CHECKING
from sqlalchemy import Select
from sqlalchemy.orm import relationship

from efficieno.ontology.base import ObjectBase

from demo_project.data_objects.employee import Employee
from demo_project.data_objects.department import Department


class EmployeeDept(ObjectBase):
    __data_object_type__ = "data_view"
    __table__ = (
        Select(
            Employee.empno.label("Employee Number"),
            Employee.ename.label("Employee Name"),
            Employee.hiredate.label("Hire Date"),
            Employee.deptno,
            Department.dname.label("Department Name"),
        )
        .join(Department)
        .subquery()
    )

    view_name = "Emp Dept View"
    view_description = "Emp Dept View Desc"

    dept_num = Employee.deptno
