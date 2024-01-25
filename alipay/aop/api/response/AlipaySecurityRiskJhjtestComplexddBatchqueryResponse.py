#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityRiskJhjtestComplexddBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityRiskJhjtestComplexddBatchqueryResponse, self).__init__()
        self._out_p = None

    @property
    def out_p(self):
        return self._out_p

    @out_p.setter
    def out_p(self, value):
        self._out_p = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityRiskJhjtestComplexddBatchqueryResponse, self).parse_response_content(response_content)
        if 'out_p' in response:
            self.out_p = response['out_p']
