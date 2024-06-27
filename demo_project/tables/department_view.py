from efficieno.old_components.components.table_views.base import TableView
from efficieno.old_components.components.table_views.columns import TableColumn
from demo_project.ontology.department import Department
from demo_project.ontology.employee import Employee

class DepartmentView(TableView):
    table_header = "Department Details"
    table_description = "Department Description"

    dept_id = TableColumn(Department.dept_id, display_name="Department ID", order=1)
    dept_name = TableColumn(Department.dept_name, display_name="Department Name", order=2)
    dept_location = TableColumn(Department.dept_location, display_name="Department Location", order=3)
