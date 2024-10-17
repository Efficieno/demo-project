from efficieno.components.dashboard_objects import PanelComponent, Dashboard


class Test(Dashboard):
    __dashboard_name__ = "test"
    __dashboard_description__ = "test"

    __grid_root_element__ = {'type': 'branch', 'data': [{'type': 'leaf', 'data': {'views': ['panel_IP1_fhJ_R'], 'activeView': 'panel_IP1_fhJ_R', 'id': '1'}, 'size': 259}, {'type': 'leaf', 'data': {'views': ['panel__NXT8QrunU'], 'activeView': 'panel__NXT8QrunU', 'id': '2'}, 'size': 259}, {'type': 'leaf', 'data': {'views': ['panel_SrQ6YWB5ry'], 'activeView': 'panel_SrQ6YWB5ry', 'id': '3'}, 'size': 258.015625}], 'size': 1787.953125}
    __grid_width__ = 1787.953125
    __grid_height__ = 776.015625
    __grid_orientation__ = "VERTICAL"
    __active_group__ = 1

    panel_IP1_fhJ_R = PanelComponent(component_type="metrics",
                          name="DemoMetrics",
                          query="Select(func.count(EmpDept.emp_no).label('Count Employees'))",
                          data_objects={'EmpDept': 'efficieno.experiment.demo_ontology_layer'},
                          header="Demo Metric Header",
                          description="Demo Metric Description",
                          columns=[],
                          content_component="default")
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
