#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import subprocess
from subprocess import Popen, PIPE
import subprocess
import os

d = r'ffmpeg.exe -f gdigrab -offset_x 0 -offset_y 0 -video_size 1366x768 -i desktop -f dshow -i audio="virtual-audio-capturer" -vcodec libx264 -preset:v ultrafast -tune:v zerolatency -r 24 -y -acodec aac -ac 1 -ar 44100 -ab 64k d:\out.mp4'


class CutSplicingVideo(object):
    def __init__(self):
        self.p = None
        pass

    def transcribeScreen(self):
        os.system(d)


    def kill_cmd(self):
        self.p.terminate()


vp = CutSplicingVideo()
vp.transcribeScreen()





