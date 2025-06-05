import traci


def handle_traffic_lights(vehicle_edge, vehicle_id):
    # Define traffic lights and their monitored edges
    if vehicle_edge in ["-E35", "E30"]:
        # Traffic light J22
        print(f"emergency Vehicle detected. Changing signal J22.")
        traci.trafficlight.setPhase("J22", 2)

    if vehicle_edge in ["E34","E32"]:
        # Traffic light J22
        print(f"emergency Vehicle detected. Changing signal J22.")
        traci.trafficlight.setPhase("J22", 0)

    if vehicle_edge in ["E16", "-E19",]:
        # Traffic light J11
        print(f"emergency Vehicle detected. Changing signal J11.")
        traci.trafficlight.setPhase("J11", 0)

    if vehicle_edge in ["-E18","-E20","E21","-E24"]:
        # Traffic light j12
        print(f"emergency Vehicle detected. Changing signal J12.")
        traci.trafficlight.setPhase("J12", 0)

    if vehicle_edge in ["E7","-E16"]:
        # Traffic light j6
        print(f"emergency Vehicle detected. Changing signal J6.")
        traci.trafficlight.setPhase("J6", 0)
    
    if vehicle_edge in ["E8","E9"]:
        # Traffic light j6
        print(f"emergency Vehicle detected. Changing signal J6.")
        traci.trafficlight.setPhase("J6", 2)

    if vehicle_edge in ["E25","E18"]:
        # Traffic light J5
        print(f"emergency Vehicle detected. Changing signal J5.")
        traci.trafficlight.setPhase("J5", 0)

    if vehicle_edge == "-E8":
        # Traffic light J5
        print(f"emergency Vehicle detected. Changing signal J5.")
        traci.trafficlight.setPhase("J5", 2)
        
    if vehicle_edge in ["E11", "E14", "E13", "E12"]:
        # Traffic light J4,  
        print(f"emergency Vehicle detected. Changing signal J4.")
        traci.trafficlight.setPhase("J4", 2)

    if vehicle_edge in ["E2", "-E25"]:
        # Traffic light J4,  
        print(f"emergency Vehicle detected. Changing signal J4.")
        traci.trafficlight.setPhase("J4", 0)

    if vehicle_edge in ["-E13","-E14","E12","-E11"]:
        # Traffic light J1
        print(f"emergency Vehicle detected. Changing signal J1.")
        traci.trafficlight.setPhase("J1", 2)

    if vehicle_edge in ["-E0","-E7"]:
        # Traffic light J1
        print(f"emergency Vehicle detected. Changing signal J1.")
        traci.trafficlight.setPhase("J1", 0)


    if vehicle_edge == "E24":
        # Traffic light J18
        print(f"emergency Vehicle detected. Changing signal J18.")  
        traci.trafficlight.setPhase("J18", 4)


    if vehicle_edge == "-E31":
        # Traffic light J18
        print(f"emergency Vehicle detected. Changing signal J18.")  
        traci.trafficlight.setPhase("J18", 2)

    # if vehicle_edge == "E35":
    #     # Traffic light J25
    #     print(f"emergency Vehicle detected. Changing signal J25.")  
    #     traci.trafficlight.setPhase("J25", 2)
    

    # if vehicle_edge in ["E40","-E41"]:
    #     # Traffic light J25
    #     print(f"emergency Vehicle detected. Changing signal J25.")  
    #     traci.trafficlight.setPhase("J25", 0)

    # if vehicle_edge in ["E41","E47"]:
    #     # Traffic light J28
    #     print(f"emergency Vehicle detected. Changing signal J28.")  
    #     traci.trafficlight.setPhase("J28", 0)

    # if vehicle_edge == "E38":
    #     # Traffic light J28
    #     print(f"emergency Vehicle detected. Changing signal J28.")  
    #     traci.trafficlight.setPhase("J28", 2)
    

    # if vehicle_edge in ["-E47","-E48"]:
    #     # Traffic light J30
    #     print(f"emergency Vehicle detected. Changing signal J30.")  
    #     traci.trafficlight.setPhase("J30", 2)

    # if vehicle_edge == "-E42":
    #     # Traffic light J30
    #     print(f"emergency Vehicle detected. Changing signal J30.")  
    #     traci.trafficlight.setPhase("J30", 0)

    # if vehicle_edge == "E39":
    #     # Traffic light J29
    #     print(f"emergency Vehicle detected. Changing signal J29.")  
    #     traci.trafficlight.setPhase("J29", 0)
    
    if vehicle_edge in ["-E40","E48"]:
        # Traffic light J30
        print(f"emergency Vehicle detected. Changing signal J29.")  
        traci.trafficlight.setPhase("J29", 0)
