from typing import TYPE_CHECKING
from sqlalchemy import Select
from sqlalchemy.orm import relationship

from efficieno.ontology.base import ObjectBase

from demo_project.data_objects.employee import Employee
from demo_project.data_views.department_view import DepartmentView


class EmployeeView(ObjectBase):
    __data_object_type__ = "data_view"
    __table__ = Select(Employee.empno, Employee.ename, Employee.job.label("Job"), Employee.deptno).subquery()
    # dept_number = column_property(Employee.deptno, Department.dept_no)

    view_name = "Employee View"
    view_description = "Employee View Desc"

    dept_no = Employee.deptno


EmployeeView.department_view_col = relationship(
    DepartmentView,
    primaryjoin=EmployeeView.dept_no == DepartmentView.dept_no,
    foreign_keys=EmployeeView.dept_no,
    # remote_side="DepartmentView.dept_number",
    viewonly=True,
)

DepartmentView.employee_view_col = relationship(
    EmployeeView,
    primaryjoin=DepartmentView.dept_no == EmployeeView.dept_no,
    foreign_keys=DepartmentView.dept_no,
    # remote_side="EmployeeView.dept_number",
    viewonly=True,
)
