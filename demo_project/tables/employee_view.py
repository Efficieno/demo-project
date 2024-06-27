from efficieno.old_components.components.table_views.base import TableView
from efficieno.old_components.components.table_views.columns import TableColumn
from demo_project.ontology.department import Department
from demo_project.ontology.employee import Employee


class EmployeeView(TableView):
    table_header = "Employee View"
    table_description = "Employee Details"

    emp_id = TableColumn(Employee.emp_id, display_name="Employee ID", order=1)
    salary = TableColumn(Employee.salary, display_name="Employee Salary", order=2)
    comm = TableColumn(Employee.comm, display_name="Employee Comm", order=3)
    dept_no = TableColumn(Employee.dept_no, display_name="Employee Dept No", order=4)
