# Autonomous Drone Platform

A Python-based command-line system for controlling an autonomous drone using ArduPilot SITL, DroneKit, and MAVLink.

This project simulates a full drone control pipeline, allowing programmatic control of a virtual quadcopter in real time.

---

## Features

* Connects to ArduCopter SITL via MAVLink
* Saves initial position as “home”
* Autonomous takeoff to user-defined altitude
* GPS waypoint navigation
* Return-to-home functionality
* Autonomous landing with completion detection
* Real-time vehicle status monitoring

---

## Demo Flow

```
takeoff 10
goto <lat> <lon> 10
home
land
```

---

## Tech Stack

* Python
* DroneKit
* MAVLink
* ArduPilot (ArduCopter SITL)
* WSL (Ubuntu)

---

## How to Run

Start SITL:

```bash
cd ~/ardupilot/ArduCopter
../Tools/autotest/sim_vehicle.py -v ArduCopter --console --map --out=127.0.0.1:14550
```

Run CLI:

```bash
cd ~/drone-platform
python3 drone_cli.py
```

## Why This Project

This project explores how software systems interface with autonomous hardware through real-time communication protocols (MAVLink). It focuses on building a control layer that can later be extended into a full UI-driven drone platform with waypoint planning and obstacle avoidance.

## Next Steps

* Mission sequencing (multi-waypoint automation)
* Web-based UI (React + backend API)
* Computer vision for obstacle detection
* Real drone integration
