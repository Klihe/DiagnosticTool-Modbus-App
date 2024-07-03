from PyQt6.QtWidgets import QLabel, QLineEdit, QComboBox, QPushButton

import window.valuesgroup.constants as c

class ValuesSearch:
    def __init__(self, items: list[str]) -> None:
        self.__items = items
        
        self.__create()
        
    def __create(self) -> None:
        self.__search_combobox = QComboBox()
        self.__search_combobox.addItems(self.__items)
        
        self.__search_edit = QLineEdit()
        self.__search_edit.setPlaceholderText("Search")
        
        self.__search_button = QPushButton("Search")
        
    def addSearch(self, layout, row: int) -> None:
        self.__layout = layout
        self.__row = row
        
        self.__layout.addWidget(self.__search_combobox, self.__row, 0)
        self.__layout.addWidget(self.__search_edit, self.__row, 1)
        self.__layout.addWidget(self.__search_button, self.__row, 2)
        
class ValuesDescr:
    def __init__(self, label1: str="group", label2: str="phy_addr", label3: str="log_addr", label4: str="value", label5: str="name", label6: str="description", label7: str="notes") -> None:
        self.__label1 = label1
        self.__label2 = label2
        self.__label3 = label3
        self.__label4 = label4
        self.__label5 = label5
        self.__label6 = label6
        self.__label7 = label7
        
        self.__create()
        
    def __create(self) -> None:
        self.__group_label = QLabel(self.__label1)
        self.__group_label.setFixedSize(100, 20)
        
        self.__physical_address_label = QLabel(self.__label2)
        self.__physical_address_label.setFixedSize(100, 20)
        
        self.__logical_address_label = QLabel(self.__label3)
        self.__logical_address_label.setFixedSize(100, 20)
        
        self.__value_label = QLabel(self.__label4)
        self.__value_label.setFixedSize(100, 20)
        
        self.__name_label = QLabel(self.__label5)
        self.__name_label.setFixedSize(100, 20)
        
        self.__description_label = QLabel(self.__label6)
        self.__description_label.setFixedSize(100, 20)
        
        self.__notes_label = QLabel(self.__label7)
        self.__notes_label.setFixedSize(100, 20)
        
    def addDescr(self, layout, row: int) -> None:
        self.__layout = layout
        self.__row = row
        
        self.__layout.addWidget(self.__group_label, self.__row, 0)
        self.__layout.addWidget(self.__physical_address_label, self.__row, 1)
        self.__layout.addWidget(self.__logical_address_label, self.__row, 2)
        self.__layout.addWidget(self.__value_label, self.__row, 3)
        self.__layout.addWidget(self.__name_label, self.__row, 4)
        self.__layout.addWidget(self.__description_label, self.__row, 5)
        self.__layout.addWidget(self.__notes_label, self.__row, 6)
        
class ValuesLine:
    def __init__(self, group: str, physical_address: str, logical_address: str, value: str, name: str, description: str, notes: str):
        self.__group = group
        self.__physical_address = physical_address
        self.__logical_address = logical_address
        self.__value = value
        self.__name = name
        self.__description = description
        self.__notes = notes
        
        self.__create()
        
    def __create(self) -> None:
        self.__group_label = QLabel(self.__group)
        self.__physical_address_label = QLabel(self.__physical_address)
        self.__logical_address_label = QLabel(self.__logical_address)
        
        if self.__group == c.NAME_1 or self.__group == c.NAME_2:
            self.__value_edit = QLineEdit(self.__value)
        else:
            self.__value_label = QLabel(self.__value)
            
        self.__name_edit = QLineEdit(self.__name)
        self.__description_edit = QLineEdit(self.__description)
        self.__notes_edit = QLineEdit(self.__notes)
    
    def addLine(self, layout, row: int) -> None:
        self.__layout = layout
        self.__row = row
        
        self.__layout.addWidget(self.__group_label, self.__row, 0)
        self.__layout.addWidget(self.__physical_address_label, self.__row, 1)
        self.__layout.addWidget(self.__logical_address_label, self.__row, 2)
        
        if self.__group == c.NAME_1 or self.__group == c.NAME_2:
            self.__layout.addWidget(self.__value_edit, self.__row, 3)
        else:
            self.__layout.addWidget(self.__value_label, self.__row, 3)
            
        self.__layout.addWidget(self.__name_edit, self.__row, 4)
        self.__layout.addWidget(self.__description_edit, self.__row, 5)
        self.__layout.addWidget(self.__notes_edit, self.__row, 6)
        
class ValuesGroup:
    def __init__(self) -> None:
        self.__lines = []
        
        self.__search = ValuesSearch(items=['group', 'physical address', 'logical address', 'value', 'name', 'description', 'notes'])
        self.__descr = ValuesDescr()
        
        for _ in range(10):
            line = ValuesLine(
                group='None',
                physical_address='None',
                logical_address='None',
                value='None',
                name='None',
                description='None',
                notes='None'
            )
            
            self.__lines.append(line)
            
    def addGroup(self, layout) -> None:
        self.__search.addSearch(layout=layout, row=c.SEARCH_POSITION)
        self.__descr.addDescr(layout=layout, row=c.DESCR_POSITION)
        
        for row, line in enumerate(self.__lines):
            line.addLine(layout=layout, row=row+c.VALUES_POSITION)