#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChannelPutPlanDetailDTO(object):

    def __init__(self):
        self._activity_page = None
        self._bill_way = None
        self._channel_id = None
        self._channel_name = None
        self._creator_id = None
        self._creator_name = None
        self._crowd_ids = None
        self._customize_page = None
        self._gmt_create = None
        self._gmt_modified = None
        self._gmt_plan_end = None
        self._gmt_plan_start = None
        self._id = None
        self._modifier_id = None
        self._modifier_name = None
        self._name = None
        self._page_type = None
        self._reject_reason = None
        self._status = None
        self._task_id = None
        self._task_name = None
        self._tenant_code = None

    @property
    def activity_page(self):
        return self._activity_page

    @activity_page.setter
    def activity_page(self, value):
        self._activity_page = value
    @property
    def bill_way(self):
        return self._bill_way

    @bill_way.setter
    def bill_way(self, value):
        self._bill_way = value
    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
    @property
    def channel_name(self):
        return self._channel_name

    @channel_name.setter
    def channel_name(self, value):
        self._channel_name = value
    @property
    def creator_id(self):
        return self._creator_id

    @creator_id.setter
    def creator_id(self, value):
        self._creator_id = value
    @property
    def creator_name(self):
        return self._creator_name

    @creator_name.setter
    def creator_name(self, value):
        self._creator_name = value
    @property
    def crowd_ids(self):
        return self._crowd_ids

    @crowd_ids.setter
    def crowd_ids(self, value):
        if isinstance(value, list):
            self._crowd_ids = list()
            for i in value:
                self._crowd_ids.append(i)
    @property
    def customize_page(self):
        return self._customize_page

    @customize_page.setter
    def customize_page(self, value):
        self._customize_page = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def gmt_plan_end(self):
        return self._gmt_plan_end

    @gmt_plan_end.setter
    def gmt_plan_end(self, value):
        self._gmt_plan_end = value
    @property
    def gmt_plan_start(self):
        return self._gmt_plan_start

    @gmt_plan_start.setter
    def gmt_plan_start(self, value):
        self._gmt_plan_start = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def modifier_id(self):
        return self._modifier_id

    @modifier_id.setter
    def modifier_id(self, value):
        self._modifier_id = value
    @property
    def modifier_name(self):
        return self._modifier_name

    @modifier_name.setter
    def modifier_name(self, value):
        self._modifier_name = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def page_type(self):
        return self._page_type

    @page_type.setter
    def page_type(self, value):
        self._page_type = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def task_name(self):
        return self._task_name

    @task_name.setter
    def task_name(self, value):
        self._task_name = value
    @property
    def tenant_code(self):
        return self._tenant_code

    @tenant_code.setter
    def tenant_code(self, value):
        self._tenant_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_page:
            if hasattr(self.activity_page, 'to_alipay_dict'):
                params['activity_page'] = self.activity_page.to_alipay_dict()
            else:
                params['activity_page'] = self.activity_page
        if self.bill_way:
            if hasattr(self.bill_way, 'to_alipay_dict'):
                params['bill_way'] = self.bill_way.to_alipay_dict()
            else:
                params['bill_way'] = self.bill_way
        if self.channel_id:
            if hasattr(self.channel_id, 'to_alipay_dict'):
                params['channel_id'] = self.channel_id.to_alipay_dict()
            else:
                params['channel_id'] = self.channel_id
        if self.channel_name:
            if hasattr(self.channel_name, 'to_alipay_dict'):
                params['channel_name'] = self.channel_name.to_alipay_dict()
            else:
                params['channel_name'] = self.channel_name
        if self.creator_id:
            if hasattr(self.creator_id, 'to_alipay_dict'):
                params['creator_id'] = self.creator_id.to_alipay_dict()
            else:
                params['creator_id'] = self.creator_id
        if self.creator_name:
            if hasattr(self.creator_name, 'to_alipay_dict'):
                params['creator_name'] = self.creator_name.to_alipay_dict()
            else:
                params['creator_name'] = self.creator_name
        if self.crowd_ids:
            if isinstance(self.crowd_ids, list):
                for i in range(0, len(self.crowd_ids)):
                    element = self.crowd_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.crowd_ids[i] = element.to_alipay_dict()
            if hasattr(self.crowd_ids, 'to_alipay_dict'):
                params['crowd_ids'] = self.crowd_ids.to_alipay_dict()
            else:
                params['crowd_ids'] = self.crowd_ids
        if self.customize_page:
            if hasattr(self.customize_page, 'to_alipay_dict'):
                params['customize_page'] = self.customize_page.to_alipay_dict()
            else:
                params['customize_page'] = self.customize_page
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.gmt_plan_end:
            if hasattr(self.gmt_plan_end, 'to_alipay_dict'):
                params['gmt_plan_end'] = self.gmt_plan_end.to_alipay_dict()
            else:
                params['gmt_plan_end'] = self.gmt_plan_end
        if self.gmt_plan_start:
            if hasattr(self.gmt_plan_start, 'to_alipay_dict'):
                params['gmt_plan_start'] = self.gmt_plan_start.to_alipay_dict()
            else:
                params['gmt_plan_start'] = self.gmt_plan_start
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.modifier_id:
            if hasattr(self.modifier_id, 'to_alipay_dict'):
                params['modifier_id'] = self.modifier_id.to_alipay_dict()
            else:
                params['modifier_id'] = self.modifier_id
        if self.modifier_name:
            if hasattr(self.modifier_name, 'to_alipay_dict'):
                params['modifier_name'] = self.modifier_name.to_alipay_dict()
            else:
                params['modifier_name'] = self.modifier_name
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.page_type:
            if hasattr(self.page_type, 'to_alipay_dict'):
                params['page_type'] = self.page_type.to_alipay_dict()
            else:
                params['page_type'] = self.page_type
        if self.reject_reason:
            if hasattr(self.reject_reason, 'to_alipay_dict'):
                params['reject_reason'] = self.reject_reason.to_alipay_dict()
            else:
                params['reject_reason'] = self.reject_reason
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.task_name:
            if hasattr(self.task_name, 'to_alipay_dict'):
                params['task_name'] = self.task_name.to_alipay_dict()
            else:
                params['task_name'] = self.task_name
        if self.tenant_code:
            if hasattr(self.tenant_code, 'to_alipay_dict'):
                params['tenant_code'] = self.tenant_code.to_alipay_dict()
            else:
                params['tenant_code'] = self.tenant_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChannelPutPlanDetailDTO()
        if 'activity_page' in d:
            o.activity_page = d['activity_page']
        if 'bill_way' in d:
            o.bill_way = d['bill_way']
        if 'channel_id' in d:
            o.channel_id = d['channel_id']
        if 'channel_name' in d:
            o.channel_name = d['channel_name']
        if 'creator_id' in d:
            o.creator_id = d['creator_id']
        if 'creator_name' in d:
            o.creator_name = d['creator_name']
        if 'crowd_ids' in d:
            o.crowd_ids = d['crowd_ids']
        if 'customize_page' in d:
            o.customize_page = d['customize_page']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'gmt_plan_end' in d:
            o.gmt_plan_end = d['gmt_plan_end']
        if 'gmt_plan_start' in d:
            o.gmt_plan_start = d['gmt_plan_start']
        if 'id' in d:
            o.id = d['id']
        if 'modifier_id' in d:
            o.modifier_id = d['modifier_id']
        if 'modifier_name' in d:
            o.modifier_name = d['modifier_name']
        if 'name' in d:
            o.name = d['name']
        if 'page_type' in d:
            o.page_type = d['page_type']
        if 'reject_reason' in d:
            o.reject_reason = d['reject_reason']
        if 'status' in d:
            o.status = d['status']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'task_name' in d:
            o.task_name = d['task_name']
        if 'tenant_code' in d:
            o.tenant_code = d['tenant_code']
        return o


