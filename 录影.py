#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import subprocess

ffmpegPath = r"D:\learn\ffmpeg\bin\ffmpeg.exe"

d = r'D:\learn\ffmpeg\bin\ffmpeg.exe -f gdigrab -i desktop -f dshow -i audio="virtual-audio-capturer" -vcodec libx264 -preset:v ultrafast -tune:v zerolatency -r 25 -acodec libmp3lame '


class CutSplicingVdeio(object):
    def __init__(self):
        pass

    def instructions(self):
        dercription = "vdeio and image transform,vdeio other opreation"
        return dercription

    def transcribeScreen(self, filePath):
        cmd = d+filePath
        print(cmd)
        subprocess.call(cmd)


vp = CutSplicingVdeio()
vp.transcribeScreen(r"D:\learn\record.mp4")
