from typing import Final

#
# USER CONFIGURATION SECTION
# Select one or more options to enable
#
CSV_FILE_ENABLED = 1

EMAIL_SMS_ENABLED = 1

IP_PORT_ENABLED = 0  # Future

# MQTT
MQTT_ENABLED = 0
MQTT_HOST = "localhost"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_USERNAME = None
MQTT_PASSWORD = None

# INFLUX_DB
INFLUX_DB_ENABLED = 0
INFLUX_HOST = "192.168.100.11"
INFLUX_PORT = 8086  # default port
INFLUX_USER = "rpi"  # requires write access
INFLUX_PASSWORD = "rpi"
INFLUX_DBNAME = "sensor_data"

# BUZZER
BUZZER_ENABLED = 0
buzzerPIN = 18  # Customize based on your wiring

AIRTHINGS = 0  # Default = 0, which is monitoring and logging disabled

HOME_ASSISTANT_DISCOVERY = (
    0  # Set to 1 to enable Home Assistant MQTT discovery topic creation
)

AIRTHINGS_SERIAL = None # If multiple Airthings sensors, set this to the serial number of the device to monitor

# --- END USER CONFIGURATION ---


# Destinations
MQTT = "MQTT"
CSV_FILE = "CSV_FILE"
EMAIL_SMS = "EMAIL_SMS"
INFLUX_DB = "INFLUX_DB"
BUZZER = "BUZZER"

MQTT_SENSORS = {
    "pressure": {
        "device_class": "pressure",
        "unit_of_measurement": "psi",
        "name": "Pressure",
        "state_topic": "RadonMaster/PresSensor",
        "value_template": "{{ value_json.psi }}",
        "suggested_display_precision": 4,
    },
    "pressure_inwc": {
        "unit_of_measurement": "in. wc",
        "name": "Pressure_wc",
        "state_topic": "RadonMaster/PresSensor",
        "value_template": "{{ value_json.data }}",
        "device_class": None,
        "suggested_display_precision": 2,
    },
}

AIRTHINGS_SENSORS = {
    "radon_st_avg": {
        "unit_of_measurement": "Bq/m3",
        "name": "Radon Short Term",
        "state_topic": "RadonMaster/WavePlus",
        "value_template": "{{ value_json.radon_st_avg }}",
        "device_class": None,
        "suggested_display_precision": 2,
    },
    "radon_lt_avg": {
        "unit_of_measurement": "Bq/m3",
        "name": "Radon Long Term",
        "state_topic": "RadonMaster/WavePlus",
        "value_template": "{{ value_json.radon_lt_avg }}",
        "device_class": None,
        "suggested_display_precision": 2,
    },
    "voc": {
        "unit_of_measurement": "ppb",
        "name": "VOC",
        "state_topic": "RadonMaster/WavePlus",
        "value_template": "{{ value_json.voc }}",
        "device_class": "volatile_organic_compounds_parts",
        "suggested_display_precision": 2,
    },
    "co2": {
        "unit_of_measurement": "ppm",
        "name": "CO2",
        "state_topic": "RadonMaster/WavePlus",
        "value_template": "{{ value_json.co2 }}",
        "device_class": "carbon_dioxide",
        "suggested_display_precision": 2,
    },
    "temperature": {
        "unit_of_measurement": "°C",
        "name": "Temperature",
        "state_topic": "RadonMaster/WavePlus",
        "value_template": "{{ value_json.temperature }}",
        "device_class": "temperature",
        "suggested_display_precision": 1,
    },
    "humidity": {
        "unit_of_measurement": "%",
        "name": "Humidity",
        "state_topic": "RadonMaster/WavePlus",
        "value_template": "{{ value_json.humidity }}",
        "device_class": "humidity",
        "suggested_display_precision": 0,
    },
    "pressure_airthings": {
        "unit_of_measurement": "hPa",
        "name": "Airthings Pressure",
        "state_topic": "RadonMaster/WavePlus",
        "value_template": "{{ value_json.pressure_airthings }}",
        "device_class": "pressure",
        "suggested_display_precision": 2,
    },
    "fan": {
        "unit_of_measurement": "%",
        "name": "Fan",
        "state_topic": "RadonMaster/WavePlus",
        "value_template": "{{ value_json.fan }}",
        "device_class": None,
        "suggested_display_precision": 0,
    },
}
