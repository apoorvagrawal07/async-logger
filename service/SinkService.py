import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.SinkType import SinkType as stype

class SinkService:
    def sinkOut(self, message, sinkType: stype):
        if(sinkType.name == "STDOUT"):
            print(f"STDOUT - {message}")
        elif sinkType.name == "FILE":
            print(f"File - {message}")


    
