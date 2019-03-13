#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import os
import pandas as pd

"""
  TCP    192.168.1.155:63758    129.211.126.69:4730    ESTABLISHED     12884
  TCP    192.168.1.155:63973    129.211.126.69:4730    ESTABLISHED     3568
"""


def kill_port(port):
    find_port = 'netstat -aon | findstr %s' % port
    result = os.popen(find_port)
    info = result.read().split('\n')
    data = []
    for line in info:
        if not line:
            continue
        temp = [str for str in line.split(" ") if str]
        data.append(temp)
    parser_cmd(data)


def parser_cmd(data):
    columns = ["type", "secret", "open", "status", "pid"]
    df = pd.DataFrame(data=data, columns=list(columns))
    for index in range(len(data)):
        pid = df.loc[index, 'pid']
        kill_pid(pid)


def kill_pid(pid):
    find_kill = 'taskkill -f -pid %s' % pid
    print(find_kill)
    result = os.popen(find_kill)
    print(result)


kill_port(4730)
