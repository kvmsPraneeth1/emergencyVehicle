import os
import traci
# import libsumo as traci

import time

def run_omnetpp_ini():
    try:
        # Connect to SUMO on port 9999
        traci.init(port=9999)
        traci.setOrder(2)
        print("Connected to SUMO on port 9999.")
        time.sleep(100)
        print("ok")
        # Main simulation loop
        while True:
            try:
                if traci.simulation.getMinExpectedNumber() <= 0:
                    break

                vehicles_in_simulation = traci.vehicle.getIDList()

                # Check if "vehicle0" is present; if not, add it back
                if "vehicle0" not in vehicles_in_simulation:
                    print("Vehicle0 is not present in the simulation. Adding it back.")

                    # Ensure the route exists; if not, add it
                    if not traci.route.getIDList():
                        traci.route.add("route0", ["-4006740"])

                    # Add the vehicle and set color to red
                    traci.vehicle.add("vehicle0", "route0", typeID="car")
                    traci.vehicle.setColor("vehicle0", (255, 0, 0))

                # Step the simulation forward
                traci.simulationStep()
                time.sleep(0.1)  # Delay to prevent high CPU usage

            except traci.TraCIException as e:
                print("Error during simulation step: %s" % e)
                break

        print("Simulation completed.")

    except traci.TraCIException as e:
        print("TraCI connection error: %s" % e)

    finally:
        # Close the connection to SUMO
        try:
            traci.close()
            print("Disconnected from SUMO.")
        except Exception as e:
            print("Error closing connection: %s" % e)

# Run the function
run_omnetpp_ini()
