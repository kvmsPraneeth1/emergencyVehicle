import os
import sumolib
import sys
from collections import defaultdict, deque
import heapq
import math
import traci
import threading
import traffic_controller_bidar as tc



# Path to SUMO tools and your net.xml file
# sumo_tools_path = r'C:\newSumo\sumoNew'
net_file = r'C:\newSumo\project\projectA\simulations\sumoSimulation1\bidar.net.xml'  # Replace with the path to your net.xml file
sumo_cfg_file = r'C:\newSumo\project\projectA\simulations\sumoSimulation1\bidar.sumocfg'  # Replace with your SUMO config file
output_graph_file = 'graph.txt'  # Output graph file
flag = True
# Add SUMO tools to system path
if 'SUMO_HOME' in os.environ:
    sys.path.append(os.path.join(os.environ['SUMO_HOME'], 'tools'))

# Load the SUMO network
net = sumolib.net.readNet(net_file)

# Dictionary to store node connections, edge IDs, and distances (directed)
node_connections = defaultdict(list)

# Set to store all nodes
all_nodes = set()


def graph_gen():
# Loop through all edges in the network
    for edge in net.getEdges():
        from_node = edge.getFromNode().getID()
        to_node = edge.getToNode().getID()

    # Get the edge ID and length (distance) of the edge
        edge_id = edge.getID()
        distance = edge.getLength()

    # Store the connection in the dictionary (directed)
        node_connections[from_node].append((to_node, edge_id, distance))

    # Add nodes to the set of all nodes
        all_nodes.add(from_node)
        all_nodes.add(to_node)


def graph_gen_sim():
# Loop through all edges in the network
    for edge in net.getEdges():
        from_node = edge.getFromNode().getID()
        to_node = edge.getToNode().getID()

    # Get the edge ID and length (distance) of the edge
        edge_id = edge.getID()
        num_vehicles = traci.edge.getLastStepVehicleNumber(edge_id)
        density = (num_vehicles + 1) / edge.getLength()
        avgspeed = traci.edge.getLastStepMeanSpeed(edge_id) 
        density = density * avgspeed * 2500 + edge.getLength()
        #density = edge.getLength +((num_vehicles + 1)/edge.getLength()) / traci.edge.getLastStepMeanSpeed(edge)  

        
    # Store the connection in the dictionary (directed)
        node_connections[from_node].append((to_node, edge_id, density))

    # Add nodes to the set of all nodes
        all_nodes.add(from_node)
        all_nodes.add(to_node)

# Heuristic function: straight-line distance as the crow flies
def heuristic(node1, node2):
    node1_coords = net.getNode(node1).getCoord()
    node2_coords = net.getNode(node2).getCoord()
    return math.sqrt((node1_coords[0] - node2_coords[0]) ** 2 + (node2_coords[1] - node1_coords[1]) ** 2)

# A* algorithm to find the shortest path
def a_star(start_node, end_node, result_dict):
    # graph_gen_sim()
    # Priority queue to store (estimated total cost, current path cost, current node, previous node, edge ID)
    priority_queue = [(0, 0, start_node, None, None)]
    # Dictionary to store the shortest known path cost to each node
    shortest_costs = {node: float('inf') for node in all_nodes}
    shortest_costs[start_node] = 0
    # Dictionary to store the path backtracking
    previous_nodes = {node: (None, None) for node in all_nodes}  # Stores (previous node, edge ID)

    while priority_queue:
        est_total_cost, current_cost, current_node, prev_node, edge_id = heapq.heappop(priority_queue)

        # If we reached the goal node, stop
        if current_node == end_node:
            break

        # Check each neighbor of the current node
        for neighbor, neighbor_edge_id, distance in node_connections[current_node]:
            path_cost = current_cost + distance
            est_cost = path_cost + heuristic(neighbor, end_node)

            if path_cost < shortest_costs[neighbor]:
                shortest_costs[neighbor] = path_cost
                previous_nodes[neighbor] = (current_node, neighbor_edge_id)
                heapq.heappush(priority_queue, (est_cost, path_cost, neighbor, current_node, neighbor_edge_id))

    # Reconstruct the shortest path (backtracking)
    path_nodes = deque()
    path_edges = deque()
    current_node = end_node

    while previous_nodes[current_node][0] is not None:
        prev_node, edge_id = previous_nodes[current_node]
        path_nodes.appendleft(current_node)
        path_edges.appendleft(edge_id)
        current_node = prev_node

    # Add the start node to the path
    path_nodes.appendleft(start_node)

    # Save the result in the result_dict
    result_dict['path_nodes'] = path_nodes
    result_dict['path_edges'] = path_edges
    result_dict['cost'] = shortest_costs[end_node]

