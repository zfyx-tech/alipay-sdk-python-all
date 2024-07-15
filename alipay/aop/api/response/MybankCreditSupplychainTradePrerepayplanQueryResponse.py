#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InstallmentRepayPlanVO import InstallmentRepayPlanVO


class MybankCreditSupplychainTradePrerepayplanQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainTradePrerepayplanQueryResponse, self).__init__()
        self._installment_repay_plans = None
        self._ip_id = None
        self._ip_role_id = None
        self._out_order_no = None
        self._sale_pd_code = None

    @property
    def installment_repay_plans(self):
        return self._installment_repay_plans

    @installment_repay_plans.setter
    def installment_repay_plans(self, value):
        if isinstance(value, list):
            self._installment_repay_plans = list()
            for i in value:
                if isinstance(i, InstallmentRepayPlanVO):
                    self._installment_repay_plans.append(i)
                else:
                    self._installment_repay_plans.append(InstallmentRepayPlanVO.from_alipay_dict(i))
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def sale_pd_code(self):
        return self._sale_pd_code

    @sale_pd_code.setter
    def sale_pd_code(self, value):
        self._sale_pd_code = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainTradePrerepayplanQueryResponse, self).parse_response_content(response_content)
        if 'installment_repay_plans' in response:
            self.installment_repay_plans = response['installment_repay_plans']
        if 'ip_id' in response:
            self.ip_id = response['ip_id']
        if 'ip_role_id' in response:
            self.ip_role_id = response['ip_role_id']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'sale_pd_code' in response:
            self.sale_pd_code = response['sale_pd_code']
