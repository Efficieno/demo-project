from efficieno.components.dashboard_objects import PanelComponent, Dashboard


class DemoChart(Dashboard):
    __dashboard_name__ = "DemoChart"
    __dashboard_description__ = "Demo Dashboard"

    __grid_root_element__ = {'type': 'branch', 'data': [{'type': 'leaf', 'data': {'views': ['metrics_T_C_aiEmSy'], 'activeView': 'metrics_T_C_aiEmSy', 'id': '1'}, 'size': 260},
                                                        {'type': 'leaf', 'data': {'views': ['panel__NXT8QrunU'], 'activeView': 'panel__NXT8QrunU', 'id': '2'}, 'size': 260},
                                                        {'type': 'leaf', 'data': {'views': ['panel_SrQ6YWB5ry'], 'activeView': 'panel_SrQ6YWB5ry', 'id': '3'},
                                                         'size': 257.7833251953125},
                                                        {'type': 'leaf', 'data': {'views': ['tables_KH4MHFH66'], 'activeView': 'tables_KH4MHFH66', 'id': '4'}, 'size': 172.4375,
                                                         'visible': False}
                                                        ], 'size': 1787.949951171875}
    __grid_width__ = 1787.949951171875
    __grid_height__ = 777.7833251953125
    __grid_orientation__ = "VERTICAL"
    __active_group__ = 1

    metrics_T_C_aiEmSy = PanelComponent(component_type="metrics",
                                        name="Booked Orders",
                                        query="Select(func.count(OrderHeaders.header_id).label('count')).filter(OrderHeaders.flow_status_code == 'BOOKED')",
                                        data_objects={'OrderHeaders': 'demo_project.ontologies.order_headers'},
                                        header="Booked Orders",
                                        description="Booked Orders",
                                        columns=[],
                                        chart_options={},
                                        content_component="mediator",
                                        relations=[])
    panel__NXT8QrunU = PanelComponent(component_type="tables",
                                      name="Order Header Details",
                                      query="Select(OrderHeaders.header_id, OrderHeaders.organization_code, OrderHeaders.org_id, OrderHeaders.order_type_id, OrderHeaders.order_number, OrderHeaders.version_number).filter(OrderHeaders.flow_status_code == 'BOOKED')",
                                      data_objects={'OrderHeaders': 'demo_project.ontologies.order_headers'},
                                      header="Order Header Details",
                                      description="Order Header Details",
                                      columns=[{
                                          "accessor_key": "header_id",
                                          "autoincrement": "auto",
                                          "data_object": "OrderHeaders",
                                          "data_type": "Integer",
                                          "table_class": "OeOrderHeadersAll",
                                          "database_table_name": "oe_order_headers_all",
                                          "database_table_schema": "ont",
                                          "db_data_type": "INTEGER",
                                          "display_name": "header_id",
                                          "function": None,
                                          "id": "ont.oe_order_headers_all.header_id",
                                          "invisible": False,
                                          "name": "header_id",
                                          "nullable": False,
                                          "primary_key": True,
                                          "unique": None
                                      },
                                          {
                                              "accessor_key": "organization_code",
                                              "autoincrement": "auto",
                                              "data_object": "OrderHeaders",
                                              "data_type": "String",
                                              "table_class": "OrgOrganizationDefinitions",
                                              "database_table_name": "org_organization_definitions",
                                              "database_table_schema": "apps",
                                              "db_data_type": "VARCHAR",
                                              "display_name": "organization_code",
                                              "function": None,
                                              "id": "apps.org_organization_definitions.organization_code",
                                              "invisible": False,
                                              "name": "organization_code",
                                              "nullable": False,
                                              "primary_key": False,
                                              "unique": None
                                          },
                                          {
                                              "accessor_key": "org_id",
                                              "autoincrement": "auto",
                                              "data_object": "OrderHeaders",
                                              "data_type": "Integer",
                                              "table_class": "OeOrderHeadersAll",
                                              "database_table_name": "oe_order_headers_all",
                                              "database_table_schema": "ont",
                                              "db_data_type": "INTEGER",
                                              "display_name": "org_id",
                                              "function": None,
                                              "id": "ont.oe_order_headers_all.org_id",
                                              "invisible": False,
                                              "name": "org_id",
                                              "nullable": False,
                                              "primary_key": False,
                                              "unique": None
                                          },
                                          {
                                              "accessor_key": "order_type_id",
                                              "autoincrement": "auto",
                                              "data_object": "OrderHeaders",
                                              "data_type": "Integer",
                                              "table_class": "OeOrderHeadersAll",
                                              "database_table_name": "oe_order_headers_all",
                                              "database_table_schema": "ont",
                                              "db_data_type": "INTEGER",
                                              "display_name": "order_type_id",
                                              "function": None,
                                              "id": "ont.oe_order_headers_all.order_type_id",
                                              "invisible": False,
                                              "name": "order_type_id",
                                              "nullable": False,
                                              "primary_key": False,
                                              "unique": None
                                          },
                                          {
                                              "accessor_key": "order_number",
                                              "autoincrement": "auto",
                                              "data_object": "OrderHeaders",
                                              "data_type": "Integer",
                                              "table_class": "OeOrderHeadersAll",
                                              "database_table_name": "oe_order_headers_all",
                                              "database_table_schema": "ont",
                                              "db_data_type": "INTEGER",
                                              "display_name": "order_number",
                                              "function": None,
                                              "id": "ont.oe_order_headers_all.order_number",
                                              "invisible": False,
                                              "name": "order_number",
                                              "nullable": False,
                                              "primary_key": False,
                                              "unique": None
                                          },
                                          {
                                              "accessor_key": "version_number",
                                              "autoincrement": "auto",
                                              "data_object": "OrderHeaders",
                                              "data_type": "Integer",
                                              "table_class": "OeOrderHeadersAll",
                                              "database_table_name": "oe_order_headers_all",
                                              "database_table_schema": "ont",
                                              "db_data_type": "INTEGER",
                                              "display_name": "version_number",
                                              "function": None,
                                              "id": "ont.oe_order_headers_all.version_number",
                                              "invisible": False,
                                              "name": "version_number",
                                              "nullable": False,
                                              "primary_key": False,
                                              "unique": None
                                          }
                                      ],
                                      chart_options={},
                                      content_component="mediator",
                                      relations=[{"component_name": "tables_KH4MHFH66",
                                                  "relation_name": "Order Header Line details",
                                                  "relations": [{"source_class_name": "OeOrderHeadersAll",
                                                                 "source_column_name": "header_id",
                                                                 "destination_class_name": "OeOrderLinesAll",
                                                                 "destination_column_name": "header_id"}]
                                                  }])
    panel_SrQ6YWB5ry = PanelComponent(component_type="charts",
                                      name="Order Statuses",
                                      query="Select(OrderHeaders.flow_status_code, func.count(OrderHeaders.header_id).label('count')).group_by(OrderHeaders.flow_status_code)",
                                      data_objects={'OrderHeaders': 'demo_project.ontologies.order_headers'},
                                      header="Order Statuses",
                                      description="Order Statuses",
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
                                      },
                                      content_component="mediator",
                                      relations=[])

    tables_KH4MHFH66 = PanelComponent(component_type="tables",
                                      name="Order Line Details",
                                      query="Select(OrderLines.line_id, OrderLines.organization_code, OrderLines.segment1, OrderLines.line_number, OrderLines.ordered_item, OrderLines.header_id)",
                                      data_objects={'OrderLines': 'demo_project.ontologies.order_lines'},
                                      header="Order Line Details",
                                      description="Order Line Details",
                                      columns=[{
                                          "accessor_key": "line_id",
                                          "autoincrement": "auto",
                                          "data_object": "OrderLines",
                                          "data_type": "Integer",
                                          "table_class": "OeOrderLinesAll",
                                          "database_table_name": "oe_order_lines_all",
                                          "database_table_schema": "ont",
                                          "db_data_type": "INTEGER",
                                          "display_name": "line_id",
                                          "function": None,
                                          "id": "ont.oe_order_lines_all.line_id",
                                          "invisible": False,
                                          "name": "line_id",
                                          "nullable": False,
                                          "primary_key": True,
                                          "unique": None
                                      },
                                          {
                                              "accessor_key": "organization_code",
                                              "autoincrement": "auto",
                                              "data_object": "OrderLines",
                                              "data_type": "String",
                                              "table_class": "OrgOrganizationDefinitions",
                                              "database_table_name": "org_organization_definitions",
                                              "database_table_schema": "apps",
                                              "db_data_type": "VARCHAR",
                                              "display_name": "organization_code",
                                              "function": None,
                                              "id": "apps.org_organization_definitions.organization_code",
                                              "invisible": False,
                                              "name": "organization_code",
                                              "nullable": False,
                                              "primary_key": False,
                                              "unique": None
                                          },
                                          {
                                              "accessor_key": "segment1",
                                              "autoincrement": "auto",
                                              "data_object": "OrderLines",
                                              "data_type": "String",
                                              "table_class": "MtlSystemItemsB",
                                              "database_table_name": "mtl_system_items_b",
                                              "database_table_schema": "inv",
                                              "db_data_type": "VARCHAR",
                                              "display_name": "segment1",
                                              "function": None,
                                              "id": "inv.mtl_system_items_b.segment1",
                                              "invisible": False,
                                              "name": "segment1",
                                              "nullable": False,
                                              "primary_key": False,
                                              "unique": None
                                          },
                                          {
                                              "accessor_key": "line_number",
                                              "autoincrement": "auto",
                                              "data_object": "OrderLines",
                                              "data_type": "Integer",
                                              "table_class": "OeOrderLinesAll",
                                              "database_table_name": "oe_order_lines_all",
                                              "database_table_schema": "ont",
                                              "db_data_type": "INTEGER",
                                              "display_name": "line_number",
                                              "function": None,
                                              "id": "ont.oe_order_lines_all.line_number",
                                              "invisible": False,
                                              "name": "line_number",
                                              "nullable": False,
                                              "primary_key": False,
                                              "unique": None
                                          },
                                          {
                                              "accessor_key": "ordered_item",
                                              "autoincrement": "auto",
                                              "data_object": "OrderLines",
                                              "data_type": "String",
                                              "table_class": "OeOrderLinesAll",
                                              "database_table_name": "oe_order_lines_all",
                                              "database_table_schema": "ont",
                                              "db_data_type": "VARCHAR",
                                              "display_name": "ordered_item",
                                              "function": None,
                                              "id": "ont.oe_order_lines_all.ordered_item",
                                              "invisible": False,
                                              "name": "ordered_item",
                                              "nullable": False,
                                              "primary_key": False,
                                              "unique": None
                                          },
                                          {
                                              "accessor_key": "header_id",
                                              "autoincrement": "auto",
                                              "data_object": "OrderLines",
                                              "data_type": "Integer",
                                              "table_class": "OeOrderLinesAll",
                                              "database_table_name": "oe_order_lines_all",
                                              "database_table_schema": "ont",
                                              "db_data_type": "INTEGER",
                                              "display_name": "header_id",
                                              "function": None,
                                              "id": "ont.oe_order_lines_all.header_id",
                                              "invisible": True,
                                              "name": "header_id",
                                              "nullable": False,
                                              "primary_key": False,
                                              "unique": None
                                          }
                                      ],
                                      chart_options={},
                                      content_component="mediator",
                                      relations=[])
