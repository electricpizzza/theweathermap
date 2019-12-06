import folium
import pandas

cities = pandas.read_json("Morocco.json")
cities
latCity = list(cities["lat"])
lonCity = list(cities["lng"])
nameCity = list(cities["name"])
country = list(cities["country"])

cityMap = folium.FeatureGroup(name = "Cities")
for lat,lon,city in zip(latCity,lonCity,nameCity):
        html ="<main class='main' id='"+str(lat)+","+str(lon)+"'><div class='location'><h1 class='loc-timezon'></h1><canvas id='icon1' width='100' height='100'></canvas></div><div class='temperatur'><div> <h2 class='degre'></h2> <span id='fc'>C</span></div><div class='discription'></div></div></main>"
        cityMap.add_child(folium.CircleMarker(location=[lat,lon],popup=html,radius=6,fill_color='red',icon=folium.Icon(color='red')))

#f = folium.FeatureGroup(name="ZACK Map")

fg = folium.FeatureGroup(name="geojson")
fg.add_child(folium.CircleMarker(location=[31.056376, -9.033904],radius=1))

map1 = folium.Map(Location=[34.056376, -5.033904],zoom_start =13,
center=[34.056376, -5.033904])
# for la ,lo , na in zip(lat, lon , name):
#         map1.add_child(folium.CircleMarker(location = [la ,lo], popup=na,radius=6,fill_color='red'))
# map1.add_child(folium.Marker(location = (34.056376, -5.033904),
# popup="<div style='width:200px; height:300px; background-color:red;'><h1>hello Im here bItshes</h1></div>",
# icon=folium.Icon(color="red",prifix="fa fa-refresh")))


#f.add_child(folium.GeoJson(data = open("world.json","r",encoding="utf-8-sig").read(),
#style_function=lambda x : {'fillColor':'red' if x['properties']['NAME'] == 'Morocco' else 'green' ,'color':'green'}))

map1.add_child(cityMap)
map1.add_child(fg)
#map1.add_child(f)
map1.add_child(folium.LayerControl())
map1.save("newMap.html")
print("map is ready")
#help(map1)