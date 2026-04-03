from json import load

device_name = "controllerpi"
# the unique name assigned to the pi

mqtt_broker_address = "mqtt.eclipseprojects.io"
# the broker address used by the greenhouse

update_frequency = 30
# update every 30 seconds

max_ticks_without_data = 2
# after 5 consecutive ticks from a bed without data then go into safe mode

state = load(open("app/config/state.json"))["climateZones"]
# state contains all of the target / hardware information to run the greenhouse

longitude = -1.264416
latitude = 50.747026
# for weather forecast

top_window_extention_time = 60
side_window_extention_time = 40
# so the app can ensure the relay has had time to extend / retract fully

temperature_range_play = 2