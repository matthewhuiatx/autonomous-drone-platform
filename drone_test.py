import collections
import collections.abc

collections.MutableMapping = collections.abc.MutableMapping

from dronekit import connect, VehicleMode
import time

vehicle = connect('udp:127.0.0.1:14550', wait_ready=True)

print("Connected")

vehicle.mode = VehicleMode("GUIDED")
while vehicle.mode.name != "GUIDED":
    time.sleep(1)

vehicle.armed = True
while not vehicle.armed:
    time.sleep(1)

print("Taking off")
vehicle.simple_takeoff(10)

time.sleep(10)

print("Landing")
vehicle.mode = VehicleMode("LAND")

time.sleep(5)

vehicle.close()
