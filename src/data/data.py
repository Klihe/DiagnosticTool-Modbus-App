import pandas as pd

class Data:
    def __init__(self) -> None:
        self.data = None
    
    def read(self, file_path: str) -> None:
        self.__file_path = file_path
        
        self.data = pd.read_csv(self.__file_path, sep=";")
    
    def readInInterval(self) -> None:
        pass
    
    def write(self) -> None:
        pass
    
    def save(self) -> None:
        pass
    
    def saveas(self) -> None:
        pass
    
    def load(self) -> None:
        pass