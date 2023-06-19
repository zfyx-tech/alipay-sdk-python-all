#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudrunObjectstorageFilelistQueryModel(object):

    def __init__(self):
        self._env = None
        self._file_id_list = None
        self._next_token = None
        self._page_size = None
        self._prefix = None

    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value
    @property
    def file_id_list(self):
        return self._file_id_list

    @file_id_list.setter
    def file_id_list(self, value):
        if isinstance(value, list):
            self._file_id_list = list()
            for i in value:
                self._file_id_list.append(i)
    @property
    def next_token(self):
        return self._next_token

    @next_token.setter
    def next_token(self, value):
        self._next_token = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def prefix(self):
        return self._prefix

    @prefix.setter
    def prefix(self, value):
        self._prefix = value


    def to_alipay_dict(self):
        params = dict()
        if self.env:
            if hasattr(self.env, 'to_alipay_dict'):
                params['env'] = self.env.to_alipay_dict()
            else:
                params['env'] = self.env
        if self.file_id_list:
            if isinstance(self.file_id_list, list):
                for i in range(0, len(self.file_id_list)):
                    element = self.file_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.file_id_list[i] = element.to_alipay_dict()
            if hasattr(self.file_id_list, 'to_alipay_dict'):
                params['file_id_list'] = self.file_id_list.to_alipay_dict()
            else:
                params['file_id_list'] = self.file_id_list
        if self.next_token:
            if hasattr(self.next_token, 'to_alipay_dict'):
                params['next_token'] = self.next_token.to_alipay_dict()
            else:
                params['next_token'] = self.next_token
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.prefix:
            if hasattr(self.prefix, 'to_alipay_dict'):
                params['prefix'] = self.prefix.to_alipay_dict()
            else:
                params['prefix'] = self.prefix
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudrunObjectstorageFilelistQueryModel()
        if 'env' in d:
            o.env = d['env']
        if 'file_id_list' in d:
            o.file_id_list = d['file_id_list']
        if 'next_token' in d:
            o.next_token = d['next_token']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'prefix' in d:
            o.prefix = d['prefix']
        return o


