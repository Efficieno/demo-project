from efficieno.components.dashboard_objects import PanelComponent, Dashboard


class Test(Dashboard):
    __dashboard_name__ = "test"
    __dashboard_description__ = "test"

    __grid_root_element__ = {'type': 'branch', 'data': [{'type': 'branch', 'data': [{'type': 'leaf', 'data': {'views': ['metrics_kQwa4HqAkZ'], 'activeView': 'metrics_kQwa4HqAkZ', 'id': '1'}, 'size': 889}, {'type': 'leaf', 'data': {'views': ['tables_dFlPszmSDg'], 'activeView': 'tables_dFlPszmSDg', 'id': '2'}, 'size': 889.296875}], 'size': 244}, {'type': 'leaf', 'data': {'views': ['panel_SrQ6YWB5ry'], 'activeView': 'panel_SrQ6YWB5ry', 'id': '3'}, 'size': 244.921875}], 'size': 1778.296875}
    __grid_width__ = 1778.296875
    __grid_height__ = 488.921875
    __grid_orientation__ = "VERTICAL"
    __active_group__ = 2

    metrics_kQwa4HqAkZ = PanelComponent(component_type="metrics",
                          name="DemoMetric",
                          query="Select(func.count(OeOrderHeadersAll.header_id).label('HeaderID'))",
                          data_objects={'OeOrderHeadersAll': 'demo_project.data_objects.ont.oe_order_headers_all'},
                          header="DemoMetric",
                          description="DemoMetricDesc",
                          columns=[],
                          content_component="mediator")
    tables_dFlPszmSDg = PanelComponent(component_type="tables",
                          name="DemoTable",
                          query="Select(OeOrderHeadersAll.header_id,OeOrderHeadersAll.order_number,OeOrderHeadersAll.ordered_date)",
                          data_objects={'OeOrderHeadersAll': 'demo_project.data_objects.ont.oe_order_headers_all'},
                          header="DemoTable",
                          description="DemoTableDesc",
                          columns=[{'accessorKey': 'header_id', 'autoincrement': None, 'dataObject': None, 'dataType': 'Integer', 'databaseTableName': None, 'databaseTableSchema': None, 'dbDataType': 'Integer', 'displayName': 'HeaderID', 'function': 'header_id', 'name': 'header_id', 'nullable': None, 'primaryKey': True, 'unique': None, 'visible': False}, {'accessorKey': 'order_number', 'autoincrement': None, 'dataObject': None, 'dataType': 'Integer', 'databaseTableName': None, 'databaseTableSchema': None, 'dbDataType': 'Integer', 'displayName': None, 'function': 'order_number', 'name': 'order_number', 'nullable': None, 'primaryKey': False, 'unique': None, 'visible': True}, {'accessorKey': 'ordered_date', 'autoincrement': None, 'dataObject': None, 'dataType': 'Date', 'databaseTableName': None, 'databaseTableSchema': None, 'dbDataType': 'Date', 'displayName': None, 'function': 'ordered_date', 'name': 'ordered_date', 'nullable': None, 'primaryKey': False, 'unique': None, 'visible': True}],
                          content_component="mediator")
    panel_SrQ6YWB5ry = PanelComponent(component_type="metrics",
                          name="Panel 3",
                          query="Select(func.count(EmpDept.emp_no).label('Count Employees'))",
                          data_objects={'EmpDept': 'efficieno.experiment.demo_ontology_layer'},
                          header="Demo Metric Header",
                          description="Demo Metric Description",
                          columns=[],
                          content_component="default")
