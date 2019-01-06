import django_tables2 as tables
from django_tables2.utils import A
from . models import WebApp


class WebAppTable(tables.Table):
    id = tables.LinkColumn(verbose_name='ID')

    class Meta:
        model = WebApp
        sequence = ('id', )
        attrs = {"class": "table table-responsive table-hover"}
