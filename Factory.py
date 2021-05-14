import FuelTruck
import DeckLights
import AdvectionPlate
import People
import Environment


class Factory:
    def __init__(self):
        self.operator_list = []
#        self.operator_list.append(FuelTruck.FuelTruck())
#        self.operator_list.append(DeckLights.DeckLights())
#        self.operator_list.append(AdvectionPlate.AdvectionPlate())
#        self.operator_list.append(People.People())
#        self.operator_list.append(Environment.Environment())
        self.operator_name_dict = {}
        self.operator_name_dict[0] = '设备基本属性'
        self.operator_name_dict[1] = '设备部件属性'
        self.operator_name_dict[2] = '设备状态属性'
        self.operator_name_dict[3] = '设备几何属性'
        self.operator_name_dict[4] = '设备功能属性'
        self.operator_name_dict[5] = '网络关联属性'

    def getNames(self):
        name_list = []
        for item in self.operator_list:
            name_list.append(item.getName())
        return name_list

    def getOperator(self, name):
        for operator in self.operator_list:
            if operator.getName() == name:
                return operator
        return None

    def insert(self, operator):
        self.operator_list.append(operator)

    def getData(self):
        excel_data = {}
        for operator in self.operator_list:
            sheet_name = operator.getName()
            data = []

            for idx in range(6):
                tmp_list = [''] * 3
                tmp_list[0] = self.operator_name_dict[idx]
                data.append(tmp_list)
                operator_dict = operator.getData(idx)
                for key in operator_dict:
                    tmp_list = [''] * 3
                    tmp_list[1] = key
                    if hasattr(operator_dict[key], '__call__'):
                        tmp_list[2] = operator_dict[key].__name__
                    else:
                        tmp_list[2] = operator_dict[key]
                    data.append(tmp_list)
            excel_data[sheet_name] = data
        return excel_data
