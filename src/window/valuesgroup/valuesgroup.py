from PyQt6.QtWidgets import QLabel, QLineEdit, QComboBox, QPushButton, QGridLayout, QHBoxLayout, QScrollArea, QWidget, QLayout

import window.valuesgroup.constants as c

class ValuesSearch:
    def __init__(self, grabber: dict, items: list[str]) -> None:
        self.__grabber = grabber
        
        self.__items = items
        
        self.__create()
        
    def __create(self) -> None:
        self.__grabber["search_entry"] = QComboBox()
        self.__grabber["search_entry"].addItems(self.__items)
        
        self.__grabber["search_edit"] = QLineEdit()
        self.__grabber["search_edit"].setPlaceholderText("Search")
        
        self.__grabber["search_btn"] = QPushButton("Search")
        
    def _addSearch(self, layout: QLayout) -> None:
        self.__layout = layout
        
        self.__layout.addWidget(self.__grabber["search_entry"])
        self.__layout.addWidget(self.__grabber["search_edit"])
        self.__layout.addWidget(self.__grabber["search_btn"])
        
class ValuesDescr:
    def __init__(self, grabber: dict, items: list[str]) -> None:
        self.__grabber = grabber
        
        self.__label1 = items[0]
        self.__label2 = items[1]
        self.__label3 = items[2]
        self.__label4 = items[3]
        self.__label5 = items[4]
        self.__label6 = items[5]
        self.__label7 = items[6]
        
        self.__create()
        
    def __create(self) -> None:
        self.__grabber["value_descr_item1"] = QLabel(self.__label1)
        self.__grabber["value_descr_item1"].setFixedSize(100, 20)
        
        self.__grabber["value_descr_item2"] = QLabel(self.__label2)
        self.__grabber["value_descr_item2"].setFixedSize(100, 20)
        
        self.__grabber["value_descr_item3"] = QLabel(self.__label3)
        self.__grabber["value_descr_item3"].setFixedSize(100, 20)
        
        self.__grabber["value_descr_item4"] = QLabel(self.__label4)
        self.__grabber["value_descr_item4"].setFixedSize(100, 20)
        
        self.__grabber["value_descr_item5"] = QLabel(self.__label5)
        self.__grabber["value_descr_item5"].setFixedSize(100, 20)
        
        self.__grabber["value_descr_item6"] = QLabel(self.__label6)
        self.__grabber["value_descr_item6"].setFixedSize(100, 20)
        
        self.__grabber["value_descr_item7"] = QLabel(self.__label7)
        self.__grabber["value_descr_item7"].setFixedSize(100, 20)
        
    def _addDescr(self, layout: QLayout) -> None:
        self.__layout = layout
        
        self.__layout.addWidget(self.__grabber["value_descr_item1"])
        self.__layout.addWidget(self.__grabber["value_descr_item2"])
        self.__layout.addWidget(self.__grabber["value_descr_item3"])
        self.__layout.addWidget(self.__grabber["value_descr_item4"])
        self.__layout.addWidget(self.__grabber["value_descr_item5"])
        self.__layout.addWidget(self.__grabber["value_descr_item6"])
        self.__layout.addWidget(self.__grabber["value_descr_item7"])
        
