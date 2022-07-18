#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessRelationShopTradeDetailInfo(object):

    def __init__(self):
        self._gmt_payment = None
        self._trade_amount = None

    @property
    def gmt_payment(self):
        return self._gmt_payment

    @gmt_payment.setter
    def gmt_payment(self, value):
        self._gmt_payment = value
    @property
    def trade_amount(self):
        return self._trade_amount

    @trade_amount.setter
    def trade_amount(self, value):
        self._trade_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_payment:
            if hasattr(self.gmt_payment, 'to_alipay_dict'):
                params['gmt_payment'] = self.gmt_payment.to_alipay_dict()
            else:
                params['gmt_payment'] = self.gmt_payment
        if self.trade_amount:
            if hasattr(self.trade_amount, 'to_alipay_dict'):
                params['trade_amount'] = self.trade_amount.to_alipay_dict()
            else:
                params['trade_amount'] = self.trade_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessRelationShopTradeDetailInfo()
        if 'gmt_payment' in d:
            o.gmt_payment = d['gmt_payment']
        if 'trade_amount' in d:
            o.trade_amount = d['trade_amount']
        return o


