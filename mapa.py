import json

def leer_waypoints():
    try:
        with open("map.tmj", "r") as mapa:
            datos = json.load(mapa)
            for layer in datos["layers"]:
                if layer["name"] == "waypoints":
                    for obj in layer["objects"]:
                        waypoint_data = obj["polyline"]
            print(waypoint_data)
    except Exception as e:
        print("Error:", e)

def procesar_waypoints(waypoint_data):
    waypoints = []
    for e in waypoint_data:
        temp_x = e['x']
        temp_y = e['y']
        waypoints.append((temp_x, temp_y))