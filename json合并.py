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
        self.history_list = []
        self.merged_audio = None
        self.duration_list = []
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
        with open('audio/{}'.format(name), 'wb') as f:
            f.write(r.content)
            f.flush()
        return name

    def play_duration(self, filename):
        command = ["ffprobe.exe", "-loglevel", "quiet", "-print_format", "json", "-show_format", "-show_streams", "-i",
                   filename]
        result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = result.stdout.read()
        temp = str(out.decode('utf-8'))
        print(temp)
        data = pydash.get(json.loads(temp), 'streams.0.duration')
        return int(float(data) * 1000)

    def merge_audio(self):
        for history in self.history_list:
            audio = pydash.get(history, 'audio')
            path = self.stream_download(audio)
            self.duration_list.append(self.play_duration(path))
            if not self.merged_audio:
                self.merged_audio = path
                continue
            cmd = ('ffmpeg -i "concat:%s|%s" -acodec copy %s' % (self.merged_audio, path, 'audio/merged.acc'))
            os.popen(cmd)
        print('音频合并完成', self.merged_audio)

    def merge_animation(self):
        for index, history in enumerate(self.history_list):
            if not self.merged_animation:
                self.merged_animation = history
                continue
            duration = self.duration_list[index - 1]
            self.start_time = pydash.get(history, 'record_start_time') + duration
            context = pydash.get(history, 'context')
            merged_context = pydash.get(self.merged_animation, 'context')
            record_start_time = context['record_start_time']
            for content in context:
                content = self.correction_time(content, record_start_time, content['type'])
                merged_context.append(content)
        self.save_merged_animation()

    def correction_time(self, content, record_start_time, type):
        "校正时间"
        content['start_time'] = self.start_time + content['start_time'] - record_start_time
        if type == 'image':
            lines = pydash.get(content, 'lines')
            for line in lines:
                for animation in line:
                    animation['time'] = self.start_time + animation['time'] - record_start_time
        elif type == 'text':
            important = pydash.get(content, 'important')
            for animation in important:
                animation['start_time'] = self.start_time + animation['start_time'] - record_start_time
                animation['end_time'] = self.start_time + animation['end_time'] - record_start_time
        return content

    def save_merged_animation(self):
        with open('json/merged_animation.json', 'w', encoding='utf8') as f:
            f.write(self.merged_animation)

    def main(self):
        self.list_file()
        self.merge_audio()
        self.merge_animation()


if __name__ == '__main__':
    MergeHistory('F:\learn\json').main()
    # MergeHistory('F:\learn\json').play_duration(r'F:\learn\audio\1.aac')

