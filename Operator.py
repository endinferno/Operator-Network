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
