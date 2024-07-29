from PyQt6.QtCore import QThread, pyqtSignal

class CustomThread(QThread):
    finished = pyqtSignal(int)
    
    def __init__(self, target=None, args=(), kwargs={}, *, daemon=None):
        super().__init__()
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._daemon = daemon

    def run(self):
        result = self._target(*self._args, **self._kwargs)
        self.finished.emit(result)
        
    def set_function(self, target, args=(), kwargs={}):
        self._target = target
        self._args = args
        self._kwargs = kwargs
