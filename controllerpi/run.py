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


from app.green_house import GreenHouse

if __name__ == "__main__":
    green_house = GreenHouse()
    # start the greenhouse
    try:
        green_house.start_app_loop()
    except KeyboardInterrupt:
        log("WAIT", "greenhouse", "shutdown", "Safely stopping greenhouse, Ctrl+C again to force")