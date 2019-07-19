#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import os
import re
from pathlib import Path


class BasePath():
    @property
    def root_dir(self):
        dir = Path(__file__).parent
        if not dir.exists():
            dir.mkdir(parents=True)
        return dir

    @property
    def date_path(self):
        import arrow
        dir = arrow.now().format('YYYY/MM/DD/')
        return str(dir)


class HuoShanPath(BasePath):

    def get_name_suffix(self, path: str):
        name, suffix = str(path).rsplit(".", 1)
        return name, suffix

    @property
    def finish_dir(self):
        dir = self.root_dir.joinpath('finish')
        if not dir.exists():
            dir.mkdir(parents=True)
        return dir

    @property
    def urls_dir(self):
        return self.root_dir.joinpath('urls')

    @property
    def share_url(self):
        return self.root_dir.joinpath("share_url.txt")

    @property
    def download_url(self):
        return self.root_dir.joinpath("download_url.txt")

    def get_video_name(self, video_info):
        if not video_info['share_title']:
            video_name = '{}_{}.mp4'.format(video_info['nickname'], video_info['create_time'])
        else:
            video_name = '{}.mp4'.format(video_info['share_title'])
        pattern = re.compile('[*"?|]')
        video_name = pattern.sub('', video_name)
        return video_name

    def get_watermark_path(self, video_info):
        video_name = self.get_video_name(video_info)
        dir = self.root_dir.joinpath('watermark_videos').joinpath(video_info['nickname'])
        if not dir.exists():
            dir.mkdir(parents=True)
        video_path = dir.joinpath(video_name).as_posix()
        return video_path, video_name

    def get_video_path(self, video_info):
        video_name = self.get_video_name(video_info)
        dir = self.root_dir.joinpath('videos').joinpath(video_info['nickname'])
        if not dir.exists():
            dir.mkdir(parents=True)
        video_path = dir.joinpath(video_name).as_posix()
        return video_path, video_name

    def remove_dir(self, dir):
        if not os.path.isdir(dir):
            return
        for file in os.listdir(dir):
            file_path = os.path.join(dir, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                self.remove_dir(file_path)
        os.rmdir(dir)


huoshan_path = HuoShanPath()

if __name__ == '__main__':
    pass
