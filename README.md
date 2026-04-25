# Autonomous Drone Platform

**A Python-based command-line system for controlling an autonomous drone using ArduPilot SITL, DroneKit, and MAVLink.**

This project simulates a full drone control pipeline, allowing **programmatic control of a virtual quadcopter in real time**.

The current version supports:

- Interactive mission execution
- GPS waypoint navigation
- Return-to-home behavior
- Autonomous landing
- Real-time vehicle status monitoring

---

## Features

- **ArduCopter SITL integration** via MAVLink
- **Home position tracking** saved at startup
- **Autonomous takeoff** to user-defined altitude
- **GPS waypoint navigation**
- **Mission command execution**
- **Return-to-home hover behavior**
- **Autonomous landing with completion detection**
- **Real-time vehicle telemetry and status output**

---

## Architecture

```text
User CLI Input
      ↓
Python Controller
      ↓
DroneKit API
      ↓
MAVLink Protocol
      ↓
ArduPilot / ArduCopter SITL
      ↓
Simulated Drone
````

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

## Demo Flow

```bash
mission 10 -35.3635 149.1650 10
home
land
```

This commands the simulated drone to:

1. take off to 10 meters
2. fly to the GPS waypoint
3. hold position at the waypoint
4. return home when commanded
5. land when commanded

## Tech Stack

* Python
* DroneKit
* MAVLink
* ArduPilot / ArduCopter SITL
* WSL / Ubuntu

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

Example:

```bash
mission 10 -35.3635 149.1650 10
```

## Why This Project

This project explores how software systems interface with autonomous hardware through real-time communication protocols like **MAVLink**.

It focuses on building a reusable control layer that can be extended into:

* UI-driven mission control
* Multi-waypoint planning
* Autonomous navigation systems
* Real-world drone integration

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
