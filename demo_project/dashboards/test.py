from efficieno.components.dashboard_objects import PanelComponent, Dashboard


class Test(Dashboard):
    __dashboard_name__ = "test"
    __dashboard_description__ = "test"

    __grid_root_element__ = {'type': 'branch', 'data': [{'type': 'leaf', 'data': {'views': ['metrics_ks7wh8J1Y'], 'activeView': 'metrics_ks7wh8J1Y', 'id': '1'}, 'size': 182}, {'type': 'leaf', 'data': {'views': ['panel__NXT8QrunU'], 'activeView': 'panel__NXT8QrunU', 'id': '2'}, 'size': 182}, {'type': 'leaf', 'data': {'views': ['panel_SrQ6YWB5ry'], 'activeView': 'panel_SrQ6YWB5ry', 'id': '3'}, 'size': 181.984375}], 'size': 1778.296875}
    __grid_width__ = 1778.296875
    __grid_height__ = 545.984375
    __grid_orientation__ = "VERTICAL"
    __active_group__ = 1

    metrics_ks7wh8J1Y = PanelComponent(component_type="metrics",
                          name="DemoMetric",
                          query="Select(func.count(OeOrderHeadersAll.header_id).label('HeaderID'))",
                          data_objects={'OeOrderHeadersAll': 'demo_project.data_objects.ont.oe_order_headers_all'},
                          header="DemoMetric",
                          description="DemoMetricDesc",
                          columns=[],
                          content_component="mediator")
    panel__NXT8QrunU = PanelComponent(component_type="metrics",
                          name="DemoMetrics",
                          query="Select(func.count(EmpDept.emp_no).label('Count Employees'))",
                          data_objects={'EmpDept': 'efficieno.experiment.demo_ontology_layer'},
                          header="Demo Metric Header",
                          description="Demo Metric Description",
                          columns=[],
                          content_component="default")
    panel_SrQ6YWB5ry = PanelComponent(component_type="metrics",
                          name="DemoMetrics",
                          query="Select(func.count(EmpDept.emp_no).label('Count Employees'))",
                          data_objects={'EmpDept': 'efficieno.experiment.demo_ontology_layer'},
                          header="Demo Metric Header",
                          description="Demo Metric Description",
                          columns=[],
                          content_component="default")
