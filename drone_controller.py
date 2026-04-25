import collections
import collections.abc
import math
import time

collections.MutableMapping = collections.abc.MutableMapping

from dronekit import connect, VehicleMode, LocationGlobalRelative


def connect_drone(connection_string="udp:127.0.0.1:14550"):
    vehicle = connect(connection_string, wait_ready=True)
    print("Connected")

    vehicle.parameters["ARMING_SKIPCHK"] = -1
    print("Arming checks skipped for SITL")

    print("Waiting for position estimate...")
    while vehicle.location.global_relative_frame.lat is None:
        time.sleep(1)

    time.sleep(10)
    print("Position estimate should be ready")

    return vehicle


def get_home_location(vehicle):
    location = vehicle.location.global_relative_frame
    home_location = LocationGlobalRelative(location.lat, location.lon, location.alt)
    print(f"Home saved: ({home_location.lat}, {home_location.lon}, {home_location.alt:.2f}m)")
    return home_location


def set_mode(vehicle, mode_name):
    vehicle.mode = VehicleMode(mode_name)

    while vehicle.mode.name != mode_name:
        print(f"Waiting for mode {mode_name}...")
        time.sleep(1)

    print(f"Mode set to {mode_name}")


def arm(vehicle, timeout=20):
    vehicle.armed = True
    start = time.time()

    while not vehicle.armed:
        print("Waiting for arming...")

        if time.time() - start > timeout:
            raise TimeoutError("Failed to arm. Check MAVProxy console for pre-arm errors.")

        time.sleep(1)

    print("Armed")


def takeoff(vehicle, altitude):
    set_mode(vehicle, "GUIDED")
    arm(vehicle)

    print(f"Taking off to {altitude} meters")
    vehicle.simple_takeoff(altitude)

    while True:
        current_altitude = vehicle.location.global_relative_frame.alt
        print(f"Altitude: {current_altitude:.2f}m")

        if current_altitude >= altitude * 0.95:
            print(f"Reached target altitude ({altitude}m)")
            break

        time.sleep(1)


def get_distance_meters(current, target):
    dlat = target.lat - current.lat
    dlon = target.lon - current.lon
    return math.sqrt((dlat * 111139) ** 2 + (dlon * 111139) ** 2)


def goto(vehicle, lat, lon, altitude):
    target = LocationGlobalRelative(lat, lon, altitude)
    print(f"Flying to waypoint: lat={lat}, lon={lon}, alt={altitude}")

    set_mode(vehicle, "GUIDED")
    vehicle.simple_goto(target)

    while True:
        current = vehicle.location.global_relative_frame
        distance = get_distance_meters(current, target)

        print(f"Distance to waypoint: {distance:.2f}m")

        if distance <= 1.5:
            print(f"Arrived at waypoint: ({lat}, {lon}, {altitude})")
            break

        time.sleep(1)


def return_home(vehicle, home_location, altitude=10):
    print(f"Returning home: lat={home_location.lat}, lon={home_location.lon}, alt={altitude}")
    goto(vehicle, home_location.lat, home_location.lon, altitude)
    print("Arrived home")


def land(vehicle):
    print("Landing")
    set_mode(vehicle, "LAND")

    while True:
        altitude = vehicle.location.global_relative_frame.alt
        print(f"Altitude: {altitude:.2f}m")

        if altitude <= 0.5 and not vehicle.armed:
            print("Landed successfully")
            break

        if not vehicle.armed:
            print("Landed successfully")
            break

        time.sleep(1)


def status(vehicle):
    location = vehicle.location.global_relative_frame

    print(f"Mode: {vehicle.mode.name}")
    print(f"Armed: {vehicle.armed}")
    print(f"Altitude: {location.alt:.2f}m")
    print(f"Lat: {location.lat}")
    print(f"Lon: {location.lon}")


def close(vehicle):
    vehicle.close()
    print("Connection closed")
