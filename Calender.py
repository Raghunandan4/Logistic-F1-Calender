import math

# define a function to calculate the distance between two pts(lat1, lon1) and (lat2, lon2)

def distance(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # apply the Haversine formula to calculate the distance
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = 6371 * c # 6371 is the radius of the Earth in kilometers
    return distance

# define a function to find the nearest neighbour to a given point(lat, lon)

def nearest_neighbor(lat, lon, points):
    min_distance = float('inf') # initialise min_distance with infinity
    nearest_neighbor = None # initialize nearest_neighbour with None
    for point in points:
        d = distance(lat, lon, point[0], point[1]) # calculate the distance between the two points
        if d < min_distance: # if the distance is smaller than the current min_distance, update min_distance and nearest neighbour 
           min_distance = d
           nearest_neighbor = point
        return nearest_neighbor    

# define the list of points (countries)

points = [
    (26.8347, 50.5089), # Bahrain
    (21.6334, 39.1035), # Saudi Arabia
    (-37.8490, 144.9680), # Australia
    (40.4083, 49.8622), # Azerbaijan
    (25.9566, -80.2310), # Miami
    (44.3447, 11.7155), # Imola
    (43.7347, 7.4197), # Monaco
    (41.5728, 2.2661), # Spain
    (45.5079, -73.5290), # Canada
    (47.2183, 14.7606), # Austria
    (52.8786, -1.0169), # Great Britain
    (47.5106, 19.2556), # Hungary
    (50.4373, 5.9750), # Belgium
    (52.3744, 4.5397), # Netherlands
    (45.6237, 9.2844), # Monza
    (1.2931, 103.8550), # Singapore
    (34.8414, 136.5460), # Japan 
    (25.4861, 51.4523), # Qatar
    (30.1375, -97.6400), # Austin
    (19.4052, -99.0930), # Mexico
    (-23.7010, -46.6980), # Brazil
    (36.1068, -115.1600), # Las Vegas
    (24.4749, 54.6038), # Abu Dhabi
    ]

total_distance = 0 # initialize total_distance

current_point = points[0] # start at the first point

path = [current_point] # add the first point to the path

points.remove(current_point) # remove the first point from the list of points 

while len(points) > 0: # repeat untill all points have been visited 

    next_point = nearest_neighbor(current_point[0], current_point[1], points) # type: ignore find the nearest neighbour to the current point

    path.append(next_point) # type: ignore # add the nearest neighbour to the path

    points.remove(next_point) # type: ignore # remove the nearest neighbour from the list of the points

    total_distance += distance(current_point[0], current_point[1], next_point[0], next_point[1]) # type: ignore add the distance to the total distance

    current_point = next_point # update the current point


# print the order of the points in the path

print("Order of points: ")
for point in path:
    print(point)

# print the total distance

print("Total distance: %.2f kilometers" % total_distance)
