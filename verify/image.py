#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# Author:Leslie-x
import random


def get_back_tracks(distance):
    over_length = distance
    back_tracks = []
    while over_length > 3:
        offset = random.choice((-1, -2, -3))
        back_tracks.append(offset)
        over_length += offset
    res = '-{}'.format(over_length)
    back_tracks.append(int(res))
    print(back_tracks)



get_back_tracks(11)
