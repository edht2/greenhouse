from app.sensors.Chirp.chirp_sensor import ChirpSensor
from app.mqtt.mqtt import pub
from app.tools.utils import utils
from app.tools.log import log
from app.config import climate_zone_name
from json import dumps

class Bed:
    def __init__(self, chirp_sensor_I2C_address, chirp_sensor_calibration, bed_number) -> None:        
        self.bed_number = bed_number
        
        self.chirp_sensor = ChirpSensor(
            I2C_address=chirp_sensor_I2C_address,
            number=self.bed_number,
            min_moist=chirp_sensor_calibration[0],
            max_moist=chirp_sensor_calibration[1]
        )

        # create the sensor object, used for sampling readings
        
        self.soil_moisture_readings = []
        self.temperature_readings = []
        self.status = "OK"
    
    def sample_readings(self) -> None:
        try:
            reading = self.chirp_sensor.read()
            # trigger a reading
            
            self.soil_moisture_readings.append(reading[0])
            self.temperature_readings.append(reading[1])
        
            # add the read sensor values to a list from which we can take the median
            # do this to flatten any volatility from the capactitive readings
        except Exception as e:
            log(
                device=climate_zone_name,
                outcome=False,
                subject="bed",
                topic="chirp_sensor_reading", 
                message="Error while trying to read sensor data",
                error=e
            )
            # if the sensor fails to read
            
            self.status = "ER"
            # by setting the status to 'ER', the controller pi now knows to stop using this soil moisture sensor, and instead uses the clock.
         
    def send(self, mqttTopic: str) -> None:
        message = dumps({
            "median_soil_moist" : f"{utils.median(self.soil_moisture_readings):.1f}",
            "median_temp" : f"{utils.median(self.temperature_readings):.1f}",
            "status" : self.status
        })
        self.soil_moisture_readings, self.temperature_readings = [], []
        # clear the reading lists
        
        print(message)
        pub.publish(mqttTopic, message)
        # send the packet to the controller pi


    def identify(self) -> str:
        return f"This is the bed to which I am linked {self.number}"
