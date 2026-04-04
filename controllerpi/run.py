from colorama import Style, Fore, Back
from datetime import datetime, timedelta
from app.tools.log import log
from time import sleep

print(f"{Back.GREEN}{Fore.WHITE}Initiating GreenHouse...{Style.RESET_ALL}")
# print a nice log message!

# *** Timing system ***
""" The timing system will ensure the greenhouse will be in sync with real world time
this is useful because it means that restarting at 00:00 (midnight) can be more precise in timing"""
start_time = datetime.now()
start_time += timedelta(seconds=60-start_time.second, microseconds=-start_time.microsecond)
# this affectivly is a ceil opperation to ensure the greenhouse stays in sync with the real time

print(f"Waiting until {Fore.CYAN}{start_time.strftime('%c')}{Style.RESET_ALL}")
#sleep(60 - datetime.now().second)
# /*** Timing system ***


from app.greenhouse import Greenhouse

if __name__ == "__main__":
    greenhouse = Greenhouse()
    # start the greenhouse
    try:
        # This is in a try except to catch KeyboardInterrupts
        greenhouse.start_app_loop()
    finally:
        log("WAIT", "greenhouse", "shutdown", "Safely stopping greenhouse, Ctrl+C again to force stop")
       
        for clz in greenhouse.climate_zones:
            
            # *** Close all windows ***
            clz.side_windows.close()
            clz.top_windows.close()
            
            # *** Close all solenoids ***
            for bed in clz.beds: bed.watering_solenoid.close()
            
            # *** Heating and misting ***
            clz.heating_solenoid.close()
            clz.misting_solenoid.close()
        
        log(True, "greenhouse", "shutdown", "Stopped greenhouse")