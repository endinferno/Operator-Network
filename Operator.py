global DEVICE_BASIC
global DEVICE_PART
global DEVICE_STATUS
global DEVICE_GEOMETRY
global DEVICE_FUNC
global DEVICE_NETWORK
DEVICE_BASIC = 0
DEVICE_PART = 1
DEVICE_STATUS = 2
DEVICE_GEOMETRY = 3
DEVICE_FUNC = 4
DEVICE_NETWORK = 5


class Operator:
    def __init__(self):
        self.device_basic_attributes = {}
        self.device_part_attributes = {}
        self.status_attributes = {}
        self.geometry_attributes = {}
        self.func_attributes = {}
        self.network_relation_attributes = {}

    def Insert(self, attr_number, attr_name, attr_value):
        if attr_number == 0:
            self.device_basic_attributes[attr_name] = attr_value
        elif attr_number == 1:
            self.device_part_attributes[attr_name] = attr_value
        elif attr_number == 2:
            self.status_attributes[attr_name] = attr_value
        elif attr_number == 3:
            self.geometry_attributes[attr_name] = attr_value
        elif attr_number == 4:
            self.func_attributes[attr_name] = attr_value
        elif attr_number == 5:
            self.network_relation_attributes[attr_name] = attr_value
        else:
            print('No Such Attribute Number')

    def callFuncByDictAttr(self, dict_name):
        self.func_attributes[dict_name]()

    def getName(self):
        return self.device_basic_attributes['s_name']

    def getData(self, attr_number):
        if attr_number == 0:
            return self.device_basic_attributes
        elif attr_number == 1:
            return self.device_part_attributes
        elif attr_number == 2:
            return self.status_attributes
        elif attr_number == 3:
            return self.geometry_attributes
        elif attr_number == 4:
            return self.func_attributes
        elif attr_number == 5:
            return self.network_relation_attributes
        else:
            return None

    def readFromExcelData(self, excel_data):
        attr_type = 0
        for row in range(len(excel_data.index)):
            title = excel_data.loc[row].values[0]
            if title != '':
                if title == '设备基本属性':
                    attr_type = DEVICE_BASIC
                elif title == '设备部件属性':
                    attr_type = DEVICE_PART
                elif title == '设备状态属性':
                    attr_type = DEVICE_STATUS
                elif title == '设备几何属性':
                    attr_type = DEVICE_GEOMETRY
                elif title == '设备功能属性':
                    attr_type = DEVICE_FUNC
                elif title == '网络关联属性':
                    attr_type = DEVICE_NETWORK
                else:
                    assert(True, '该属性不存在')
                continue
            key = excel_data.loc[row].values[1]
            value = excel_data.loc[row].values[2]
            self.Insert(attr_type, key, value)
