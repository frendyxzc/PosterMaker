# -*- coding: UTF-8 -*-
#
# frendyxzc@126.com
# 2017.09.22
#
# [Sample]
#   python post.py --bg 20170815112219.jpg --font msyhl.ttc --fontSize 30 --userIcon testIcon.jpg --userIconAttr 80,80,316,242 --userName 哈哈 --userNameAttr 360,335 --qr qrimg.jpg --qrAttr 142,140,191,946 --textColor 0,0,0 --output tmp.jpg
#


import argparse
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
    parser.add_argument('--bg', type=str, default='',
                       help='指定模板图片')
    parser.add_argument('--font', type=str, default='',
                       help='字体')
    parser.add_argument('--fontSize', type=int, default='30',
                       help='字体大小')

    parser.add_argument('--userIcon', type=str, default='',
                       help=u'用户头像')
    parser.add_argument('--userIconAttr', type=str, default='30,30,0,0',
                       help=u'用户头像的宽、高、X坐标、Y坐标：W,H,X,Y')

    parser.add_argument('--userName', type=str, default='frendy',
                       help=u'用户昵称')
    parser.add_argument('--userNameAttr', type=str, default='',
                       help=u'用户昵称的X坐标、Y坐标：X,Y')

    parser.add_argument('--qr', type=str, default='',
                       help=u'用户二维码')
    parser.add_argument('--qrAttr', type=str, default='30,30,0,0',
                       help=u'用户二维码宽、高、X坐标、Y坐标：W,H,X,Y')

    parser.add_argument('--textColor', type=str, default='0,0,0',
                       help=u'文字颜色：R,G,B')

    parser.add_argument('--output', type=str, default='post.jpg',
                       help=u'输出文件名')
    args = parser.parse_args()
    return args



if __name__ == '__main__':
    args = parse_args()

    userIconAttr = args.userIconAttr.split(',')
    userNameAttr = args.userNameAttr.split(',')
    qrAttr = args.qrAttr.split(',')

    textColor = args.textColor.split(',')

    pMaker = postMaker(
        bg=args.bg, font=args.font, fontSize=args.fontSize, output=args.output)
    pMaker.create(
        userIcon=args.userIcon,
        userIconW=int(userIconAttr[0]),
        userIconH=int(userIconAttr[1]),
        userIconX=int(userIconAttr[2]),
        userIconY=int(userIconAttr[3]),
        userName=args.userName,
        userNameX=int(userNameAttr[0]),
        userNameY=int(userNameAttr[1]),
        qr=args.qr,
        qrW=int(qrAttr[0]),
        qrH=int(qrAttr[1]),
        qrX=int(qrAttr[2]),
        qrY=int(qrAttr[3]),
        textColor={'R': int(textColor[0]), 'G': int(textColor[1]), 'B': int(textColor[2])})

    print('** done: ' + args.output)