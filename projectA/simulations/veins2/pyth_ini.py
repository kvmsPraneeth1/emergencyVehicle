import os
import subprocess
import traci
import time


def run_omnetpp_ini():
    try:
        # Connect to SUMO on port 9999
        traci_connection = traci.connect(port=9999)
        time.sleep(1)
        print("Connected to SUMO on port 9999.")

        # Main simulation loop
        while traci_connection.simulation.getMinExpectedNumber() > 0:
            print("1")
            vehicles_in_simulation = traci_connection.vehicle.getIDList()

            # Check if "vehicle0" is present; if not, add it back
            if "vehicle0" not in vehicles_in_simulation:
                print("2")
                print("Vehicle0 is not present in the simulation. Adding it back.")
                # Add the vehicle on a specified edge (e.g., "-4006740")
                traci_connection.route.add("route0", ["-4006740"])
                traci_connection.vehicle.add("vehicle0", "route0", typeID="car")

                traci_connection.vehicle.setColor("vehicle0", (255, 0, 0))  # Set color to red

            # Step the simulation forward
            print("3")
            traci_connection.simulationStep()
            time.sleep(0.1)  # Delay to prevent high CPU usage

        print("Simulation completed.")

    except traci.TraCIException as e:
        print("TraCI connection error: %s" % e)

    finally:
        # Close the connection to SUMO
        traci_connection.close()
        print("Disconnected from SUMO.")

# Run the function
run_omnetpp_ini()
