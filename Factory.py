import FuelTruck
import DeckLights
import AdvectionPlate
import People
import Environment


class Factory:
    def __init__(self):
        self.operator_list = []
        self.operator_list.append(FuelTruck.FuelTruck())
        self.operator_list.append(DeckLights.DeckLights())
        self.operator_list.append(AdvectionPlate.AdvectionPlate())
        self.operator_list.append(People.People())
        self.operator_list.append(Environment.Environment())

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

