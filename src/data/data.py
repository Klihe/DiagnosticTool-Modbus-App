import pandas as pd
import csv

class Data:
    def __init__(self) -> None:
        self.data = None
    
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
    
    def save(self) -> None:
        pass
    
    def saveas(self) -> None:
        pass
    
    def load(self) -> None:
        pass