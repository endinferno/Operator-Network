from Operator import *


class FuelTruck(Operator):
    def __init__(self):
        super().__init__()

        super().Insert(DEVICE_BASIC, 's_name', '加油车')
        super().Insert(DEVICE_BASIC, 's_type', 'A')
        super().Insert(DEVICE_BASIC, 's_id', '1')
        super().Insert(DEVICE_BASIC, 's_label', 'A1')

        super().Insert(DEVICE_PART, 'sub_set_1', '加油管')

        super().Insert(DEVICE_STATUS, 'use_state', '0')
        super().Insert(DEVICE_STATUS, 'load_state', '0')
        super().Insert(DEVICE_STATUS, 'loc_state', '仓库')

        super().Insert(DEVICE_GEOMETRY, 'length', 10)
        super().Insert(DEVICE_GEOMETRY, 'width', 10)
        super().Insert(DEVICE_GEOMETRY, 'height', 2)

        super().Insert(DEVICE_FUNC, 'ac_1', self.addFuelByVolume)
        super().Insert(DEVICE_FUNC, 'ac_2', self.connectFuelTube)
        super().Insert(DEVICE_FUNC, 'ac_3', self.disconnectFuelTube)
        super().Insert(DEVICE_FUNC, 'ac_4', self.addFuelByTime)
        super().Insert(DEVICE_FUNC, 'ac_1', self.setLength)
        super().Insert(DEVICE_FUNC, 'ac_2', self.setWidth)
        super().Insert(DEVICE_FUNC, 'ac_3', self.setHeight)
        super().Insert(DEVICE_FUNC, 'ac_4', self.setUseState)
        super().Insert(DEVICE_FUNC, 'ac_1', self.getLength)
        super().Insert(DEVICE_FUNC, 'ac_2', self.getWidth)
        super().Insert(DEVICE_FUNC, 'ac_3', self.getHeight)
        super().Insert(DEVICE_FUNC, 'ac_4', self.getUseState)
        super().Insert(DEVICE_FUNC, 'ac_1', self.matchEco)

    def addFuelByVolume(self):
        print('按加油量加油')

    def connectFuelTube(self):
        print('连接加油管')

    def disconnectFuelTube(self):
        print('断开加油管')

    def addFuelByTime(self):
        print('按加油时间加油')

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
        print('判断加油车是否与保障位匹配')
