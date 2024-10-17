from efficieno.components.metric_objects import Metric
from sqlalchemy import Integer, Select, bindparam
from sqlalchemy import func

from demo_project.data_objects.ont.oe_order_headers_all import OeOrderHeadersAll


class DemoMetric(Metric):
    __metric_name__ = "Open Order Count"
    __metric_description__ = "Open Orders "

    __query__ = Select(OeOrderHeadersAll).filter(OeOrderHeadersAll.flow_status_code == 'BOOKED')
    metric_column = func.count(OeOrderHeadersAll.header_id)
    table_columns = (OeOrderHeadersAll.header_id, OeOrderHeadersAll.order_number, OeOrderHeadersAll.flow_status_code)