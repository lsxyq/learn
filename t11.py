#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x

j1 = {
    "record_start_time": 1550819397835,
    "audio": "https://imglive.ehafo.com/course/temp/2019/02/53HO3WF5jA1h6R8h76nY0cYFK0bB7OQ9ZMttSihm.aac"

}
j2 = {
    "record_start_time": 1550819577273,
    "audio": "https://imglive.ehafo.com/course/temp/2019/02/c4WLaPqYju2CimyYOO91zhTrjZiCFEDkN6LvmjjK.aac"}
j3 = {
    "record_start_time": 1550819778238,
    "audio": "https://imglive.ehafo.com/course/temp/2019/02/6SwrBsAseki5z3wUXLyr4emMGArpLOr7JHXmXQos.aac"
}

l1 = []
l1.append(j1)
l1.append(j2)
l1.append(j3)

l1.sort(key=lambda obj:obj['record_start_time'])

