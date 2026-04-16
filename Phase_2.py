import pandasas pd
from distanceimport haversine

data = pd.read_csv("places.csv")

user_lat =28.6130
user_lon =77.2095

distances = []

for _, rowin data.iterrows():
    d = haversine(user_lat, user_lon, row['latitude'], row['longitude'])
    distances.append(d)

data['distance'] = distances

print(data)

