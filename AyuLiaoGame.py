# -*-coding: utf-8 -*-

import cocos
import pyaudio
import struct
from pps import PPS
from black import BlackBlock

class VoiceGame(cocos.layer.ColorLayer):
    is_event_handler = True

    def __init__(self):
        super(VoiceGame,self).__init__(255,255,255,255,800,600)

        #初始化声音
        self.NUM_SAMPLES = 1000  # pyAudio内部缓存的块的大小
        self.LEVEL = 1500 # 保存声音的阈值

        self.voicebar = cocos.sprite.Sprite('black.png')
        self.voicebar.position = 20,450
        self.voicebar.scale_y = 0.1
        self.voicebar.image_anchor = 0,0
        self.add(self.voicebar)
        #皮皮鳝
        self.pps = PPS()
        self.add(self.pps)
        #地板
        self.floor = cocos.cocosnode.CocosNode()
        self.add(self.floor)

        pos = 0,100
        for i in range(100):
            b = BlackBlock(pos)
            #添加黑色的砖块
            self.floor.add(b)
            pos = b.x + b.width, b.height


        #开启声音输入
        pa = pyaudio.PyAudio()
        SAMPLING_RATE = int(pa.get_device_info_by_index(0)['defaultSampleRate'])
        self.stream = pa.open(format=pyaudio.paInt16,channels=1,rate=SAMPLING_RATE,input=True,frames_per_buffer=self.NUM_SAMPLES)

        self.schedule(self.update)

    def on_mouse_press(self,x,y,buttons,modifiers):
        pass

    def collide(self):
        px = self.pps.x - self.floor.x
        for b in self.floor.get_children():
            if b.x <= px + self.pps.width * 0.8 and px + self.pps.width*0.2 <= b.x + b.width:
                if self.pps.y < b.height:
                    self.pps.land(b.height)
                    break;

    def update(self,dt):

        string_audio_data = self.stream.read(self.NUM_SAMPLES)
        k = max(struct.unpack('1000h',string_audio_data))

        self.voicebar.scale_x = k /10000.0

        if k > 3000:
            self.floor.x -= min((k/20.0),150)*dt

        if k > 8000:
            self.pps.jump((k-8000)/1000.0)
        self.collide()

    def reset(self):
        self.floor.x = 0

cocos.director.director.init(caption="Let's GO!")
cocos.director.director.run(cocos.scene.Scene(VoiceGame()))






























