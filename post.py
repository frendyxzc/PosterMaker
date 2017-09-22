# -*- coding: UTF-8 -*-
#
# frendyxzc@126.com
# 2017.09.22

import argparse
import os
import os.path
import time
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont

class postMaker(object):
    def __init__(self, bg, font, fontSize, output):
        self.bg = bg
        self.font = font
        self.fontSize = fontSize
        self.output = output
        self.post = None

    def create(self,
               userIcon, userIconW, userIconH, userIconX, userIconY,
               userName, userNameX, userNameY,
               qr, qrW, qrH, qrX, qrY, textColor):
        try:
            bg = Image.open(self.bg)
            userIcon = Image.open(userIcon)
            font = ImageFont.truetype(self.font, self.fontSize)

            userIcon.thumbnail((userIconW, userIconH))
            bg.paste(userIcon, (userIconX, userIconY))

            draw = ImageDraw.Draw(bg)
            draw.ink = textColor.get('R',0) + textColor.get('G',0) * 256 + textColor.get('B',0)*256*256
            textWidth,textHeight = font.getsize(userName)
            draw.text([userNameX-textWidth/2, userNameY], userName, font=font)

            qr = Image.open(qr)
            qr.thumbnail((qrW, qrH))
            bg.paste(qr,(qrX, qrY))

            self.post = bg
            bg.save(self.output, "jpeg")
        except Exception as e:
            print(repr(e))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bg', type=str, default='.',
                       help='指定模板图片')
    parser.add_argument('--font', type=str, default='.',
                       help='字体')
    parser.add_argument('--fontSize', type=str, default='.',
                       help='字体大小')

    parser.add_argument('--userIcon', type=str, default='',
                       help=u'用户头像')
    parser.add_argument('--userIconW', type=int, default='',
                       help=u'用户头像宽')
    parser.add_argument('--userIconH', type=int, default='',
                       help=u'用户头像高')
    parser.add_argument('--userIconX', type=int, default='',
                       help=u'用户头像X坐标')
    parser.add_argument('--userIconY', type=int, default='',
                       help=u'用户头像Y坐标')

    parser.add_argument('--userName', type=str, default='',
                       help=u'用户昵称')
    parser.add_argument('--userNameX', type=int, default='',
                       help=u'用户昵称X坐标')
    parser.add_argument('--userNameY', type=int, default='',
                       help=u'用户昵称Y坐标')

    parser.add_argument('--qr', type=str, default='',
                       help=u'用户二维码')
    parser.add_argument('--qrW', type=int, default='',
                       help=u'用户二维码宽')
    parser.add_argument('--qrH', type=int, default='',
                       help=u'用户二维码高')
    parser.add_argument('--qrX', type=int, default='',
                       help=u'用户二维码X坐标')
    parser.add_argument('--qrY', type=int, default='',
                       help=u'用户二维码Y坐标')

    parser.add_argument('--textColor', type=str, default='',
                       help=u'文字颜色，{R，G，B}')
    parser.add_argument('--output', type=str, default='',
                       help=u'输出文件名')
    args = parser.parse_args()
    return args



if __name__ == '__main__':
    args = parse_args()

    pMaker = postMaker(
        bg=args.bg, font=args.font, fontSize=args.fontSize, output=args.output)
    pMaker.create(
        userIcon=args.userIcon,
        userIconW=args.userIconW,
        userIconH=args.userIconH,
        userIconX=args.userIconX,
        userIconY=args.userIconY,
        userName=args.userName,
        userNameX=args.userNameX,
        userNameY=args.userNameY,
        qr=args.qr,
        qrW=args.qrW,
        qrH=args.qrH,
        qrX=args.qrX,
        qrY=args.qrY,
        textColor={'R': 0, 'G': 0, 'B': 0})

    print('** done: ' + args.output)