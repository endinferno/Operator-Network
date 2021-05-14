from Operator import *


class DeckLights(Operator):
    def __init__(self):
        super().__init__()

        super().Insert(DEVICE_BASIC, 's_name', '甲板灯光')
        super().Insert(DEVICE_BASIC, 's_type', 'B')
        super().Insert(DEVICE_BASIC, 's_id', '1')
        super().Insert(DEVICE_BASIC, 's_label', 'B1')

        super().Insert(DEVICE_PART, 'sub_set_1', '灯泡1')

        super().Insert(DEVICE_STATUS, 'use_state', '0')
        super().Insert(DEVICE_STATUS, 'load_state', '0')
        super().Insert(DEVICE_STATUS, 'loc_state', '甲板')

        super().Insert(DEVICE_FUNC, 'ac_1', self.openBulb)
        super().Insert(DEVICE_FUNC, 'ac_2', self.closeBulb)
        super().Insert(DEVICE_FUNC, 'ac_3', self.openAllLights)
        super().Insert(DEVICE_FUNC, 'ac_4', self.closeAllLights)
        super().Insert(DEVICE_FUNC, 'ac_5', self.setUseState)
        super().Insert(DEVICE_FUNC, 'ac_6', self.getUseState)
        super().Insert(DEVICE_FUNC, 'ac_7', self.getLightBright)

    def openBulb(self):
        print('打开灯泡1')

    def closeBulb(self):
        print('关闭灯泡1')

    def openAllLights(self):
        print('打开全部灯光')

    def closeAllLights(self):
        print('关闭全部灯光')

    def setUseState(self):
        print('设置灯泡使用状态')

    def getUseState(self):
        print('获取灯泡使用状态')

    def getLightBright(self):
        print('获取灯泡亮度')
