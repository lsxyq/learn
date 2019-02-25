#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import os
import json
import pydash
import subprocess
import requests
from io import BytesIO


class MergeHistory():
    def __init__(self):
        pass

    def main(self):
        self.parser_json(path='')

    def merge_audio(self, ):
        cmd = (r'ffmpeg -i "concat:D:\learn\audio\1.aac|D:\learn\audio\2.aac" -acodec copy D:\learn\audio\out2.m4a')
        os.popen(cmd)

    def merge_animation(self):
        pass

    def play_duration(self, filename):
        command = ["ffprobe.exe", "-loglevel", "quiet", "-print_format", "json", "-show_format", "-show_streams", "-i",
                   filename]
        result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = result.stdout.read()
        temp = str(out.decode('utf-8'))
        data = pydash.get(json.loads(temp), 'format.duration')
        return data

    def parser_json(self, path):
        f = open(path, 'r', encoding='utf8')
        data = json.loads(f.read())
        f.close()
        start_time = pydash.get(data, 'record_start_time')
        audio = pydash.get(data, 'audio')
        context = pydash.get(data, 'context')
        for content in context:
            pass

    def stream_download(self, url):
        r = requests.get(url, stream=True)
        name = url.rsplit('/', 1)[-1]
        with open('audio/{}'.format(name), 'wb') as f:
            f.write(r.content)
        return name


if __name__ == '__main__':
    pass

