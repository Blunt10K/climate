import Adafruit_BMP.BMP085 as BMP085

bmp280 = BMP085.BMP085()

print(f'Temperature: {bmp280.read_temperature()} C')
print(f'Temperature: {bmp280.read_pressure()} Pa')
print(f'Temperature: {bmp280.read_altitude()} metres')
print(f'Sealevel Pressure: {bmp280.read_sealevel_pressure()}')