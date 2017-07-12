import folium
import pandas

data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

map=folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Mapbox Bright")
fg=folium.FeatureGroup(name="My Map")

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000<=elevation<3000:
        return "orange"
    else:
        return "red"

for i,j,k in zip(lat,lon,elev):
    fg.add_child(folium.CircleMarker(location=[i,j],popup=str(k)+" m",radius=4,color=color_producer(k),fill_color=color_producer(k)))
map.add_child(fg)
map.save("Map1.html")
