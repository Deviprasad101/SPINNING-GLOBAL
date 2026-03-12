from anymap_ts import MapLibreMap

m = MapLibreMap(
    center=[-74.0060, 40.7128],
    zoom=15,
    pitch=60,
    bearing=-17,
    style="https://tiles.openfreemap.org/styles/liberty"
)

m.add_control_grid(
    exclude=[
        "GeoportailFrance.plan", 
        "GeoportailFrance.orthos", 
        "GeoportailFrance.parcels",
        "GeoportailFrance.CorineLandCover",
        "GeoportailFrance.ignMaps",
        "GeoportailFrance.parcel"
    ]
)

m.add_3d_terrain(exaggeration=1.5)
m.add_3d_buildings(
    fill_extrusion_color="#4682B4", # Steel blue
    fill_extrusion_opacity=0.8
)
m.add_layer_control(position="bottom-left")

m.to_html("buildings_3d_example.html")
print("Successfully wrote buildings_3d_example.html with 3D features and Control Grid")
