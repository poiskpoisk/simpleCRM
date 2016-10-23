# -*- coding: utf-8 -*-#
__author__ = 'AMA'

import django_tables2 as tables
from .models import SalesPerson, Todo, Customer, Deal
from django.utils.translation import ugettext as _
from django_tables2.utils import A  # alias for Accessor


class SalesPersonTable(tables.Table):
    email = tables.Column()
    id = tables.LinkColumn('salespersonpage', args=[A('pk')])

    class Meta:
        model = SalesPerson
        exclude = ('avatar',)
        attrs = {'class': 'paleblue table table-striped table-bordered'}  # add class="paleblue" to <table> tag
        empty_text = _(
            'Пока нет ни одного менеджера по продажам. Для добавления используйте соответствующий пункт меню')


class ToDosTable(tables.Table):
    id = tables.LinkColumn('todopage', args=[A('pk')])

    class Meta:
        model = Todo
        attrs = {'class': 'paleblue table table-striped table-bordered'}
        empty_text = _(
            'Пока нет ни одного запланированного дела. Для добавления используйте соответствующий пункт меню')


class CustomersTable(tables.Table):
    id = tables.LinkColumn('customerpage', args=[A('pk')])

    class Meta:
        model = Customer
        exclude = ('avatar', 'comment')
        attrs = {'class': 'paleblue table table-striped table-bordered'}
        empty_text = _('Пока нет ни одного клиента. Для добавления используйте соответствующий пункт меню')


class DealsTable(tables.Table):
    id = tables.LinkColumn('dealpage', args=[A('pk')])
    deal_data = tables.DateTimeColumn(format="d/m/Y")
    deal_time = tables.DateTimeColumn(format="H.i")

    class Meta:
        model = Deal
        attrs = {'class': 'paleblue table table-striped table-bordered'}
        empty_text = _('Пока нет ни одной сделки. Для добавления используйте соответствующий пункт меню')
