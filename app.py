import streamlit as st
import folium
from streamlit_folium import st_folium
from get_data import add_dpt_wms_layer

st.set_page_config(page_title="GeoAgro WMS Viewer", layout="wide")
st.title("🗺️ ผังเมืองกรมโยธาธิการและผังเมือง (WMS)")

# ศูนย์กลางเริ่มต้น: กรุงเทพฯ
center = [13.7563, 100.5018]

# สร้างแผนที่ Folium
m = folium.Map(location=center, zoom_start=6)

# เรียกใช้ฟังก์ชันจาก get_data.py
add_dpt_wms_layer(m)

# เพิ่ม Layer Control
folium.LayerControl().add_to(m)

# แสดงผลบน Streamlit
st_folium(m, width=1000, height=600)
