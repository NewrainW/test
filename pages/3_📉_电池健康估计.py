import random
import time
import streamlit as st
from streamlit_echarts import st_echarts

st.set_page_config(page_title="电池健康估计", layout="wide")


def render_ring_gauge():
    # battery_capacity = round(random.random(), 2)
    battery_capacity = 0.86
    data = [battery_capacity]
    if battery_capacity > 0.8:
        data.append(0.8)
    if battery_capacity > 0.6:
        data.append(0.6)
    if battery_capacity > 0.4:
        data.append(0.4)
    if battery_capacity > 0.2:
        data.append(0.2)
    option1 = {
        "title": {
            "text": "当前电量",
            "subtext": "SOC估计",
            "left": "center"
        },
        "series": [
            {
                "type": "liquidFill",
                "data": data,
                "radius": "70%",
                "outline": {
                    "borderDistance": 0,
                    "itemStyle": {
                        "borderWidth": 8,
                        "borderColor": "#156ACF",
                        "shadowBlur": 20,
                        "shadowColor": "rgba(0, 0, 0, 0.25)"
                    }
                },
                "backgroundStyle": {
                    "color": "#E3F7FF"
                },
                "label": {
                    "normal": {
                        "formatter": f"{battery_capacity * 100}%",
                        "fontSize": 50,
                        "color": "#FFFFFF"
                    }
                }
            }
        ]
    }
    option = {
        "title": {
            "text": "电池剩余寿命",
            "subtext": "SOH估计",
            "left": "center"
        },
        "series": [
            {
                "type": "gauge",
                "startAngle": 90,
                "endAngle": -270,
                "pointer": {"show": False},
                "progress": {
                    "show": True,
                    "overlap": False,
                    "roundCap": True,
                    "clip": False,
                    "itemStyle": {"borderWidth": 10, "borderColor": "#00d596"},
                },
                "axisLine": {"lineStyle": {"width": 10}},
                "splitLine": {"show": False, "distance": 0, "length": 0},
                "axisTick": {"show": False},
                "axisLabel": {"show": False, "distance": 0},
                "data": [
                    {
                        "value": 97,
                        "name": "健康值",
                        "title": {"offsetCenter": ["0%", "0%"]},
                        "detail": {"offsetCenter": ["0%", "20%"]},
                    }
                ],
                "title": {"fontSize": 14},
                "detail": {
                    "width": 50,
                    "height": 14,
                    "fontSize": 14,
                    "color": "auto",
                    "borderColor": "auto",
                    "borderRadius": 20,
                    "borderWidth": 1,
                    "formatter": "{value}%",
                },
            }
        ]
    }

    with soc_column:
        st_echarts(option1, height="400px", key="echarts1")
    with soh_column:
        st_echarts(option, height="400px", key="echarts2")
    time.sleep(2)
    st.experimental_rerun()


soc_column, soh_column = st.columns(2)

while True:
    render_ring_gauge()
    time.sleep(2)
