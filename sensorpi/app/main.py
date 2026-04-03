from app.config import read_frequency, mqtt_topic, climate_zone_name, send_frequency
from app.tools.log import log
from time import sleep
from app.mqtt.mqtt import pub

class sensorPi:
    def __init__(self, beds: list, scd30: object) -> None:
        self.beds = beds
        self.scd30_sensor = scd30
        # this is a list of Bed objects and the SCD30 sensor object!
        log(
            device=climate_zone_name,
            outcome=True,
            subject='app',
            topic='setup',
            message='Successfully created the sensorPi app!'
        )
        # log the sensorpi is working
        
        self.main_loop()
        # start the app loop
    
    def main_loop(self) -> None:
        ticks_since_lasts_send = 0
        running = True
        
        while running:
            for bed in self.beds: bed.sample_readings()
            # take a reading from every bed and save it

            self.scd30_sensor.read()
            # takes a reading from the SCD30 sensor

            if ticks_since_lasts_send == send_frequency:
                # enough readings have past

                # send the bed data such as soil moisture on the 
                for bed in self.beds: bed.send(f"{mqtt_topic}/bed{bed.bed_number}")

                # loop through every bed sending the collected data as you go
                
                self.scd30_sensor.send(f"{mqtt_topic}/SCD30")
                # send the scd30 sensor data
                
            ticks_since_lasts_send += 1  

            sleep(read_frequency)
            # wait until the next tick in required
