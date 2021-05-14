from Operator import *


class People(Operator):
    def __init__(self):
        super().__init__()

        super().Insert(DEVICE_BASIC, 's_name', '人员因素')
        super().Insert(DEVICE_BASIC, 's_type', '')
        super().Insert(DEVICE_BASIC, 's_id', '')
        super().Insert(DEVICE_BASIC, 's_label', '')

        super().Insert(DEVICE_STATUS, 'use_state', '')
        super().Insert(DEVICE_STATUS, 'load_state', '')
        super().Insert(DEVICE_STATUS, 'work_state', '')
        super().Insert(DEVICE_STATUS, 'loc_state', '')

        super().Insert(DEVICE_FUNC, 'ac_1', self.doSomething)
        super().Insert(DEVICE_FUNC, 'ac_1', self.setUseState)
        super().Insert(DEVICE_FUNC, 'ac_2', self.setLocState)
        super().Insert(DEVICE_FUNC, 'ac_1', self.getUseState)
        super().Insert(DEVICE_FUNC, 'ac_2', self.getLocState)
        super().Insert(DEVICE_FUNC, 'ac_1', self.matchEco)

    def doSomething(self):
        print('执行工作')

    def setUseState(self):
        print('改变使用状态')

    def getUseState(self):
        print('获取使用状态')

    def setLocState(self):
        print('改变位置')

    def getLocState(self):
        print('获取位置')

    def matchEco(self):
        print('判断人员在某环境要素下能否发挥人员功能')
