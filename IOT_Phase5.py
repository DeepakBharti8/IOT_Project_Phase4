import random
import time

class Sensor:
    def __init__(self, sensor_type, location):
        self.sensor_type = sensor_type
        self.location = location

    def collect_data(self):
        # Simulate data collection for water level sensors
        if self.sensor_type == 'water_level':
            data = random.uniform(0, 10)
        # Simulate data collection for rainfall sensors
        elif self.sensor_type == 'rainfall':
            data = random.uniform(0, 20)
        else:
            data = None
        return {
            'sensor_type': self.sensor_type,
            'location': self.location,
            'timestamp': time.time(),
            'data': data
        }

# Simulate IoT sensor deployment
water_level_sensor = Sensor('water_level', 'River Station A')
rainfall_sensor = Sensor('rainfall', 'Area X')

while True:
    water_level_data = water_level_sensor.collect_data()
    rainfall_data = rainfall_sensor.collect_data()

    print(f"Collected data from {water_level_sensor.location} ({water_level_sensor.sensor_type}): {water_level_data}")
    print(f"Collected data from {rainfall_sensor.location} ({rainfall_sensor.sensor_type}): {rainfall_data}")

    time.sleep(60)  # Simulate data collection every 60 seconds

