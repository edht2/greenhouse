<h1>Sensor PI</h1>

Records and sends sensor data such as bed soil moisture and climate zone humidity

<h2>Setup</h2>

It's recomended to run in a virtual environment!

1. Pull the latest version from github `git pull git@github.com:edht2/sensorpi.git`<br>
2. Create and enter virtual environment `python3 -m venv .venv && source .venv/bin/activate`
3. Install requirements `pip install -r requirements.txt`
4. Configure the app to the climatezone. This may be: Sensor calibration / I²C addresses / ClimateZone id
5. Start the app! `python3 run.py`

<h2>Trouble Shooting</h2>

* It is cruicial to ensure the I²C components are properly configured! If you have just bought a new device, ensure the address is setup correctly. For the Chirp sensors, this can be done with the setup address utility. If the device is incorrectly setup, it will likley throw an IO error (erno 5). All utilities can be accessed by using the python shell. 

<h3>Changing I²C address</h3>

``` bash
python3
>>>import utilities.switch_address_chirp
[Starts address changing script]
```

<h3>Calibrating Chirp sensors</h3>

``` bash
python3
>>>import utilities.calibrate_chirp
[Starts calibration script]
```