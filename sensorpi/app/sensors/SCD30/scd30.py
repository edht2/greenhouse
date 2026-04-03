from app.config import read_frequency
from scd30_i2c import SCD30 as SCD30driver
from app.tools.utils import utils
from app.mqtt.mqtt import pub
from json import dumps
import time

class SCD30:
    def __init__(self, climate_zone_id):
        self.climate_zone_id = climate_zone_id
        self.scd30 = SCD30driver()
        self.scd30.set_measurement_interval(read_frequency)
        # start reading from the scd30 sensor at the rate defined in config ('read_frequency')
        self.scd30.start_periodic_measurement()
        # start taking readings

        self.CO2_readings = []
        self.temperature_readings = []
        self.RH_readings = []
        # a list of readings

    def read(self):
        try:
            if self.scd30.get_data_ready():
                # if the sensorpi can read the sensor data
                measurements = self.scd30.read_measurement()
                # get the reading from the sensor

            if measurements is not None:
                # if the sensor has acctually worked...  sometimes the sensor just returns 'None'

                self.CO2_readings.append(measurements[0])
                self.temperature_readings.append(measurements[1])
                self.RH_readings.append(measurements[2])
                # add the new results to the lists of readings

                return measurements
                # returns: CO², Temp and RH% in that order!
            else:
                time.sleep(0.2)

                return self.read()

        except:
            # oh no! something went wrong try again
            time.sleep(0.2)
            # wait a bit

        return self.read()

    def send(self, mqtt_topic):
        median_CO2_reading = utils.median(self.CO2_readings)
        median_temperature_reading = utils.median(self.temperature_readings)
        median_RH_reading = utils.median(self.RH_readings)
        # get a median to reduce the effect of outlier data

        self.CO2_readings = []
        self.temperature_readings = []
        self.RH_readings = []
        # reset the values

        message = dumps({
            "median_rh" : f"{median_RH_reading:.1f}",
            "median_temp" : f"{median_temperature_reading:.1f}",
            "median_co2_ppm" : f"{median_CO2_reading:.1f}"
        })

        print(mqtt_topic, message)
        pub.publish(mqtt_topic, message)
 
        # publish the data--dumps turns a python dictionary into a json string

        def stop(self):
            self.scd30.stop_periodic_measurements()
            # if we want to stop the sensor we can

    def identify(self):
        return f"This is the climate_zone to which I am linked {self.climate_zone_id}"