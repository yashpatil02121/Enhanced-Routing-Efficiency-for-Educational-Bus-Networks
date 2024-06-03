import folium

def plot_bus_routes(map):
    bus_routes = [
        [(40.629041, -74.025606), (40.629041, -74.025606), (40.631234, -74.028974), (40.632567, -74.022345)],  # Bus 1 route
        [(40.629041, -74.025606), (40.629041, -74.025606), (40.628942, -74.021566), (40.631768, -74.027412)],  # Bus 2 route
        [(40.629041, -74.025606), (40.629041, -74.025606), (40.631482, -74.025962), (40.633245, -74.029378)],  # Bus 3 route
        [(40.629041, -74.025606), (40.644895, -74.013818), (40.630099, -73.993521), (40.627177, -73.980853), (40.629041, -74.025606)]  # Bus 4 route
    ]

    colors = ['red', 'green', 'blue', 'purple']

    for index, route in enumerate(bus_routes):
        folium.PolyLine(locations=route, color=colors[index], weight=5).add_to(map)

map = folium.Map(location=[40.629041, -74.025606], zoom_start=13)
plot_bus_routes(map)
folium.TileLayer('openstreetmap').add_to(map)
map.save('routes_map.html')
