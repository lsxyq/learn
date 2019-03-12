#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
from pathlib import Path
import json
import pydash
import requests
import os
import subprocess


class MergeHistory():
    def __init__(self, path):
        self.root_path = path
        self.default_path = 'download\merged.aac'
        self.history_list = []
        self.duration_list = []
        self.audio_path_list = []
        self.merged_animation = None
        self.start_time = None

    def list_file(self):
        json_dir = Path(self.root_path)
        for path in json_dir.iterdir():
            self.parser_json(path)
        self.history_list.sort(key=lambda obj: obj['record_start_time'])

    def parser_json(self, path):
        f = open(path, 'r', encoding='utf8')
        data = json.loads(f.read())
        f.close()
        self.history_list.append(data)

    def stream_download(self, url):
        r = requests.get(url, stream=True)
        name = url.rsplit('/', 1)[-1]
        path = 'download\{}'.format(name)
        f = open(path, 'wb')
        f.write(r.content)
        f.flush()
        f.close()
        return path

    def play_duration(self, url):
        command = (r'ffprobe -print_format json -loglevel quiet -show_streams %s' % url)
        result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = result.stdout.read()
        temp = str(out.decode('utf-8'))
        data = pydash.get(json.loads(temp), 'streams.0.duration')
        return float(data) * 1000

    def merge_audio(self):
        for history in self.history_list:
            audio = pydash.get(history, 'audio')
            path = self.stream_download(audio)
            self.audio_path_list.append(path)
            self.duration_list.append(self.play_duration(audio))
        print(self.audio_path_list)
        # cmd = ('ffmpeg -i "concat:%s" -acodec copy %s' % ('|'.join(self.audio_path_list), self.default_path))
        cmd = ('ffmpeg -i "concat:%s" -acodec aac  %s' % ('|'.join(self.audio_path_list), self.default_path))
        os.popen(cmd)
        print('音频合并完成', self.default_path)
        from functools import reduce
        duration = reduce(lambda x, y: x + y, self.duration_list)
        print('音频预计时长', duration / 1000 / 60)

    def merge_animation(self):
        for index, history in enumerate(self.history_list):
            if not self.merged_animation:
                self.merged_animation = history
                self.start_time = pydash.get(history, 'record_start_time')
                continue
            duration = self.duration_list[index - 1]
            print(self.start_time, '开始前')
            self.start_time = self.start_time + duration
            print(self.start_time, '开始后')

            context = pydash.get(history, 'context')
            record_start_time = pydash.get(history, 'record_start_time')
            merged_context = pydash.get(self.merged_animation, 'context')
            for index, content in enumerate(context):
                content = self.correction_time(content, record_start_time, content['type'])
                merged_context.append(content)
        self.save_merged_animation()
        print(self.duration_list)

    def correction_time(self, content, record_start_time, type):
        # 校正每条记录相对于开始的时间
        if not content.get('start_time'):
            if not (content.get('lines') and content.get('important')):
                return content
            if content.get('lines'):
                first_time = pydash.get(content, 'lines.0.0.time')
                content['start_time'] = self.start_time + first_time - record_start_time
            elif content.get('important'):
                first_time = pydash.get(content, 'important.0.start_time')
                content['start_time'] = self.start_time + first_time - record_start_time
        else:
            content['start_time'] = self.start_time + content['start_time'] - record_start_time
        if type == 'image':
            lines = pydash.get(content, 'lines')
            if not lines:
                return content
            for line in lines:
                for animation in line:
                    animation['time'] = self.start_time + animation['time'] - record_start_time
        elif type == 'text':
            important = pydash.get(content, 'important')
            if not important:
                return content
            for animation in important:
                animation['start_time'] = self.start_time + animation['start_time'] - record_start_time
                animation['end_time'] = self.start_time + animation['end_time'] - record_start_time
        return content

    def save_merged_animation(self):
        with open('test/merged_animation.json', 'w', encoding='utf8') as f:
            f.write(json.dumps(self.merged_animation))
        print('动画文件合成')

    def main(self):
        self.list_file()
        self.merge_audio()
        self.merge_animation()


if __name__ == '__main__':
    MergeHistory(r'D:\learn\json').main()

    # obj= MergeHistory(r'D:\learn\json')
    # obj.history_list.append({r'D:\learn\audio\1.aac'})
    # obj.history_list.append({r'D:\learn\audio\2.aac'})
    # obj.history_list.append({r'D:\learn\audio\3.aac'})
    # obj.merge_audio()
