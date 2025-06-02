import time
from gpiozero import MCP3008, Device
from gpiozero.pins.pigpio import PiGPIOFactory

Device.pin_factory = PiGPIOFactory()

moisture_sensor = MCP3008(channel=0)

while True:
    raw_value = moisture_sensor.value
    timestamp = time.strftime("%H:%M:%S")

    print(f"[{timestamp}] {raw_value:3f}")

    time.sleep(1)
