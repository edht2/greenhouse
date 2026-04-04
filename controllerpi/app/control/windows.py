#from app.tools.safe_window_validator import safe_window_validator
from app.control.actuator import Actuator
from app.config.config import state

def safe_window_validator(*args) -> bool: return True

class WindowGroup:
    
    def __init__(self, window: str, clid: int) -> None:
        
        self.window_type = window
        self.climate_zone_number = clid
        
        self.acctuators = [
            Actuator([
                actuator["actuatorRelayIndexExtend"], 
                actuator["actuatorRelayIndexRetract"]],
                extension_time=40
        ) for actuator in state[self.climate_zone_number-1][window]]
        # creates all of the windows in the actuator class so you can type 'side_window[index].extend()'
        
    def open(self, asnc=True) -> None:
        # opens all windows
        
        if safe_window_validator(self.window_type):
            # if it is safe to open the top windows
            
            for window in self.acctuators: window.extend(asnc)
            # open all of the windows
            
    def close(self, asnc=True) -> None:
        # closes all windows
        
        if safe_window_validator(self.window_type):
            # if it is safe to open the top windows
            
            for window in self.acctuators: window.retract(asnc)