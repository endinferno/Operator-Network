import tkinter as tk
from Operator import *
import Factory
from functools import partial


class Interface:
    def __init__(self):
        self.top = tk.Tk()
        self.top.title('Visual Display')
        self.top.geometry('1000x600')
        self.top.resizable(0, 0)
        self.label_text = ['设备基本属性', '设备部件属性', '设备状态属性',
                           '设备几何属性', '设备功能属性', '网络关联属性']
        self.label_dict = {0: None, 1: None, 2: None,
                           3: None, 4: None, 5: None}
        self.entry_dict = {0: None, 1: None, 2: None,
                           3: None, 4: None, 5: None}
        self.component_num = [2] * 6

    def defineModule(self):
        self.left_canvas = tk.Canvas(self.top, width=800, height=600, bg='red')
        self.member_frame = tk.Frame(
            self.top, width=200, height=600, border=2, bg='black')
        self.member_frame.propagate(0)
        self.listbox = tk.Listbox(self.member_frame, height=20, selectmode=tk.SINGLE)
        self.add_operator_button = tk.Button(
            self.member_frame, text='添加对象', command=self.addOperator)

    def addOperator(self):
        self.print_attr_window = tk.Toplevel()
        button_list = []
        show_scrollbar = tk.Scrollbar(self.print_attr_window)
        show_canvas = tk.Canvas(self.print_attr_window, width=800,
                                height=600, bg='black', yscrollcommand=show_scrollbar.set)
        show_scrollbar.config(command=show_canvas.yview)
        show_frame = tk.Frame(show_canvas, bg='black', width=800, height=600)
        for i in range(len(self.component_num)):
            self.label_dict[i] = tk.Label(show_frame, text=self.label_text[i])
            entry_list = []
            for idx in range(self.component_num[i]):
                e1 = tk.StringVar()
                entry_list.append(tk.Entry(show_frame, textvariable=e1))
            self.entry_dict[i] = entry_list
            button_list.append(tk.Button(show_frame, text='新建',
                               command=partial(self.addEntryNum, i)))
        self.row = 0
        label = tk.Label(show_frame, text='名称')
        label.grid(row=self.row, column=0)
        e = tk.StringVar()
        self.operator_name_entry = tk.Entry(show_frame, textvariable=e)
        self.operator_name_entry.grid(row=self.row, column=1)
        self.row += 1
        for i in range(len(self.label_text)):
            self.label_dict[i].grid(row=self.row, column=0)
            self.row += 1
            entry_list = self.entry_dict[i]
            for idx in range(len(entry_list)):
                if idx != 0 and idx % 2 == 0:
                    self.row += 1
                entry_list[idx].grid(row=self.row, column=(idx+1) % 2+1)
            button_list[i].grid(row=self.row, column=3)
            self.row += 1
        submit_button = tk.Button(show_frame, text='添加', command=self.submitOperator)
        submit_button.grid(row=self.row, column=1)
        show_canvas.create_window((0, 0), window=show_frame, anchor='nw')
        self.print_attr_window.update()
        show_canvas.config(scrollregion=show_canvas.bbox('all'))
        show_scrollbar.pack(side='left', fill='y')
        show_canvas.pack()
        self.print_attr_window.mainloop()

    def submitOperator(self):
        operator = Operator()
        name = self.operator_name_entry.get()
        operator.Insert(DEVICE_BASIC, 's_name', name)
        for i in range(len(self.component_num)):
            entry_list = self.entry_dict[i]
            for idx in range(int(len(entry_list)/2)):
                key = entry_list[idx].get()
                value = entry_list[idx+1].get()
                operator.Insert(i, key, value)
        self.factory.insert(operator)
        self.listbox.insert(0, self.operator_name_entry.get())

    def addEntryNum(self, i):
        self.print_attr_window.destroy()
        self.component_num[i] += 2
        self.create_sub_window()

    def initOperator(self, factory):
        self.factory = factory
        name_list = self.factory.getNames()
        for name in name_list:
            self.listbox.insert(0, name)

    def packModule(self):
        self.listbox.pack()
        self.add_operator_button.pack()
        self.left_canvas.pack(side='left', fill='both', expand=True)
        self.member_frame.pack(side='top')

    def Run(self):
        self.top.mainloop()

    def initAction(self):
        self.listbox.bind('<<ListboxSelect>>', self.__listBoxSelect)

    def __listBoxSelect(self, event):
        print_attr_window = tk.Toplevel()
        show_scrollbar = tk.Scrollbar(print_attr_window)
        show_canvas = tk.Canvas(print_attr_window, width=800, height=600,
                                bg='black', yscrollcommand=show_scrollbar.set)
        show_scrollbar.config(command=show_canvas.yview)
        show_frame = tk.Frame(show_canvas, bg='black', width=800, height=600)
        self.component_num = [2] * 6
        name = self.listbox.get(self.listbox.curselection())
        operator = self.factory.getOperator(name)
        self.row = 0
        for i in range(len(self.component_num)):
            self.label_dict[i] = tk.Label(show_frame, text=self.label_text[i])
            self.label_dict[i].grid(row=self.row, column=0)
            if i == 0:
                self.__addAttribute(i, show_frame, operator.device_basic_attributes)
            elif i == 1:
                self.__addAttribute(i, show_frame, operator.device_part_attributes)
            elif i == 2:
                self.__addAttribute(i, show_frame, operator.status_attributes)
            elif i == 3:
                self.__addAttribute(i, show_frame, operator.geometry_attributes)
            elif i == 4:
                self.__addAttribute(i, show_frame, operator.func_attributes)
            elif i == 5:
                self.__addAttribute(i, show_frame, operator.network_relation_attributes)
        show_canvas.create_window((0, 0), window=show_frame, anchor='nw')
        print_attr_window.update()
        show_canvas.config(scrollregion=show_canvas.bbox('all'))
        show_scrollbar.pack(side='left', fill='y')
        show_canvas.pack()
        print_attr_window.mainloop()

    def __addAttribute(self, device_type, window, operator_dict):
        if operator_dict:
            for key in operator_dict:
                e1 = tk.StringVar()
                entry_for_dict_attr = tk.Entry(window, textvariable=e1)
                e1.set(key)
                self.row = self.row + 1
                entry_for_dict_attr.grid(row=self.row, column=1)
                e2 = tk.StringVar()
                entry_for_dict_value = tk.Entry(window, textvariable=e2)
                if hasattr(operator_dict[key], '__call__'):
                    e2.set(operator_dict[key].__name__)
                else:
                    e2.set(operator_dict[key])
                entry_for_dict_value.grid(row=self.row, column=2)
        self.row = self.row + 1

    def __destroy_show_frame(self):
        for widget in self.show_frame.winfo_children():
            widget.destroy()
