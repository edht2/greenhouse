<h1>Controller PI</h1>
<h2>Setup</h2>

1. Pull the latest version from github `git pull git@github.com:edht2/sensorpi.git`<br>
2. Create and enter virtual environment `python3 -m venv .venv && source .venv/bin/activate`
3. Install requirements `pip install -r requirements.txt`
4. OPTIONAL: Configure settings in `/config/state.json` and `/config/config.py`
5. Start the app! `python3 run.py`

<h2>Settings</h2>

All settings are handeled in `/config`. These are things such as tick frequency, temperature sensitivity, beds, actuators and safe mode. Configuration done in `/config/config.py` should be setup <b>before</b> starting the app. Most settings can be changed via the webapp.

<h2>MQTT</h2>

By default, the app uses `mqtt.eclipseprojects.io` as an MQTT broker. However it is recomended to use you own to secure the app. This can be changed in `/config/config.py`.

<h2>Sensors</h2>

The controller PI is expected to have a barometric pressure sensor connected via I²C. Other than that, all sensor data is sent either via a weather API or from the sensor PIs