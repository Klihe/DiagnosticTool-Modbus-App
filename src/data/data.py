from PyQt6.QtWidgets import QFileDialog
import pandas as pd
import csv


class Data:
    def __init__(self) -> None:
        self.data = None
        self.__current_file_path = None
    
    def read(self, file_path: str) -> None:
        self.__file_path = file_path
        
        self.data = pd.read_csv(self.__file_path, sep=";")
        
    def write(self, file_path: str, data: dict) -> None:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            
            header = data.keys()
            writer.writerow(header)
            
            rows = zip(*data.values())
            writer.writerows(rows)
    
    def save(self, content, window) -> None:
        if not self.__current_file_path:
            self.saveas(content, window)
        else:
            self.write(self.__current_file_path, content)
            print(f"Content saved to: {self.__current_file_path}")
    
    def saveas(self, content, window) -> None:
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(window, "Save File", "", "CSV files (*.csv);;All files (*.*)")
        if file_path:
            self.__current_file_path = file_path
            self.write(self.__current_file_path, content)
            print(f"Content saved to: {self.__current_file_path}")
    
    def load(self, window) -> None:
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(window, "Open File", "", "CSV files (*.csv);;All files (*.*)")
        if file_path:
            self.read(file_path)
    