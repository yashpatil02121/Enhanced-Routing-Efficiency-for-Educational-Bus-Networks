from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import folium
from folium import IFrame
from geopy.geocoders import Nominatim
import json
import requests
from geopy.geocoders import Nominatim

url = "https://trueway-matrix.p.rapidapi.com/CalculateDrivingMatrix"

# querystring = {
#     "origins": "19.4162831,72.8143737;19.431060, 72.812969;19.432426, 72.810556;19.432934, 72.809668;19.414671, 72.816632;19.415032, 72.819658;19.414243, 72.822265;19.411171, 72.817333;19.413962, 72.815923;19.408389, 72.821165;19.411784, 72.822637"
# }

# coordinates of Holy Family Convent High School vasai
# querystring = {
#     "origins":"19.1992, 72.8981; 19.2092, 72.9081; 19.2035, 72.9132; 19.1894, 72.8897; 19.2030, 72.8852;19.2046, 72.9015; 19.2138, 72.8997;19.1965, 72.8956; 19.1918, 72.8993"
# }

# St. Francis
# 19.3152473472142, 72.85621263504753   school
# 19.31668912879359,72.85057936947739; 19.313916512308772, 72.85107532882343; 19.310365012064075, 72.85044869728496; 19.310365012064075,72.85044869728496; 19.310935003919386,72.86533233913663; 19.30812085826061, 72.86473357733612; 19.30812085826061, 72.86473357733612; 19.30812085826061,72.86473357733612;
# querystring = {
#     "origins":"19.315206395257285, 72.8562294478749; 19.31619612124383, 72.85880905329796; 19.314513705575436, 72.85873419213874; 19.314115778427634, 72.86044691452545; 19.313439540892766, 72.85813303698804; 19.312345500213628, 72.85346053377677; 19.31125827589783, 72.85321764255828; 19.309287244954707, 72.85360626834338; 19.30843686988745, 72.85456973635036"
# }

querystring = {
    "origins":"19.315206395257285, 72.8562294478749; 19.31668912879359,72.85057936947739; 19.313916512308772, 72.85107532882343; 19.310365012064075, 72.85044869728496; 19.310365012064075,72.85044869728496; 19.310935003919386,72.86533233913663; 19.30812085826061, 72.86473357733612; 19.30812085826061, 72.86473357733612; 19.30812085826061,72.86473357733612"
}

# school:19.1992, 72.8981
# east: 19.2092, 72.9081; 19.2035, 72.9132; 19.2127, 72.9218; 19.2048, 72.9227; 19.2083, 72.9296
# west: 19.1894, 72.8897; 19.2030, 72.8852; 19.1957, 72.8935; 19.2071, 72.8999; 19.1983, 72.8908
# north: 19.2046, 72.9015; 19.2138, 72.8997; 19.2073, 72.8946; 19.2159, 72.8938; 19.2087, 72.9043
# south: 19.1965, 72.8956; 19.1918, 72.8993; 19.1857, 72.8962; 19.1943, 72.8918; 19.1889, 72.8999

# querystring = {
#     "origins": "19.4162831,72.8143737;19.750123,72.812345;19.820456,73.123456;19.915678,72.987654;19.635241,72.894561;19.785432,73.009876;19.862345,73.567890;19.440987,73.456789;19.573219,72.876543;19.4162831,72.8143737;19.422660, 72.824139;19.416364, 72.823168;19.424607, 72.832879;19.419341, 72.863468;19.405832, 72.849630;19.430674, 72.871964;19.414533, 72.876091;19.403318, 72.855512;19.455826, 72.884469;19.463192, 72.886379;19.415861, 72.799788;19.415861, 72.799788;19.394468, 72.787671;19.409159, 72.766629;19.413953, 72.784554;19.404082, 72.779935;19.426318, 72.791275;19.418069, 72.783696;19.428919, 72.782503;19.432798, 72.775085;19.431496, 72.816258;19.432927, 72.807397;19.444236, 72.806896;19.454888, 72.818490;19.447766, 72.801410; 19.458543, 72.808466;19.427334, 72.810930;19.431060, 72.812969;19.432426, 72.810556;19.432934, 72.809668;19.414671, 72.816632;19.415032, 72.819658;19.414243, 72.822265;19.411171, 72.817333;19.413962, 72.815923;19.408389, 72.821165;19.411784, 72.822637;19.387040, 72.826636;19.387154, 72.810508;19.381602, 72.829194"
# }

# querystring = {
#     "origins": "19.693558,72.765518;19.540270,73.997322;19.981066,72.745178;19.453600,73.328201;19.357500,73.628201;19.620099,72.953521" 
# }

