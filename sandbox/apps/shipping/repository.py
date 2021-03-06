from decimal import Decimal as D

from izi.apps.shipping.methods import FixedPrice, NoShippingRequired
from izi.apps.shipping.repository import Repository as CoreRepository

# Dummy shipping methods
method1 = FixedPrice(charge_excl_tax=D('10.00'), charge_incl_tax=D('10.00'))
method1.code = 'method1'
method1.description = 'Ship by van'

method2 = FixedPrice(charge_excl_tax=D('20.00'), charge_incl_tax=D('20.00'))
method2.code = 'method2'
method2.description = 'Ship by boat'


class Repository(CoreRepository):
    methods = (method1, method2,)
