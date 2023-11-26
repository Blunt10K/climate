import Adafruit_BMP.BMP085 as BMP085

sensor = BMP085.BMP085()

print(f'Temperature: {sensor.read_temperature()} C')
print(f'Pressure: {sensor.read_pressure()} Pa')
print(f'Altitude: {sensor.read_altitude()} metres')
print(f'Sealevel Pressure: {sensor.read_sealevel_pressure()}')