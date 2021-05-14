from Operator import *


class AdvectionPlate(Operator):
    def __init__(self):
        super().__init__()

        super().Insert(DEVICE_BASIC, 's_name', '平流板')
        super().Insert(DEVICE_BASIC, 's_type', 'C')
        super().Insert(DEVICE_BASIC, 's_id', '1')
        super().Insert(DEVICE_BASIC, 's_label', 'C1')

        super().Insert(DEVICE_STATUS, 'use_state', '0')
        super().Insert(DEVICE_STATUS, 'loc_state', '甲板')

        super().Insert(DEVICE_GEOMETRY, 'length', 10)
        super().Insert(DEVICE_GEOMETRY, 'width', 10)
        super().Insert(DEVICE_GEOMETRY, 'height', 2)

        super().Insert(DEVICE_FUNC, 'ac_1', self.advectionPlateRise)
        super().Insert(DEVICE_FUNC, 'ac_2', self.advectionPlateDrop)
        super().Insert(DEVICE_FUNC, 'ac_3', self.setLength)
        super().Insert(DEVICE_FUNC, 'ac_4', self.setWidth)
        super().Insert(DEVICE_FUNC, 'ac_5', self.setHeight)
        super().Insert(DEVICE_FUNC, 'ac_6', self.setUseState)
        super().Insert(DEVICE_FUNC, 'ac_7', self.getLength)
        super().Insert(DEVICE_FUNC, 'ac_8', self.getWidth)
        super().Insert(DEVICE_FUNC, 'ac_9', self.getHeight)
        super().Insert(DEVICE_FUNC, 'ac_10', self.getUseState)

    def advectionPlateRise(self):
        print('平流板升起')

    def advectionPlateDrop(self):
        print('平流板放下')

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
