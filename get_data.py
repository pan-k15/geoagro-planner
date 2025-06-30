import folium

def add_dpt_wms_layer(m):
    folium.raster_layers.WmsTileLayer(
        url="https://dptgis.dpt.go.th/arcgis/services/PLLU_ALLv3/MapServer/WMSServer?",
        layers="0",
        name="ผังเมืองกรมโยธาฯ",
        fmt="image/png",
        transparent=True,
        version="1.3.0",
        attr="กรมโยธาธิการและผังเมือง",  # ✅ use 'attr' instead of 'attribution'
        overlay=True,
        control=True
    ).add_to(m)
