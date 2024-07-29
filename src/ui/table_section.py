from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QLineEdit, QPushButton, QLayout, QScrollArea, QVBoxLayout, QComboBox
from PyQt6.QtGui import QIntValidator

class TableSearch(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.__create()
        
    def __create(self) -> None:
        self.__item_layout = QHBoxLayout()
        
        self.__search_label = QLabel("Search:")
        self.__search_edit = QLineEdit()
        self.__search_options_box = QComboBox()
        self.__search_button = QPushButton("Search")
        
    def _addSearch(self, layout: QLayout) -> None:
        self.__layout = layout
        
        self.__item_layout.addWidget(self.__search_label)
        self.__item_layout.addWidget(self.__search_edit)
        self.__item_layout.addWidget(self.__search_options_box)
        self.__item_layout.addWidget(self.__search_button)
        
        self.__layout.addLayout(self.__item_layout)

class TableDescription(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.__create()
        
    def __create(self) -> None:
        self.__item_layout = QHBoxLayout()
        
        self.__group_label = QLabel("Group")
        self.__physical_address_label = QLabel("Physical\nAddress")
        self.__logical_address_label = QLabel("Logical\nAddress")
        self.__value_label = QLabel("Value")
        self.__value_changed_label = QLabel("Value Changed")
        self.__value_compare_label = QLabel("Value Compare")
        self.__save_check_label = QLabel("Save Check")
        self.__in_graph_label = QLabel("In Graph")
        self.__name_label = QLabel("Name")
        self.__description_label = QLabel("Description")
        self.__notes_label = QLabel("Notes")
        
        self.__group_label.setFixedSize(100, 30)
        self.__physical_address_label.setFixedSize(50, 30)
        self.__logical_address_label.setFixedSize(50, 30)
        self.__value_label.setFixedSize(100, 30)
        self.__value_changed_label.setFixedSize(100, 30)
        self.__value_compare_label.setFixedSize(100, 30)
        self.__save_check_label.setFixedSize(50, 30)
        self.__in_graph_label.setFixedSize(50, 30)
        self.__name_label.setFixedSize(150, 30)
        self.__description_label.setFixedSize(300, 30)
        self.__notes_label.setFixedSize(100, 30)
        
    def _addDescription(self, layout: QLayout) -> None:
        self.__layout = layout
        
        self.__item_layout.addWidget(self.__group_label)
        self.__item_layout.addWidget(self.__physical_address_label)
        self.__item_layout.addWidget(self.__logical_address_label)
        self.__item_layout.addWidget(self.__value_label)
        self.__item_layout.addWidget(self.__value_changed_label)
        self.__item_layout.addWidget(self.__value_compare_label)
        self.__item_layout.addWidget(self.__save_check_label)
        self.__item_layout.addWidget(self.__in_graph_label)
        self.__item_layout.addWidget(self.__name_label)
        self.__item_layout.addWidget(self.__description_label)
        self.__item_layout.addWidget(self.__notes_label)
        
        self.__layout.addLayout(self.__item_layout)
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
        self.__item_layout = QHBoxLayout()
        
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
        
        self.__group_label.setFixedSize(100, 30)
        self.__physical_address_label.setFixedSize(50, 30)
        self.__logical_address_label.setFixedSize(50, 30)
        if self.__name == "Coil" or self.__name == "Discrete Input":
            self.__value_label.setFixedSize(100, 30)
        else:
            self.__value_edit.setFixedSize(100, 30)
        self.__value_changed_label.setFixedSize(100, 30)
        self.__value_compare_label.setFixedSize(100, 30)
        self.__save_check_button.setFixedSize(50, 30)
        self.__in_graph_button.setFixedSize(50, 30)
        self.__name_edit.setFixedSize(150, 30)
        self.__description_edit.setFixedSize(300, 30)
        self.__notes_edit.setFixedSize(100, 30)
        
    def _addLine(self, layout: QLayout) -> None:
        self.__layout = layout
        
        self.__item_layout.addWidget(self.__group_label)
        self.__item_layout.addWidget(self.__physical_address_label)
        self.__item_layout.addWidget(self.__logical_address_label)
        
        if self.__name == "Coil" or self.__name == "Discrete Input":
            self.__item_layout.addWidget(self.__value_label)
        else:
            self.__item_layout.addWidget(self.__value_edit)
            
        self.__item_layout.addWidget(self.__value_changed_label)
        self.__item_layout.addWidget(self.__value_compare_label)
        self.__item_layout.addWidget(self.__save_check_button)
        self.__item_layout.addWidget(self.__in_graph_button)
        self.__item_layout.addWidget(self.__name_edit)
        self.__item_layout.addWidget(self.__description_edit)
        self.__item_layout.addWidget(self.__notes_edit)
        
        self.__layout.addLayout(self.__item_layout)
        
class TableGrid(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.__create()
        
    def __create(self) -> None:
        self.__line1 = TableLine("Group", "Physical Address", "Logical Address", "Value", "Value Changed", "Value Compare", "Name", "Description", "Notes")
    
    def _addGrid(self, layout: QLayout) -> None:
        self.__layout = layout
        
        self.__line1._addLine(self.__layout)
        
class TableSection(QWidget):
    def __init__(self, config: dict) -> None:
        super().__init__()
        
        self.__config = config
        
        self.__create()
        
    def __create(self) -> None:
        self.__scroll_area = QScrollArea()
        self.__scroll_area.setWidgetResizable(True)
        
        self.__grid_container = QWidget()
        self.__grid_layout = QVBoxLayout(self.__grid_container)
        
        self.__search = TableSearch()
        self.__description = TableDescription()
        self.__grid = TableGrid()
        
    def addSection(self, layout: QLayout) -> None:
        self.__layout = layout
        
        self.__search._addSearch(self.__layout)
        self.__description._addDescription(self.__layout)
        self.__grid._addGrid(self.__grid_layout)
        self.__scroll_area.setWidget(self.__grid_container)
        
        self.__layout.addWidget(self.__scroll_area)