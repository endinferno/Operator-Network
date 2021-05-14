from Operator import *


class Environment(Operator):
    def __init__(self):
        super().__init__()

        super().Insert(DEVICE_BASIC, 's_name', '环境因素')
        super().Insert(DEVICE_BASIC, 's_id', '')

        super().Insert(DEVICE_STATUS, 'use_state', '')
        super().Insert(DEVICE_STATUS, 'load_state', '')

        super().Insert(DEVICE_GEOMETRY, 'length', 10)
        super().Insert(DEVICE_GEOMETRY, 'width', 10)
        super().Insert(DEVICE_GEOMETRY, 'height', 2)

        super().Insert(DEVICE_FUNC, 'ac_1', self.setLength)
        super().Insert(DEVICE_FUNC, 'ac_2', self.setWidth)
        super().Insert(DEVICE_FUNC, 'ac_3', self.setHeight)
        super().Insert(DEVICE_FUNC, 'ac_4', self.setUseState)
        super().Insert(DEVICE_FUNC, 'ac_5', self.getLength)
        super().Insert(DEVICE_FUNC, 'ac_6', self.getWidth)
        super().Insert(DEVICE_FUNC, 'ac_7', self.getHeight)
        super().Insert(DEVICE_FUNC, 'ac_8', self.getUseState)
        super().Insert(DEVICE_FUNC, 'ac_9', self.matchEco)

    def setLength(self):
        print('设置长度')

    def setWidth(self):
        print('设置宽度')

    def setHeight(self):
        print('设置高度')

    def setUseState(self):
        print('设置使用状态')

    def getLength(self):
        print('获取高度')

    def getWidth(self):
        print('获取宽度')

    def getHeight(self):
        print('获取高度')

    def getUseState(self):
        print('获取使用状态')

    def matchEco(self):
        print('判断环境在某环境要素下能否发挥环境功能')
