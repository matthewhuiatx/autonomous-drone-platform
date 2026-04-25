Copy/paste this as your new `README.md`:

````md
# Autonomous Drone Platform

A Python-based command-line system for controlling an autonomous drone using ArduPilot SITL, DroneKit, and MAVLink.

This project simulates a full drone control pipeline, allowing programmatic control of a virtual quadcopter in real time. The current version supports interactive mission commands for takeoff, waypoint navigation, return-to-home behavior, landing, and vehicle status monitoring.

---

## Features

- Connects to ArduCopter SITL via MAVLink
- Saves the initial drone position as “home”
- Supports autonomous takeoff to a user-defined altitude
- Supports GPS waypoint navigation
- Supports autonomous mission execution
- Returns to saved home location and holds position
- Lands at the current location with completion detection
- Displays real-time vehicle status

---

## Architecture

```text
CLI Command
   ↓
Python Controller
   ↓
DroneKit
   ↓
MAVLink
   ↓
ArduPilot / ArduCopter SITL
   ↓
Simulated Drone
````

---

## Commands

| Command                                                      | Description                                                               |
| ------------------------------------------------------------ | ------------------------------------------------------------------------- |
| `takeoff <altitude>`                                         | Takes off to a specified altitude                                         |
| `goto <lat> <lon> <altitude>`                                | Flies to a GPS waypoint                                                   |
| `mission <takeoff_altitude> <lat> <lon> <waypoint_altitude>` | Takes off, flies to a waypoint, and holds position                        |
| `home`                                                       | Returns to saved home location at default altitude and holds position     |
| `home <altitude>`                                            | Returns to saved home location at a specified altitude and holds position |
| `land`                                                       | Lands at the current location                                             |
| `status`                                                     | Displays current flight state                                             |
| `exit`                                                       | Closes the drone connection                                               |

---

## Demo Flow

```bash
mission 10 -35.3635 149.1650 10
home
land
```

This commands the simulated drone to take off to 10 meters, fly to the GPS waypoint, hold position, return home when commanded, and land when commanded.

---

## Tech Stack

* Python
* DroneKit
* MAVLink
* ArduPilot / ArduCopter SITL
* WSL / Ubuntu

---

## How to Run

Start ArduCopter SITL:

```bash
cd ~/ardupilot/ArduCopter
../Tools/autotest/sim_vehicle.py -v ArduCopter --console --map --out=127.0.0.1:14550
```

Run the CLI:

```bash
cd ~/drone-platform
python3 drone_cli.py
```

Example command:

```bash
mission 10 -35.3635 149.1650 10
```

---

## Why This Project

This project explores how software systems interface with autonomous hardware through real-time communication protocols like MAVLink. It focuses on building a reusable control layer that can later be extended into a full UI-driven drone platform with waypoint planning, mission execution, computer vision, and obstacle avoidance.

---

## Roadmap

* [x] ArduPilot SITL setup
* [x] Python drone controller
* [x] Interactive CLI
* [x] Takeoff, waypoint, home, land, and status commands
* [x] Autonomous mission command
* [ ] Mission logging
* [ ] Multi-waypoint mission planning
* [ ] Web dashboard
* [ ] Computer vision waypoint detection
* [ ] Obstacle avoidance
* [ ] Real drone integration

```
```
