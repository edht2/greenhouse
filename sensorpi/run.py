""" This creates a listener waiting for a config from the controller pi then sends another message requesting this config. """

from colorama import Style, Fore, Back
from app.config import climate_zone_name, climate_zone_number, chirpsensor_i2c_address, chirp_sensor_cal, bed_num
from app.main import sensorPi
from app.tools.sensors import instantiate_sensors

if __name__ == "__main__":
    print(f"{Back.GREEN}{Fore.WHITE}Initiating {climate_zone_name}...{Style.RESET_ALL}")
    
    ### TO CONFIGURE SENSORS UNCOMMENT ###
    import utilities.switch_address_chirp
    # import utilities.calibrate_chirp
    ######################################

    """ create a dictionary for the climate zone which includes the bed id numbers, the i2c addresses for each of the 
        soil moisture sensors and the calibration data for them. """

    beds_dictionary = {"beds" : []}
    # create a dictionary with one item called beds which is an empty list

    for x in range(len(bed_num)): 
    # loop x times to reflect the number of beds in each climate zone. 
        
        bed = dict(chirp_sensor_i2c_address = chirpsensor_i2c_address[x], 
                chirp_sensor_calibration = chirp_sensor_cal[x], 
                bed_number = bed_num[x], 
                mqtt_topic = f"bed{bed_num[x]}")
        # create a 'bed' dictionary to describe individual beds with attributes from config.py 
        
        beds_dictionary["beds"].append(bed)
        # append each 'bed' dictionary to the 'beds' list in beds_dictionary


    beds, scd30 = instantiate_sensors(beds_dictionary, climate_zone_number)
    # get the arguments for the beds and scd30)

    sensorPi(beds=beds, scd30=scd30)
    # instantiate the sensor pi