# Function to save the graph to a file
def save_graph_to_file(graph_file):
    with open(graph_file, 'w') as f:
        for node, connections in node_connections.items():
            connections_str = ', '.join([f"{neighbor} - {edge_id}" for neighbor, edge_id, _ in connections])
            f.write(f"{node} : {connections_str}\n")

# Traffic light handling function


# Function to control the traffic lights in a separate thread
def traffic_light_controller(start_node, end_node):
   cost=[]
   while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()

        vehicles_in_simulation = traci.vehicle.getIDList()


        if "vehicle0" not in vehicles_in_simulation:
            print("Vehicle0 is not present in the simulation. Adding it back.")
            # Add the route with calculated edges
            traci.vehicle.add("vehicle0", "route0", typeID="car")  # Add the vehicle again
            traci.vehicle.setColor("vehicle0", (255, 0, 0))  # Set color to red again
        # Check the current vehicle's position and handle traffic lights
        current_edge = traci.vehicle.getRoadID("vehicle0") 

        current_edge = traci.vehicle.getRoadID("vehicle0")
        next_junction = traci.edge.getToJunction(current_edge)
        # print(f"vehilce is at {current_edge}")
        # Check if we passed a junction and recalculate path
        if next_junction != start_node and flag:  # New junction detected
            start_node = next_junction  # Update start node to current junction
            print(f"Recalculating shortest path from {start_node} to {end_node}...")

            # Recalculate A* from new junction nano
            graph_gen_sim()
            # print(node_connections)

            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<< new graph generated >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            result_dict = {}
            a_star_thread = threading.Thread(target=a_star, args=(start_node, end_node, result_dict))
            a_star_thread.start()

            # Wait for A* algorithm to finish
            a_star_thread.join()

            path_edges = result_dict['path_edges']
            path_nodes = result_dict['path_nodes']
            path_edges = result_dict['path_edges']
            total_density = result_dict['cost']
            cost.append(total_density)
            # print(f"new shortest path from {start_node} to {end_node} is:")
            # print(" -> ".join(path_nodes))
            # print("Edges taken: ", list(path_edges))
            # print(f"The total distance is: {total_density}")
            # print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<cost>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(total_density)
            # print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<</cost>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            # Update vehicle's route with new path
            
            
            path_edges.appendleft(current_edge)
            traci.vehicle.setRoute("vehicle0", path_edges)
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<new path assigned >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            # num_vehicles = traci.edge.getLastStepVehicleNumber(current_edge)
            # print("--------------------------------------------------------------------------")
            # print(f"number of vehilces in edge : {current_edge} are {num_vehicles}")
            # print("--------------------------------------------------------------------------")
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")



        #  Get the current edge the vehicle is on
        tc.handle_traffic_lights(current_edge, "vehicle0")  # Handle traffic light logic

         
   

def start_simulation(path_edges):
    traci.init(port=9999)
    
    traci.setOrder(2)
    # Add the vehicle and route
    traci.route.add("route0", path_edges)  # Add the route with calculated edges
    traci.vehicle.add("vehicle0", "route0", typeID="car")  # Add a vehicle to the simulation
    traci.vehicle.setColor("vehicle0", (255, 0, 0))  # Set its color to red
    
    # Start traffic light controller in a separate thread
    traffic_light_thread = threading.Thread(target=traffic_light_controller, args=(start_node,end_node))
    traffic_light_thread.start()

    # Wait for traffic light thread to finish
    traffic_light_thread.join()
    
    traci.close()

# Main function
if __name__ == "__main__":
    # Input the start and end nodes
    print("-------------------------------------------------------------------------------------------------------------------------------------------------\n")
    # print(traci.getVersion())

    print("\n\n-------------------------------------------------------------------------------------------------------------------------------------------------\n")
    graph_gen()
    start_node = '1117251964'
    end_node = '7791433364'

    # Ensure both nodes exist in the network
    if start_node not in all_nodes or end_node not in all_nodes:
        print("One or both of the specified nodes do not exist in the network.")
    else:
        # Result dictionary to store A* results
        result_dict = {}
        a_star_thread = threading.Thread(target=a_star, args=(start_node, end_node, result_dict))
        a_star_thread.start()

            # Wait for A* algorithm to finish
        a_star_thread.join()
        # Start A* algorithm in a separate thread
        

        # Output the result
        if 'path_nodes' in result_dict:
            path_nodes = result_dict['path_nodes']
            path_edges = result_dict['path_edges']
            total_distance = result_dict['cost']
            
            print(f"The shortest path from {start_node} to {end_node} is:")
            print(" -> ".join(path_nodes))
            print("Edges taken: ", list(path_edges))
            print(f"The total distance is: {total_distance}")
        else:
            print(f"No path found between {start_node} and {end_node}.")

        # Save the graph to a text file
        save_graph_to_file(output_graph_file)
        print(f"Graph saved to {output_graph_file}")

        # Start the SUMO simulation with the generated path
        start_simulation(result_dict['path_edges'])
