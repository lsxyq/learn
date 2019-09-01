#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author:Leslie-x 


'''
1: 一根不均匀的长绳，完全燃烧时间为一个小时，现有若干的同样的的长绳，请你利用长绳记时一个小时一十五分钟，如何实现？
   先点燃A绳子一头，同时点燃B绳子两头，等其中B绳子烧完时，在点燃A绳子另一头，即从此刻开始到A烧完为一个小时

   绳子两端分别是A、B,A、B同时点着，烧完时为半个小时，那个点记为C然后在相同绳子上分别找出A、B、C从c点剪断，
   点燃AC或BC两头，计时开始，烧完用时15分，迅速点燃另一整根绳子，烧完为1小时。及时的时间总共为1小时15分

2: 共有100个球，A,B两个人一次不放回的拿球，每次至少拿一个，最多拿五个，你第一个拿，你会怎么拿？
后面怎么拿才能保证你拿到第一百个球？
   就是用逆向归纳的方法：如果最后你拿完剩1、2、3、4、5个球，那么则是对方拿到了第100个球。
所以你的目标就是剩余6个球，这样无论对方怎么拿，你都能拿到100个球。由此类推，倒数第二次，
你的目标就是剩余12个球，这样不管对方拿几个，你都可以将剩余球的个数变为6个，从而变为前面说的那种情况，
而拿到第100个球。于是，不难归纳出，只要每次你的目标是剩余球的个数为6的倍数，那么你肯定最终拿到第100个球。
所以，如果最开始有100个球，那么只要你先拿4个，使剩余球的个数为96个（96=16×6），那么最后拿到第100个球的肯定是你。



3: 共有25匹马，但是只有五个赛道，每次只能有五匹马比赛，排除其他一切因素，不能使用其他的工具，
每匹马的发挥恒定，请问至少要几次才能找出最快的五匹马？



一个城市的车辆只有蓝色和绿色两种颜色，蓝色15%，绿色85%，某日发生了一次车祸，目击者声称车辆是蓝色，
但是专家表示，当时的情况下，证人看错的概率是80%
那么。肇事车辆是蓝色的概率到底是多少？

这个问题明显是分为四种情况：
是蓝车，他看错了，15%*20%=3%
是蓝车，他看对了，15%*80%=12%
是绿车，他看对了，85%*80%=68%
是绿车，他看错了，85%*20%=17%
'''
