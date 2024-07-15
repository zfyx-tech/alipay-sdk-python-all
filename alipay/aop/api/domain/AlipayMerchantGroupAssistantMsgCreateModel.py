#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityAssistantMsgContentVO import ActivityAssistantMsgContentVO


class AlipayMerchantGroupAssistantMsgCreateModel(object):

    def __init__(self):
        self._activity_content = None
        self._biz_type = None
        self._gmt_published = None
        self._group_ids = None
        self._name = None

    @property
    def activity_content(self):
        return self._activity_content

    @activity_content.setter
    def activity_content(self, value):
        if isinstance(value, ActivityAssistantMsgContentVO):
            self._activity_content = value
        else:
            self._activity_content = ActivityAssistantMsgContentVO.from_alipay_dict(value)
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def gmt_published(self):
        return self._gmt_published

    @gmt_published.setter
    def gmt_published(self, value):
        self._gmt_published = value
    @property
    def group_ids(self):
        return self._group_ids

    @group_ids.setter
    def group_ids(self, value):
        if isinstance(value, list):
            self._group_ids = list()
            for i in value:
                self._group_ids.append(i)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_content:
            if hasattr(self.activity_content, 'to_alipay_dict'):
                params['activity_content'] = self.activity_content.to_alipay_dict()
            else:
                params['activity_content'] = self.activity_content
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.gmt_published:
            if hasattr(self.gmt_published, 'to_alipay_dict'):
                params['gmt_published'] = self.gmt_published.to_alipay_dict()
            else:
                params['gmt_published'] = self.gmt_published
        if self.group_ids:
            if isinstance(self.group_ids, list):
                for i in range(0, len(self.group_ids)):
                    element = self.group_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.group_ids[i] = element.to_alipay_dict()
            if hasattr(self.group_ids, 'to_alipay_dict'):
                params['group_ids'] = self.group_ids.to_alipay_dict()
            else:
                params['group_ids'] = self.group_ids
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantGroupAssistantMsgCreateModel()
        if 'activity_content' in d:
            o.activity_content = d['activity_content']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'gmt_published' in d:
            o.gmt_published = d['gmt_published']
        if 'group_ids' in d:
            o.group_ids = d['group_ids']
        if 'name' in d:
            o.name = d['name']
        return o


