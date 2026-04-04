""" A class containing the whole greenhouse """
from app.config.config import state, update_frequency
from app.climate_zone import ClimateZone
from app.tools.log import log
from datetime import datetime
from time import sleep
from os import system

class Greenhouse:
    
    def __init__(self) -> None:
        
        print(f'\n{"—" * 40} GREEN-HOUSE INITIALISING {"—" * 40}\n')
        
        self.climate_zones = [ClimateZone(climate_zone["climateZoneNumber"]) for climate_zone in state]
        # create the climate zone object
        
        self.tick_count = 1
        
        log('OK', "greenhouse", "init", "App has been successfuly setup")
        

    def update(self) -> None:
        for climate_zone in self.climate_zones:
            climate_zone.update()
            # look at the sensor values, what is going on? fix it.
            
        self.tick_count += 1
     
    def start_app_loop(self) -> None:
        
        while True:
            
            try:
                print(f"\n{'—' * 45} TICK {self.tick_count} {'—' * (46 - len(str(self.tick_count)))}\n")
                
                
                log('WAIT', "greenhouse", "app-loop", "Triggering new update")
                self.update() # trigger an update
                
                log('OK', "greenhouse", "app-loop", "Successfuly performed an update")               
                
            except Exception as e:
                
                log('FATAL', "greenhouse", "app-loop", "Failed to perform update", error=e)
                # Oh no! A fatal error has occured!
                
                # to avoid potential dangers to the green-house it is cruitial that all watering soloids and windows are closed
                for climate_zone in self.climate_zones:
                    
                    for bed in climate_zone.beds:
                        
                        bed.watering_solenoid.close()
                        # this will close all watering solenoids
                    
                    for window in climate_zone.side_windows + climate_zone.top_windows:
                        
                        window.retract()
                        # close all windows

            sleep(update_frequency)
            
            if datetime.now().hour == 0 and datetime.now().minute == 0 and datetime.now().second <= 30:
                # if it is midnight restart the app
                system('reboot') # restarts the rpi
                
                """ The controller pi software is a startup application therefore it will automatically run again after restart """