""" Simple utility to help calibrate the chirp sensors """

from app.sensors.Chirp.chirp_firmware import Chirp
from colorama import Fore

addr = input("Address of target sensor, eg. 0x20 (leave blank if you're not sure)\n>").strip().lower()
if addr == "": addr = "0x20"

# Default address of Chirp seensor is 0x20
# Create an interface with the sensor

try:
    chirp = Chirp(bus=1, address=addr)
    chirp.version
    
except PermissionError as pe:
    print(f"No Chirp device found! {Fore.YELLOW}hint: Check I²C is enabled! Use `raspi-config` to enable{Fore.RESET}")
    raise PermissionError

except IOError as ioe:
    print(f"No Chirp device found! {Fore.YELLOW}hint: Check you are probing the correct address. Use `i2cdetect -y 1` from i2c-tools library to probe all addresses{Fore.RESET}")
    raise IOError

# Read min and max moisture
input("Ensure the sensor is completely dry then press enter")
chirp.trigger()
min_moist = chirp.moist

input("Place the sensor in water, ensure it is submerged up to the black solder sleve, then press enter")
chirp.trigger()
max_moist = chirp.moist

# Print the sensor readings range
print(f"Range: {min_moist} - {max_moist}\nAdd to `app/config.py`")
