from efficieno.components.charts_object import Chart
from sqlalchemy import Integer, Select, bindparam
from sqlalchemy import func

from demo_project.data_objects.ont.oe_order_headers_all import OeOrderHeadersAll


class DemoChart(Chart):

    __chart_name__ = "Demo Chart"
    __chart_description__ = "Demo Chart Desc"

    chart_config = {
        "title": [
            {
                "show": True,
                "text": "Open Jobs by Status",
                "subtext": "Open orders",
            }
        ],
        "series": [
            {
                "type": "bar",
                "name": "Items",
                "label": {"show": True, "margin": 8},
            }
        ],
        "tooltip": {
            "show": True,
        },
        "xAxis": {"type": "category"},
        "yAxis": {},
    }

    # __query__ = Select(OeOrderHeadersAll).filter(OeOrderHeadersAll.flow_status_code == 'BOOKED')
    __query__ = Select(OeOrderHeadersAll)
    __chart_selection__ = (OeOrderHeadersAll.flow_status_code, func.count(OeOrderHeadersAll.header_id))
    __chart_group_by__ = [OeOrderHeadersAll.flow_status_code]
    table_columns = [OeOrderHeadersAll.order_number, OeOrderHeadersAll.booked_date, OeOrderHeadersAll.flow_status_code]