# -*- coding: utf-8 -*-
#皮皮鳝元素的动作和属性
import cocos
#引入皮皮鳝这个精灵元素
class PPS(cocos.sprite.Sprite):
    def __init__(self):
        super(PPS,self).__init__('pps.png')
        #设置类的参数
        # 不可以跳
        self.can_jump = False
        # 速度为0
        self.speed = 0
        self.image_anchor = 0,0
        # 位置为x:100,y:300
        self.position = 100,300
        self.schedule(self.update)

    def jump(self,h):
        if self.can_jump:
            self.y += 1
            self.speed -= max(min(h,10),7)
            self.can_jump = False

    def land(self,y):
        if self.y > y -30:
            self.can_jump = True
            self.speed = 0
            self.y = y

    def update(self,dt):
        self.speed += 10*dt
        self.y -= self.speed
        if self.y < -80:
            self.reset()

    def reset(self):
        self.parent.reset()
        self.can_jump = False
        self.speed = 0
        self.position = 100,300

