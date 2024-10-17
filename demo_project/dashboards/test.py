from efficieno.components.dashboard_objects import PanelComponent, Dashboard


class Test(Dashboard):
    __dashboard_name__ = "test"
    __dashboard_description__ = "test desc"

    __grid_root_element__ = {'type': 'branch', 'data': [{'type': 'leaf', 'data': {'views': ['metrics-aYDu6rKw0'], 'activeView': 'metrics-aYDu6rKw0', 'id': '1'}, 'size': 183}, {'type': 'leaf', 'data': {'views': ['panel-AFP3xePe-_'], 'activeView': 'panel-AFP3xePe-_', 'id': '2'}, 'size': 183}, {'type': 'leaf', 'data': {'views': ['panel-hqaQcmw5bo'], 'activeView': 'panel-hqaQcmw5bo', 'id': '3'}, 'size': 184.375}], 'size': 1778.296875}
    __grid_width__ = 1778.296875
    __grid_height__ = 550.375
    __grid_orientation__ = "VERTICAL"
    __active_group__ = 1

    component_1 = PanelComponent(component_type="metrics",
                                 name="DemoMetrics",
                                 query="Select(func.count(EmpDept.emp_no).label('Count Employees'))",
                                 data_objects={"EmpDept": "efficieno.experiment.demo_ontology_layer"},
                                 header="Demo Metric Header",
                                 description="Demo Metric Description",
                                 columns=[])

    component_2 = PanelComponent(component_type="tables",
                                 name="DemoTable",
                                 query="Select(EmpDept.emp_no, EmpDept.emp_name)",
                                 data_objects={"EmpDept": "efficieno.experiment.demo_ontology_layer"},
                                 header="Demo Table Header",
                                 description="Demo Table Description",
                                 actions=[],
                                 inline_actions=None,
                                 columns=[
                                     {
                                         "accessorKey": "emp_no",
                                         "autoincrement": None,
                                         "dataObject": None,
                                         "dataType": "String",
                                         "databaseTableName": None,
                                         "databaseTableSchema": None,
                                         "dbDataType": "String",
                                         "displayName": "Emp No",
                                         "function": "emp_no",
                                         "name": "emp_no",
                                         "nullable": None,
                                         "primaryKey": True,
                                         "unique": None,
                                         "visible": False
                                     },
                                     {
                                         "accessorKey": "emp_name",
                                         "autoincrement": None,
                                         "dataObject": None,
                                         "dataType": "String",
                                         "databaseTableName": None,
                                         "databaseTableSchema": None,
                                         "dbDataType": "String",
                                         "displayName": "Emp Name",
                                         "function": "emp_name",
                                         "name": "emp_name",
                                         "nullable": None,
                                         "primaryKey": True,
                                         "unique": None,
                                         "visible": False
                                     }
                                 ])

    component_3 = PanelComponent(component_type="charts",
                                 name="DemoChart",
                                 query="Select(EmpDept.emp_no, EmpDept.emp_name)",
                                 data_objects={"EmpDept": "efficieno.experiment.demo_ontology_layer"},
                                 header="Demo Charts Header",
                                 description="Demo Charts Description",
                                 actions=[],
                                 inline_actions=None,
                                 columns=[],
                                 chart_options={
                                     "series": [
                                         {
                                             "label": {
                                                 "margin": 8,
                                                 "show": True
                                             },
                                             "name": "Items",
                                             "type": "bar"
                                         }
                                     ],
                                     "title": [
                                         {
                                             "show": True,
                                             "subtext": "Open orders",
                                             "text": "Open Jobs by Status"
                                         }
                                     ],
                                     "tooltip": {
                                         "show": True
                                     },
                                     "xAxis": {
                                         "type": "category"
                                     },
                                     "yAxis": {
                                     }
                                 })
