from efficieno.old_components.components.table_views.base import TableView
from efficieno.old_components.components.table_views.columns import TableColumn
from demo_project.ontology.department import Department
from demo_project.ontology.employee import Employee


class EmployeeDepartmentView(TableView):
    table_header = "Employee Department Details"
    table_description = "Employee Department Description"

    emp_id = TableColumn(Employee.emp_id, display_name="Employee ID", order=1)
    salary = TableColumn(Employee.salary, display_name="Employee Salary", order=2)
    comm = TableColumn(Employee.comm, display_name="Employee Comm", order=3)
    dept_name = TableColumn(Department.dept_name, display_name="Dept name", order=4)
    dept_location = TableColumn(Department.dept_location, display_name="Dept Location", order=5)