# querystring = {
#     "origins": "19.693558,72.765518;19.540270,73.997322;19.981066,72.745178;19.453600,73.328201;19.357500,73.628201;19.620099,72.953521;19.750123,72.812345;19.820456,73.123456;19.915678,72.987654;19.635241,72.894561;19.785432,73.009876;19.862345,73.567890;19.440987,73.456789;19.573219,72.876543"
# }


headers = {
    # "X-RapidAPI-Key": "5f328554c7mshda46efbec2b57f3p160e02jsn46cc01730e26",
    "X-RapidAPI-Key": "17509c00d1mshfc009df18a5f92ap1654c1jsnb2757db15c94",
    # "X-RapidAPI-Key": "21702713f4msh2ab51f9b4508cc1p18ab8ajsn13712aaf70e1",

    "X-RapidAPI-Host": "trueway-matrix.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

json_data = response.json()

# Parse origins from the query string
origins = querystring["origins"].split(";")

# Create a dictionary to store the locations and their coordinates
locations = {}
for idx, origin in enumerate(origins):
    lat, lon = map(float, origin.split(","))
    locations[f"drop/pickup{idx+1} "] = {"latitude": lat, "longitude": lon}

# Print the locations dictionary
print("Locations:")
for route, coords in locations.items():
    print(f"{route}:{coords['latitude']},{coords['longitude']}")

# Store the distance matrix

    data = {}
data["distance_matrix"] = json_data["distances"]
print("\nDistance Matrix:")
print(data)

def create_data_model():
    """Stores the data for the problem."""
 
    data["demands"] = [0, 1, 1, 2, 4, 2, 4, 8, 8, 1, 2, 1, 2, 4, 4, 8, 8]
    data["vehicle_capacities"] = [15, 15, 15, 15]
    data["num_vehicles"] = 4
    data["depot"] = 0
    return data

def get_route_details(data, manager, routing, solution, locations):
    """Returns route details for each bus."""
    route_details = []
    for vehicle_id in range(data["num_vehicles"]):
        index = routing.Start(vehicle_id)
        route_nodes = []
        route_distance = 0
        route_load = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route_nodes.append((node_index, locations[f"drop/pickup{node_index+1} "]))
            route_load += data["demands"][node_index]
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(
                previous_index, index, vehicle_id
            )
        route_nodes.append((manager.IndexToNode(index), locations[f"drop/pickup{manager.IndexToNode(index)+1} "]))
        route_details.append((route_nodes, route_distance))
    return route_details


def main():
    """Solve the CVRP problem and store route details."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(
        len(data["distance_matrix"]), data["num_vehicles"], data["depot"]
    )

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data["distance_matrix"][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Capacity constraint.
    def demand_callback(from_index):
        """Returns the demand of the node."""
        # Convert from routing variable Index to demands NodeIndex.
        from_node = manager.IndexToNode(from_index)
        return data["demands"][from_node]

    demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,  # null capacity slack
        data["vehicle_capacities"],  # vehicle maximum capacities
        True,  # start cumul to zero
        "Capacity",
    )

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )
    search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
    )
    search_parameters.time_limit.FromSeconds(1)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Store route details for each bus
    route_details = None
    if solution:
        route_details = get_route_details(data, manager, routing, solution, locations)
    
    return route_details

def get_coordinates(location):
    geolocator = Nominatim(user_agent="map_route_app")
    location_info = geolocator.geocode(location)
    if location_info:
        return location_info.latitude, location_info.longitude
    else:
        return None

def plot_route_map(origin, destination, waypoints, bus_routes=None):
    # Get coordinates for origin, destination, and waypoints
    origin_coords = get_coordinates(origin)
    destination_coords = get_coordinates(destination)
    waypoints_coords = [get_coordinates(waypoint) for waypoint in waypoints]

    # Create a folium map centered at the mean of all coordinates
    mean_lat = sum(lat for lat, lon in filter(None, [origin_coords, destination_coords] + waypoints_coords)) / len(list(filter(None, [origin_coords, destination_coords] + waypoints_coords)))
    mean_lon = sum(lon for lat, lon in filter(None, [origin_coords, destination_coords] + waypoints_coords)) / len(list(filter(None, [origin_coords, destination_coords] + waypoints_coords)))

    route_map = folium.Map(location=[mean_lat, mean_lon], zoom_start=12)

    # Plot origin and destination
    if origin_coords:
        folium.Marker(location=origin_coords, popup='Origin', icon=folium.Icon(color='green')).add_to(route_map)
    if destination_coords:
        folium.Marker(location=destination_coords, popup='Destination', icon=folium.Icon(color='red')).add_to(route_map)

    # Plot waypoints
    for i, waypoint_coords in enumerate(waypoints_coords, start=1):
        if waypoint_coords:
            folium.Marker(location=waypoint_coords, popup=f'Waypoint {i}', icon=folium.Icon(color='blue')).add_to(route_map)

    # Plot bus routes
    if bus_routes:
        for bus, details in bus_routes.items():
            route_coords = [get_coordinates(node["coords"]) for node in details[0]]
            folium.PolyLine(locations=route_coords, color='orange', weight=2.5, opacity=1).add_to(route_map)

    # Save the map to an HTML file
    route_map.save('map_route.html')


def plot_bus_coordinates(api_key, bus_routes):
    # Initialize a Folium map
    route_map = folium.Map()

    # Define colors for different buses
    colors = ['red', 'blue', 'green', 'orange', 'purple', 'gray', 'black', 'pink', 'yellow']

    # Iterate over each bus route
    for i, (bus, details) in enumerate(bus_routes.items()):
        # Get the coordinates for each node of the current bus route
        nodes = details[0]

        # Initialize a list to store the waypoints for the route
        waypoints = []

        # Initialize a list to store the node numbers for each coordinate
        node_numbers = []

        for node_index, coords in nodes:
            # Add the current node number to the list
            node_numbers.append(f"Node {node_index}")

            # Add the current coordinates as a waypoint
            waypoints.append((coords['latitude'], coords['longitude']))
        
        # Plot the coordinates and node numbers on the map for the current bus route
        for j, (lat, lon) in enumerate(waypoints):
            folium.Marker(location=[lat, lon], popup=node_numbers[j], icon=folium.Icon(color=colors[i])).add_to(route_map)
        
        # Plot the route polyline on the map for the current bus route
        folium.PolyLine(locations=waypoints, color=colors[i], weight=5, opacity=0.8).add_to(route_map)

    # Save the map to an HTML file
    route_map.save('bus_coordinates_map.html')


def generate_js_code(bus_routes):
    js_code = """
    var map = L.map('map').setView([37.7749, -122.4194], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
    """

    colors = ['red', 'blue', 'green', 'orange', 'purple', 'gray', 'black', 'pink', 'yellow']

    for i, (bus, details) in enumerate(bus_routes.items()):
        nodes = details[0]
        road_coords = []

        for node_index, coords in nodes:
            road_coords.append([coords['latitude'], coords['longitude']])

        js_code += f"""
        var route{i} = L.polyline({json.dumps(road_coords)}, {{color: '{colors[i]}', weight: 5, opacity: 0.8}}).addTo(map);
        """

    return js_code

def generate_html(bus_routes):
    js_code = generate_js_code(bus_routes)

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bus Routes Map</title>
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A==" crossorigin=""/>
        <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" crossorigin=""></script>
    </head>
    <body>
        <div id="map" style="height: 600px;"></div>
        <script>
        {js_code}
        </script>
    </body>
    </html>
    """

    return html_content

# def plot_bus_routes(api_key, bus_routes):
#     # Initialize a Folium map
#     route_map = folium.Map()

#     # Define colors for different routes
#     colors = ['red', 'blue', 'green', 'orange', 'purple', 'gray', 'black', 'pink', 'yellow']

#     # Iterate over each bus route
#     for i, (bus, details) in enumerate(bus_routes.items()):
#         # Get the coordinates for each node of the current bus route
#         nodes = details[0]

#         # Initialize a list to store the waypoints for the route
#         waypoints = []

#         # Initialize a list to store the node numbers for each coordinate
#         node_numbers = []

#         for node_index, coords in nodes:
#             # Add the current node number to the list
#             node_numbers.append(f"Node {node_index}")

#             # Add the current coordinates as a waypoint
#             waypoints.append((coords['latitude'], coords['longitude']))
        
#         # Plot the coordinates and node numbers on the map for the current bus route
#         for j, (lat, lon) in enumerate(waypoints):
#             folium.Marker(location=[lat, lon], popup=node_numbers[j], icon=folium.Icon(color=colors[i])).add_to(route_map)
        
#         # Plot the route polyline on the map for the current bus route
#         fetch_and_plot_route(api_key, route_map, waypoints, colors[i])

#     # Save the map to an HTML file
#     route_map.save('bus_routes_map5.html')

# def fetch_and_plot_route(api_key, route_map, waypoints, color):
#     # Define the API URL
#     api_url = 'https://trueway-routing.p.rapidapi.com/route?'

#     # Construct the request URL with parameters
#     url = api_url + 'language=en&vehicle=car'
#     for i, waypoint in enumerate(waypoints):
#         url += f'&locations[{i}][lat]={waypoint[0]}&locations[{i}][lng]={waypoint[1]}'

#     # Set request headers
#     headers = {
#         'x-rapidapi-key': api_key,
#         'x-rapidapi-host': 'trueway-routing.p.rapidapi.com'
#     }

#     # Send the request
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         route_data = response.json()
#         route_coords = [(point['lat'], point['lng']) for point in route_data['route']]
#         folium.PolyLine(locations=route_coords, color=color, weight=5).add_to(route_map)

def plot_bus_routes(api_key, bus_routes):
    # Initialize a Folium map
    route_map = folium.Map()

    # Define colors for different routes
    colors = ['red', 'blue', 'green', 'orange', 'purple', 'gray', 'black', 'pink', 'yellow']

    # Iterate over each bus route
    for i, (bus, details) in enumerate(bus_routes.items()):
        # Get the coordinates for each node of the current bus route
        nodes = details[0]

        # Initialize a list to store the waypoints for the route
        waypoints = []

        # Initialize a list to store the node numbers for each coordinate
        node_numbers = []

        for node_index, coords in nodes:
            # Add the current node number to the list
            node_numbers.append(f"Node {node_index}")

            # Add the current coordinates as a waypoint
            waypoints.append((coords['latitude'], coords['longitude']))
        
        # Plot the coordinates and node numbers on the map for the current bus route
        for j, (lat, lon) in enumerate(waypoints):
            folium.Marker(location=[lat, lon], popup=node_numbers[j], icon=folium.Icon(color=colors[i])).add_to(route_map)
        
        # Plot the route polyline on the map for the current bus route
        fetch_and_plot_route(api_key, route_map, waypoints, colors[i])

    # Save the map to an HTML file
    route_map.save('bus_routes_map.html')

def fetch_and_plot_route(api_key, route_map, waypoints, color):
    # Define the API URL
    api_url = 'https://trueway-routing.p.rapidapi.com/route?'

    # Construct the request URL with parameters
    url = api_url + 'language=en&vehicle=car'
    for i, waypoint in enumerate(waypoints):
        url += f'&locations[{i}][lat]={waypoint[0]}&locations[{i}][lng]={waypoint[1]}'

    # Set request headers
    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': 'trueway-routing.p.rapidapi.com'
    }

    # Send the request
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        route_data = response.json()
        route_coords = [(point['lat'], point['lng']) for point in route_data['route']]
        folium.PolyLine(locations=route_coords, color=color, weight=5).add_to(route_map)

def save_bus_routes_to_js(bus_routes, filename):
    with open(filename, 'w') as file:
        file.write("const busRoutes = [\n")
        for route_index, (route_nodes, _) in enumerate(bus_routes.values(), start=1):
            file.write("    [\n")
            for node_index, coords in route_nodes:
                file.write(f"        {{ 'latitude': {coords['latitude']}, 'longitude': {coords['longitude']} }},\n")
            file.write(f"    ], // Bus {route_index} route\n")
        file.write("];\n")

# if __name__ == "__main__":
#     # Get route details for each bus
#     route_details = main()

#     # Store route details for each bus
#     bus_routes = {}  # Dictionary to store route details for each bus

#     if route_details:
#         for i, (route_nodes, route_distance) in enumerate(route_details):
#             bus_routes[f"Bus {i+1}"] = (route_nodes, route_distance)
#     print(bus_routes)

#     # Print stored route details for each bus

#     api_key = '17509c00d1mshfc009df18a5f92ap1654c1jsnb2757db15c94'
#     # plot_bus_coordinates(api_key, bus_routes) # plot coordinates withour route
#     # Plot bus routes passing through roads
#     plot_bus_routes(api_key, bus_routes)    
    
#     for bus, details in bus_routes.items():
#         print(f"{bus}:")
#         for node_index, coords in details[0]:
#             print(f"   Node {node_index}: {coords}")
#         print(f"   Distance: {details[1]} meters")
    
#     if not bus_routes:
#         print("No solution found!")
        

if __name__ == "__main__":
    # Get route details for each bus
    route_details = main()

    # Store route details for each bus
    bus_routes = {}  # Dictionary to store route details for each bus

    if route_details:
        for i, (route_nodes, route_distance) in enumerate(route_details):
            bus_routes[f"Bus {i+1}"] = (route_nodes, route_distance)

    # Save bus routes to a JavaScript file
    save_bus_routes_to_js(bus_routes, 'bus_routes.js')

    # Print stored route details for each bus
    for bus, details in bus_routes.items():
        print(f"{bus}:")
        for node_index, coords in details[0]:
            print(f"   Node {node_index}: {coords}")
        print(f"   Distance: {details[1]} meters")

    if not bus_routes:
        print("No solution found!")