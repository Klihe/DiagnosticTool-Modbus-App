from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QLineEdit, QPushButton
from PyQt6.QtGui import QIntValidator

class TableLine(QWidget):
    def __init__(self, group: str, physical_address: str, logical_address: str, value: str, value_changed: str, value_compare: str, name: str, description: str, notes: str) -> None:
        super().__init__()
        
        self.__group = group
        self.__physical_address = physical_address
        self.__logical_address = logical_address
        self.__value = value
        self.__value_changed = value_changed
        self.__value_compare = value_compare
        self.__name = name
        self.__description = description
        self.__notes = notes
        
        self.__create()
        
    def __create(self) -> None:
        self.__layout = QHBoxLayout()
        
        self.__group_label = QLabel(self.__group)
        self.__physical_address_label = QLabel(self.__physical_address)
        self.__logical_address_label = QLabel(self.__logical_address)
        
        if self.__name == "Coil" or self.__name == "Discrete Input":
            self.__value_label = QLabel(self.__value)
        else:
            self.__value_edit = QLineEdit(self.__value)
            self.__value_edit.setObjectName(self.__name + "_value_edit")
            self.__value_edit.setValidator(QIntValidator(0, 65535))
            
        self.__value_changed_label = QLabel(self.__value_changed)
        self.__value_compare_label = QLabel(self.__value_compare)
        
        self.__save_check_button = QPushButton()
        self.__save_check_button.setObjectName(self.__name + "_save_check_button")
        self.__save_check_button.setCheckable(True)
        self.__save_check_button.setChecked(True)
        
        self.__in_graph_button = QPushButton()
        self.__in_graph_button.setObjectName(self.__name + "_in_graph_button")
        self.__in_graph_button.setCheckable(True)
        self.__in_graph_button.setChecked(False)
        
        self.__name_edit = QLineEdit(self.__name)
        self.__description_edit = QLineEdit(self.__description)
        self.__notes_edit = QLineEdit(self.__notes)