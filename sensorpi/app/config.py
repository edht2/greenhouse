climate_zone_number = 1
# the number assigned to the c.z.

climate_zone_name = f"sensorPi {climate_zone_number}"
# the name of the climate zone

read_frequency = 5
# how often the sensors are triggered

send_frequency = 5
# how often data is sent to the controller pi (how many readings per send)

mqtt_broker_address ="mqtt.eclipseprojects.io"
# the mqtt broker address is a cruicial part of the system allowing the sensor pi
# to communicate with the controller pi

mqtt_topic = f"climate_zone_{climate_zone_number}"
# where all of the data exported is directed through


if climate_zone_number == 1:
    chirpsensor_i2c_address = [0x10,0x11]
    chirp_sensor_cal = [[200, 530],[200, 530]]
    bed_num = [1,2]
    
elif climate_zone_number == 2:
    chirpsensor_i2c_address = [0x30,0x31,0x32,0x33,0x34]
    chirp_sensor_cal = [[200, 530],[200, 530],[200, 530],[200, 530],[200, 530]]
    bed_num = [4,5,6,7,8]
# i2c chirp sensor addresses, calibration for 0% and 100% moisture, plus bed numbers for each of the climate zones.

