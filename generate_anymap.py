from anymap_ts import Map

m = Map(center=[-122.4, 37.8], zoom=10)
m.add_basemap("OpenStreetMap")
m.add_draw_control(position="top-left")
m.add_layer_control()

# m and m.get_draw_data() are notebook commands; we'll focus on saving to HTML
m.to_html("anymap_output.html")
print("anymap_output.html has been generated successfully.")
