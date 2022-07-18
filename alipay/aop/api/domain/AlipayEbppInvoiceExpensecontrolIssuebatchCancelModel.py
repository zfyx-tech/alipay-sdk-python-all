#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceExpensecontrolIssuebatchCancelModel(object):

    def __init__(self):
        self._enterprise_id = None
        self._institution_id = None
        self._issue_batch_id = None

    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def institution_id(self):
        return self._institution_id

    @institution_id.setter
    def institution_id(self, value):
        self._institution_id = value
    @property
    def issue_batch_id(self):
        return self._issue_batch_id

    @issue_batch_id.setter
    def issue_batch_id(self, value):
        self._issue_batch_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.institution_id:
            if hasattr(self.institution_id, 'to_alipay_dict'):
                params['institution_id'] = self.institution_id.to_alipay_dict()
            else:
                params['institution_id'] = self.institution_id
        if self.issue_batch_id:
            if hasattr(self.issue_batch_id, 'to_alipay_dict'):
                params['issue_batch_id'] = self.issue_batch_id.to_alipay_dict()
            else:
                params['issue_batch_id'] = self.issue_batch_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceExpensecontrolIssuebatchCancelModel()
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'institution_id' in d:
            o.institution_id = d['institution_id']
        if 'issue_batch_id' in d:
            o.issue_batch_id = d['issue_batch_id']
        return o


