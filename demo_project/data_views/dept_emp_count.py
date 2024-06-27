from typing import TYPE_CHECKING
from sqlalchemy import Select
from sqlalchemy.orm import relationship
from sqlalchemy import func

from efficieno.ontology.base import ObjectBase

from demo_project.data_objects.employee import Employee
from demo_project.data_objects.department import Department
from demo_project.data_views.emp_dept_view import EmployeeDept


class DeptEmpCount(ObjectBase):
    __data_object_type__ = "data_view"
    __table__ = Select(
        Department.deptno,
        Department.dname.label("Department Name"),
        Department.loc.label("Department Location"),
        Select(func.count(Employee.empno)).where(Employee.deptno == Department.deptno).label("Employee Count"),
    ).subquery()

    view_name = "Dept Emp View"
    view_description = "Dept Emp View Desc"

    dept_num = Department.deptno


EmployeeDept.emp_department_view_col = relationship(
    DeptEmpCount,
    primaryjoin=EmployeeDept.dept_num == DeptEmpCount.dept_num,
    foreign_keys=EmployeeDept.dept_num,
    # remote_side="DepartmentView.dept_number",
    viewonly=True,
)

DeptEmpCount.dept_employee_view_col = relationship(
    EmployeeDept,
    primaryjoin=DeptEmpCount.dept_num == EmployeeDept.dept_num,
    foreign_keys=DeptEmpCount.dept_num,
    # foreign_keys="Department.deptno",
    # remote_side="Department.deptno",
    viewonly=True,
)
