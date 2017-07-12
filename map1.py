import folium
import pandas

data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

map=folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Mapbox Bright")
fgv=folium.FeatureGroup(name="My Map")
fgp=folium.FeatureGroup(name="My Population")
def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000<=elevation<3000:
        return "orange"
    else:
        return "red"

for i,j,k in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[i,j],popup=str(k)+" m",radius=4,color=color_producer(k),fill_color=color_producer(k)))

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig'),
style_function=lambda x:{'fillColor':'yellow' if x['properties']['POP2005']<10000000
else 'orange' if 10000000 <= x['properties']['POP2005']<20000000 else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
