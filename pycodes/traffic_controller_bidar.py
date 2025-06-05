import traci


def handle_traffic_lights(vehicle_edge, vehicle_id):
    # Define traffic lights and their monitored edges
    if vehicle_edge == "-839279560#1":
        # Traffic light 7831669360
        print(f"emergency Vehicle detected. Changing signal 7831669360.")
        traci.trafficlight.setPhase("7831669360", 2)

    if vehicle_edge == "839279559#38":
        # Traffic light 7831669360
        print(f"emergency Vehicle detected. Changing signal 7831669360.")
        traci.trafficlight.setPhase("7831669360", 0)

    if vehicle_edge in ["96411253#20","-839255830#0","96411253#19","839255827#1"]:
        # Traffic light 7831669360
        print(f"emergency Vehicle detected. Changing signal 7831669360.")
        traci.trafficlight.setPhase("7831669360", 4)

    if vehicle_edge in ["347328435#3","-545168501#0","839279559#33","839279559#34","347328435#2","839279559#32"]:
        # Traffic light 7832237905
        print(f"emergency Vehicle detected. Changing signal 7832237905.")
        traci.trafficlight.setPhase("7832237905", 0)

    if vehicle_edge in ["839313446#17","-839246297","839313446#16"]:
        # Traffic light 7832237905
        print(f"emergency Vehicle detected. Changing signal 7832237905.")
        traci.trafficlight.setPhase("7832237905", 4)

    if vehicle_edge in ["-119025369#0","-119025369#2","-119025369#3"]:
        # Traffic light 7832237905
        print(f"emergency Vehicle detected. Changing signal 7832237905.")
        traci.trafficlight.setPhase("7832237905", 6)

    if vehicle_edge in ["96002287#17", "-96002286#0", "-96190528#0", "96002287#15"]:
        # Traffic light 1114887143,  
        print(f"emergency Vehicle detected. Changing signal 1114887143.")
        traci.trafficlight.setPhase("1114887143", 0)
    

    if vehicle_edge in ["96190546#3", "96190546#2", "96190476#5","839309240#9","839309240#8","-839309238#0"]:
        # Traffic light 1114887143,  
        print(f"emergency Vehicle detected. Changing signal 1114887143.")
        traci.trafficlight.setPhase("1114887143", 2)
        
    if vehicle_edge in ["839302980#18", "839302980#17", "-96411246#0"]:
        # Traffic light 1114887143,  
        print(f"emergency Vehicle detected. Changing signal 1114887143.")
        traci.trafficlight.setPhase("1114887143", 4)

    if vehicle_edge in ["347328435#17", "545168414","347328435#16","839279559#11","-457317798#0","839279559#10"]:
        # Traffic light 7831895579,  
        print(f"emergency Vehicle detected. Changing signal 3174179251.")
        traci.trafficlight.setPhase("7831895579", 0)



    if vehicle_edge in ["839302979#14", "-96190555#0","839302979#13"]:
        # Traffic light 7831895579,  
        print(f"emergency Vehicle detected. Changing signal 3174179251.")
        traci.trafficlight.setPhase("7831895579", 2)


    if vehicle_edge in ["-545163887#0", "545163888#0","-545163887#1"]:
        # Traffic light 7831895579,  
        print(f"emergency Vehicle detected. Changing signal 3174179251.")
        traci.trafficlight.setPhase("7831895579", 4)

    if vehicle_edge in ["460342075#2","460342075#1","460342075#0"]:
        # Traffic light 4560140714,  
        print(f"emergency Vehicle detected. Changing signal 4560140714.")
        traci.trafficlight.setPhase("4560140714", 0)

    if vehicle_edge in ["-60649869#1","347328435#31"]:
        # Traffic light 4560140714,  
        print(f"emergency Vehicle detected. Changing signal 4560140714.")
        traci.trafficlight.setPhase("4560140714", 2)

    if vehicle_edge in ["840857953#0","840857952","840857951#1"]:
        # Traffic light 4560140714,  
        print(f"emergency Vehicle detected. Changing signal 4560140714.")
        traci.trafficlight.setPhase("4560140714", 4)

    if vehicle_edge in ["-140742040#1","-545163872#0","-140742040#2"]:
        # Traffic light 4560140714,  
        print(f"emergency Vehicle detected. Changing signal 4560140714.")
        traci.trafficlight.setPhase("4560140714", 6)

    if vehicle_edge in ["-96143891#0","-96190471#0","-96143891#1","631572903#2","631572903#1","-840888436"]:
        # Traffic light 1114027972,  
        print(f"emergency Vehicle detected. Changing signal 1114027972.")
        traci.trafficlight.setPhase("1114027972", 0)

    if vehicle_edge == "631572902#3":
        # Traffic light 1114027972
        print(f"emergency Vehicle detected. Changing signal 1114027972.")
        traci.trafficlight.setPhase("1114027972", 2)

    if vehicle_edge in ["140745481#10", "459895210#0","140745481#9"]:
        # Traffic light 7843478183
        print(f"emergency Vehicle detected. Changing signal 7843478183.")
        traci.trafficlight.setPhase("7843478183", 0)

    if vehicle_edge in ["459895205#3", "459895205#2","726281918","726279565","726278485","726276949"]:
        # Traffic light 7843478183
        print(f"emergency Vehicle detected. Changing signal 7843478183.")
        traci.trafficlight.setPhase("7843478183", 2)

    if vehicle_edge in ["-840550584#0", "-96143890#0","-840550584#1"]:
        # Traffic light 7843478183
        print(f"emergency Vehicle detected. Changing signal 7843478183.")
        traci.trafficlight.setPhase("7843478183", 4)

    if vehicle_edge in ["-459895208#2", "-459895208#3","-840550577","459895209#1"]:
        # Traffic light 7843478183
        print(f"emergency Vehicle detected. Changing signal 7843478183.")
        traci.trafficlight.setPhase("7843478183", 6)


    if vehicle_edge == "838200493#1":
        # Traffic light 7819194578
        print(f"emergency Vehicle detected. Changing signal 7819194578.")
        traci.trafficlight.setPhase("7819194578", 0)

    if vehicle_edge in ["-837756432","-837756433#1","837756433#0"]:
        # Traffic light 7819194578
        print(f"emergency Vehicle detected. Changing signal 7819194578.")
        traci.trafficlight.setPhase("7819194578", 2)

    if vehicle_edge == "834652889#2":
        # Traffic light 7819194578
        print(f"emergency Vehicle detected. Changing signal 7819194578.")
        traci.trafficlight.setPhase("7819194578", 4)

    if vehicle_edge in ["-837756423#2","-837756433#0","-837756423#3"]:
        # Traffic light 7819194578
        print(f"emergency Vehicle detected. Changing signal 7819194578.")
        traci.trafficlight.setPhase("7819194578", 6)