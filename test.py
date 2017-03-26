# -*- coding: utf-8 -*-
import cocos

from cocos.actions import Repeat,Reverse,ScaleBy,RotateBy

class HelloWorld(cocos.layer.ColorLayer):
    def __init__(self):
        #将层的背景调成蓝色
        super(HelloWorld,self).__init__(64,64,224,255)
        # 新建文字标签用于显示Hello World
        label = cocos.text.Label('Hello,World',
                                 # 如果要显示中文,需要使用支持中文的字体,比如"微软雅黑"
                                 font_name='Times New Roman',
                                 font_size=32,
                                 # 设置锚点为正中间
                                 anchor_x='center',anchor_y='center')
        # 设置文字标签在层的位置.由于锚点为正中间,即"用手捏"标签的正中间,放到(320,240)的位置
        label.position = 320,240
        # 把文字标签添加到层
        self.add(label)

        # 新建一个精灵,在这里是一个小人(英文文档没有给示范图片,所以这个icon.png请自行找个q版小人图片,放在代码同目录下)
        sprite = cocos.sprite.Sprite('black.png')
        # 精灵锚点默认在正中间,只设置位置就好
        sprite.position = 320,240
        # 放大三倍,添加到层,z轴设为1,比层更靠前
        sprite.scale = 3
        self.add(sprite,z=1)

        # 定义一个动作,即2秒内放大三倍
        scale = ScaleBy(3,duration=2)
        # 标签的动作:重复执行放大三倍缩小三倍又放大三倍...Repeat即为重复动作,Reverse为相反动作
        label.do(Repeat(scale+Reverse(scale)))
        # 精灵的动作:重复执行缩小三倍放大三倍又缩小三倍..
        sprite.do(Repeat(Reverse(scale)+scale))
        # 层的动作:重复执行10秒内360度旋转
        self.do(RotateBy(360,duration=10))

#"导演诞生",即建一个窗口,默认是640*480,不可调整大小
cocos.director.director.init()
#建一个"场景",场景里只有一个hello_layer层,层里已自带文字
main_scene = cocos.scene.Scene(HelloWorld())
#"导演说Action",让场景工作
cocos.director.director.run(main_scene)