class ValuesLine:
    def __init__(self, grabber: dict, group: str, physical_address: str, logical_address: str, value: str, name: str, description: str, notes: str, id: int) -> None:
        self.__grabber = grabber
        
        self.__group = group
        self.__physical_address = physical_address
        self.__logical_address = logical_address
        self.__value = value
        self.__name = name
        self.__description = description
        self.__notes = notes
        self.__id = id
        
        self.__create()
        
    def __create(self) -> None:
        self.__group_label = QLabel(self.__group)
        self.__physical_address_label = QLabel(self.__physical_address)
        self.__logical_address_label = QLabel(self.__logical_address)
        
        if self.__group == c.NAME_1 or self.__group == c.NAME_2:
            self.__grabber[f"value_edit_{self.__id}"] = QLineEdit(self.__value)
        else:
            self.__value_label = QLabel(self.__value)
            
        self.__grabber[f"name_edit_{self.__id}"] = QLineEdit(self.__name)
        self.__grabber[f"descr_edit_{self.__id}"] = QLineEdit(self.__description)
        self.__grabber[f"note_edit_{self.__id}"] = QLineEdit(self.__notes)
        
    def _updateLine(self, data) -> None:
        print("update")
        self.__group_label.setText(str(data["group"]))
        self.__physical_address_label.setText(str(data["physical_address"]))
        self.__logical_address_label.setText(str(data["logical_address"]))
        
        if self.__group == c.NAME_1 or self.__group == c.NAME_2:
            self.__grabber[f"value_edit_{self.__id}"].setText(str(data["value"]))
        else:
            self.__value_label.setText(str(data["value"]))
            
        self.__grabber[f"name_edit_{self.__id}"].setText(str(data["name"]))
        self.__grabber[f"descr_edit_{self.__id}"].setText(str(data["description"]))
        self.__grabber[f"note_edit_{self.__id}"].setText(str(data["notes"]))
    
    def _addLine(self, layout, row: int) -> None:
        self.__layout = layout
        self.__row = row
        
        self.__layout.addWidget(self.__group_label, self.__row, 0)
        self.__layout.addWidget(self.__physical_address_label, self.__row, 1)
        self.__layout.addWidget(self.__logical_address_label, self.__row, 2)
        
        if self.__group == c.NAME_1 or self.__group == c.NAME_2:
            self.__layout.addWidget(self.__grabber[f"value_edit_{self.__id}"], self.__row, 3)
        else:
            self.__layout.addWidget(self.__value_label, self.__row, 3)
            
        self.__layout.addWidget(self.__grabber[f"name_edit_{self.__id}"], self.__row, 4)
        self.__layout.addWidget(self.__grabber[f"descr_edit_{self.__id}"], self.__row, 5)
        self.__layout.addWidget(self.__grabber[f"note_edit_{self.__id}"], self.__row, 6)
        
    def __del__(self) -> None:
        self.__layout.removeWidget(self.__group_label)
        self.__layout.removeWidget(self.__physical_address_label)
        self.__layout.removeWidget(self.__logical_address_label)
        
        if self.__group == c.NAME_1 or self.__group == c.NAME_2:
            self.__layout.removeWidget(self.__grabber[f"value_edit_{self.__id}"])
        else:
            self.__layout.removeWidget(self.__value_label)
        
        self.__layout.removeWidget(self.__grabber[f"name_edit_{self.__id}"])
        self.__layout.removeWidget(self.__grabber[f"descr_edit_{self.__id}"])
        self.__layout.removeWidget(self.__grabber[f"note_edit_{self.__id}"])
        
        self.__group_label.deleteLater()
        self.__physical_address_label.deleteLater()
        self.__logical_address_label.deleteLater()
        
        if self.__group == c.NAME_1 or self.__group == c.NAME_2:
            self.__grabber[f"value_edit_{self.__id}"].deleteLater()
        else:
            self.__value_label.deleteLater()
        
        self.__grabber[f"name_edit_{self.__id}"].deleteLater()
        self.__grabber[f"descr_edit_{self.__id}"].deleteLater()
        self.__grabber[f"note_edit_{self.__id}"].deleteLater()
        
class ValuesGrid:
    def __init__(self, grabber: dict) -> None:
        self.__grabber = grabber
        
        self.__lines = []
        
        self.__create()
    
    def __create(self) -> None:
        for _ in range(29):
            line = ValuesLine(
                grabber=self.__grabber,
                group='None',
                physical_address='None',
                logical_address='None',
                value='None',
                name='None',
                description='None',
                notes='None',
                id=_
            )
            
            self.__lines.append(line)
            
    def _updateGrid(self, data) -> None:
        self._clearGrid()
        
        for i in range(len(data["group"][:])):
            line = ValuesLine(
                grabber=self.__grabber,
                group=str(data["group"][i]),
                physical_address=str(data["physical_address"][i]),
                logical_address=str(data["logical_address"][i]),
                value=str(data["value"][i]),
                name=str(data["name"][i]),
                description=str(data["description"][i]),
                notes=str(data["notes"][i]),
                id=i
            )
            
            self.__lines.append(line)
            
    def _addGrid(self, layout: QLayout) -> None:
        self.__layout = layout
        
        for row, line in enumerate(self.__lines):
            line._addLine(layout=self.__layout, row=row)
            
    def _clearGrid(self) -> None:
        for line in self.__lines:
            del line
            
        self.__lines.clear()
        
class ValuesGroup:
    def __init__(self, grabber: dict) -> None:
        self.__grabber = grabber
        
        self.__create()
        
    def __create(self) -> None:
        self.__scroll_area = QScrollArea()
        self.__scroll_area.setWidgetResizable(True)
        
        self.__search_layout = QHBoxLayout()
        self.__descr_layout = QHBoxLayout()
        
        self.__grid_container = QWidget()
        self.__grid_layout = QGridLayout(self.__grid_container)
        
        self.__search = ValuesSearch(self.__grabber, c.ITEMS)
        self.__descr = ValuesDescr(self.__grabber, c.ITEMS)
        self.__grid = ValuesGrid(self.__grabber)
        
    def update(self, data) -> None:
        self.__grid._updateGrid(data)
        
        self.addGroup(self.__layout)
            
    def addGroup(self, layout: QLayout) -> None:
        self.__layout = layout
        
        self.__search._addSearch(self.__search_layout)
        self.__descr._addDescr(self.__descr_layout)
        self.__grid._addGrid(self.__grid_layout)
        
        self.__scroll_area.setWidget(self.__grid_container)
        
        self._addLayout()
        
    def _addLayout(self) -> None:
        self.__layout.addLayout(self.__search_layout)
        self.__layout.addLayout(self.__descr_layout)
        
        self.__layout.addWidget(self.__scroll_area)
        