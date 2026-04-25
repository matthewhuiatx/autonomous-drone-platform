from drone_controller import (
    connect_drone,
    get_home_location,
    takeoff,
    goto,
    return_home,
    land,
    status,
    close,
)

import time


def print_commands():
    print("\nCommands:")
    print("  takeoff <altitude in m>")
    print("  goto <lat> <lon> <altitude in m>")
    print("  home")
    print("  home <altitude>")
    print("  land")
    print("  status")
    print("  exit")


def main():
    vehicle = connect_drone()
    home_location = get_home_location(vehicle)

    print_commands()

    while True:
        command = input("> ").strip().split()

        if not command:
            continue

        action = command[0].lower()

        try:
            if action == "takeoff":
                altitude = float(command[1])
                takeoff(vehicle, altitude)
                time.sleep(2)
                print_commands()

            elif action == "goto":
                lat = float(command[1])
                lon = float(command[2])
                altitude = float(command[3])
                goto(vehicle, lat, lon, altitude)
                time.sleep(2)
                print_commands()

            elif action == "home":
                altitude = 10

                if len(command) > 1:
                    altitude = float(command[1])

                return_home(vehicle, home_location, altitude)
                time.sleep(2)
                print_commands()

            elif action == "land":
                land(vehicle)
                time.sleep(2)
                print_commands()

            elif action == "status":
                status(vehicle)
                time.sleep(2)
                print_commands()

            elif action == "exit":
                close(vehicle)
                break

            else:
                print("Unknown command")

        except IndexError:
            print("Missing argument")

        except ValueError:
            print("Invalid number")

        except KeyboardInterrupt:
            close(vehicle)
            break


if __name__ == "__main__":
    main()
