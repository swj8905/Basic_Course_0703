import folium

map = folium.Map(location=[37.49787837381732, 127.02768848187284],
           zoom_start=17)
map.save("./map.html")