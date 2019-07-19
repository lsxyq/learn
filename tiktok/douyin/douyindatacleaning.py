#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import json

import arrow


class DataCleaning(object):
    def __init__(self, path):
        self.path = path
        self._raw_data = {}
        self._author_info = {}
        self._aweme_list = []

    @property
    def author_info(self):
        """
        "uid": "63344375465",
        "short_id": "38350415",
        "nickname": "麒麟",
        "gender": 1,
        "signature": "成都理工大学 大二\nWB：猪是一个胖子\n麒麟的日常",
        :return:
        """
        if not self.raw_aweme_list:
            return self._author_info
        if self._author_info:
            return self._author_info
        data = self.raw_aweme_list[0]
        self._author_info = {
            'uid': data['author']['uid'],
            'short_id': data['author']['short_id'],
            'nickname': data['author']['nickname'],
            'signature': data['author']['signature'],
        }
        return self._author_info

    @property
    def author_nickname(self):
        return self.author_info.get('nickname')

    @property
    def raw_data(self):
        if self._raw_data:
            return self._raw_data
        f = open(self.path, 'r', encoding='utf8')
        data = f.read()
        f.close()
        self._raw_data = json.loads(data)
        return self._raw_data

    @property
    def raw_aweme_list(self):
        if not self.raw_data.get('aweme_list'):
            return []
        return self.raw_data.get('aweme_list')

    @property
    def cleaned_aweme_list(self):
        if self._aweme_list:
            return self._aweme_list
        _aweme_list = []
        for aweme_info in self.raw_aweme_list:
            video_info = {
                'nickname': self.author_nickname,
                'share_title': self.get_video_title(aweme_info),
                'share_url': self.get_share_url(aweme_info),
                'create_time': self.get_create_time(aweme_info),
            }
            _aweme_list.append(video_info)
        self._aweme_list = _aweme_list
        return self._aweme_list

    def get_share_url(self, aweme_info):
        return aweme_info['share_url']

    def get_author_nickname(self, aweme_info):
        return aweme_info['author']['nickname']

    def get_video_title(self, aweme_info):
        return aweme_info['desc']

    def get_create_time(self, aweme_info):
        date = arrow.get(aweme_info['create_time']).format('YYYYMMDD')
        return date
