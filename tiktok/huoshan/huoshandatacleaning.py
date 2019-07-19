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
        self._data_list = []

    @property
    def author_info(self):
        if not self.raw_data_list:
            return self._author_info
        if self._author_info:
            return self._author_info
        data = self.get_data(self.raw_data_list[0])
        self._author_info = {
            'id': data['author']['id'],
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
    def raw_data_list(self):
        """
        [{
          "data": {},
          "rid": "2019071913175701002805608539749",
          "tags": [],
          "type": 3
        },
        {
          "data": {},
          "rid": "2019071913175701002805608539749",
          "tags": [],
          "type": 3
        },
        ]
        :return:
        """
        if not self.raw_data.get('data'):
            return []
        return self.raw_data.get('data')

    @property
    def cleaned_data_list(self):
        if self._data_list:
            return self._data_list
        _data_list = []
        for video_data in self.raw_data_list:
            video_info = {
                'rid': video_data.get('rid'),
                'nickname': self.author_nickname,
                "video_id": self.get_video_id(video_data),
                'share_title': self.get_video_title(video_data),
                'share_url': self.get_share_url(video_data),
                'create_time': self.get_create_time(video_data),
            }
            _data_list.append(video_info)
        self._data_list = _data_list
        return self._data_list

    def get_data(self, video_data):
        return video_data['data']

    def get_video_id(self, video_data):
        return self.get_data(video_data)['id_str']

    def get_share_url(self, video_data):
        return self.get_data(video_data)['share_url']

    def get_video_title(self, video_data):
        return self.get_data(video_data)['title']

    def get_create_time(self, video_data):
        date = arrow.get(self.get_data(video_data)['create_time']).format('YYYYMMDD')
        return date


if __name__ == '__main__':
    d = DataCleaning(r'C:\Projects\learn\tiktok\huoshan\urls\20190719_131757_425_125.json')
