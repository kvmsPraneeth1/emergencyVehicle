import traci


def handle_traffic_lights(vehicle_edge, vehicle_id):
    # Define traffic lights and their monitored edges
    if vehicle_edge == "708208470#6":
        # Traffic light 3164250083
        print(f"emergency Vehicle detected. Changing signal 3164250083.")
        traci.trafficlight.setPhase("3164250083", 0)

    if vehicle_edge == "310919332#9" or vehicle_edge == "1288243226":
        # Traffic light 11947052812
        print(f"emergency Vehicle detected. Changing signal 11947052812.")
        traci.trafficlight.setPhase("11947052812", 0)

    if vehicle_edge in ["1288243228", "1288248182", "1225372232"]:
        # Traffic light 11947052813
        print(f"emergency Vehicle detected. Changing signal 11947052813.")
        traci.trafficlight.setPhase("11947052813", 0)

    if vehicle_edge == "419196405#0":
        # Traffic light 11947015186
        print(f"emergency Vehicle detected. Changing signal 11947015186.")
        traci.trafficlight.setPhase("11947015186", 2)

    if vehicle_edge == "310919331#2":
        # Traffic light 6527979187
        print(f"emergency Vehicle detected. Changing signal 6527979187.")
        traci.trafficlight.setPhase("6527979187", 0)

    if vehicle_edge == "-51761231#0":
        # Traffic light 4193188229
        print(f"emergency Vehicle detected. Changing signal 4193188229.")
        traci.trafficlight.setPhase("4193188229", 0)

    if vehicle_edge in ["213135164#2", "213135164#1", "213135694", "-213135164#3"]:
        # Traffic light 2228839540,  
        print(f"emergency Vehicle detected. Changing signal 2228839540.")
        traci.trafficlight.setPhase("2228839540", 0)
        
    if vehicle_edge in ["-213135181#2", "-213135181#3", "-213135181#4", "213135181#1"]:
        # Traffic light 2228839540,  
        print(f"emergency Vehicle detected. Changing signal 2228839540.")
        traci.trafficlight.setPhase("2228839540", 2)

    if vehicle_edge in ["1203856052#5", "1203856052#4"]:
        # Traffic light 3174179251,  
        print(f"emergency Vehicle detected. Changing signal 3174179251.")
        traci.trafficlight.setPhase("3174179251", 0)

    if vehicle_edge == "213495533#2":
        # Traffic light 3174179251,  
        print(f"emergency Vehicle detected. Changing signal 3174179251.")
        traci.trafficlight.setPhase("3174179251", 2)

    if vehicle_edge == "702376527#0":
        # Traffic light 3164238276
        print(f"emergency Vehicle detected. Changing signal 3164238276.")
        traci.trafficlight.setPhase("3164238276", 0)

    if vehicle_edge == "704242322#1":
        # Traffic light 2968385219
        print(f"emergency Vehicle detected. Changing signal 2968385219.")
        traci.trafficlight.setPhase("2968385219", 0)

    if vehicle_edge in ["843452864#16", "843452864#15", "843452864#14", "843452864#13"]:
        # Traffic light 3164069023
        print(f"emergency Vehicle detected. Changing signal 3164069023.")
        traci.trafficlight.setPhase("3164069023", 0)

    if vehicle_edge == "310919302#9":
        # Traffic light 289419432
        print(f"emergency Vehicle detected. Changing signal 289419432.")
        traci.trafficlight.setPhase("289419432", 0)

    if vehicle_edge == "310922592#9":
        # Traffic light 7867739883
        print(f"emergency Vehicle detected. Changing signal 7867739883.")
        traci.trafficlight.setPhase("7867739883", 0)

    if vehicle_edge == "759785842#10":
        # Traffic light 11521130727
        print(f"emergency Vehicle detected. Changing signal 11521130727.")
        traci.trafficlight.setPhase("11521130727", 0)

    if vehicle_edge in ["313513166#5", "313513166#4"]:
        # Traffic light 5433296930
        print(f"emergency Vehicle detected. Changing signal 5433296930.")
        traci.trafficlight.setPhase("5433296930", 0)

    if vehicle_edge in ["563587939#2", "563587939#1", "563587939#0"]:
        # Traffic light 6690124740
        print(f"emergency Vehicle detected. Changing signal 6690124740.")
        traci.trafficlight.setPhase("6690124740", 0)

    if vehicle_edge in ["1160123731#1", "1160123731#0"]:
        # Traffic light 7643275161 fake
        # print(f"avilable options for 4193188221 are \n{traci.trafficlight.getAllProgramLogics("4193188221")}")
        print(f"emergency Vehicle detected. Changing signal 4193188221.")
        traci.trafficlight.setPhase("4193188221", 0)

    if vehicle_edge in ["694965020", "1160123731#1", "1160123731#0","-1288248181"]:
        # Traffic light 3935642707
        print(f"emergency Vehicle detected. Changing signal 3935642707.")
        traci.trafficlight.setPhase("3935642707", 0)
    if vehicle_edge == "310919322#2":
        # Traffic light 3935642707
        print(f"emergency Vehicle detected. Changing signal 3935642707.")
        traci.trafficlight.setPhase("3935642707", 2)