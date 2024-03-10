import streamlit as st
import altair as alt
import time
import pandas as pd
import pymysql
import random
from streamlit_extras.metric_cards import style_metric_cards
import streamlit_echarts as st_echarts

st.set_page_config(page_title="电池在线参数辨识", layout="wide")

# 连接mysql
conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       passwd='123456',
                       charset="utf8",
                       db="battery_db",
                       cursorclass=pymysql.cursors.DictCursor)


def get_latest_data():
    cursor = conn.cursor()
    cursor.execute("select * from battery_data1 order by id desc limit 1")
    return cursor.fetchone()


def new_monitoring(new_data):
    previous_data = new_data
    new_data = get_latest_data()
    temperature_placeholder.metric(label="温度",
                                   value=f"{new_data['temperature']}°C",
                                   delta=f"{new_data['temperature'] - previous_data['temperature']}°C")
    voltage_placeholder.metric(label="电压",
                               value=f"{new_data['CurrentVoltage']}V",
                               delta=f"{new_data['CurrentVoltage'] - previous_data['CurrentVoltage']}V")
    current_placeholder.metric(label="电流",
                               value=f"{new_data['Current']}A",
                               delta=f"{new_data['Current'] - previous_data['Current']}A")
    voltage1.metric(label="温度",
                    value=f"{new_data['temperature']}°C",
                    delta=f"{new_data['temperature'] - previous_data['temperature']}°C")
    voltage2.metric(label="电压",
                    value=f"{new_data['CurrentVoltage']}V",
                    delta=f"{new_data['CurrentVoltage'] - previous_data['CurrentVoltage']}V")
    voltage3.metric(label="电流",
                    value=f"{new_data['Current']}A",
                    delta=f"{new_data['Current'] - previous_data['Current']}A")


# 状态监测栏
col11, col12, col13 = st.columns(3)
temperature_placeholder = col11.empty()
voltage_placeholder = col12.empty()
current_placeholder = col13.empty()
col21, col22, col23 = st.columns(3)
voltage1 = col21.empty()
voltage2 = col22.empty()
voltage3 = col23.empty()

# soh和soc状态
soc_column, soh_column = st.columns(2)

latest_data = get_latest_data()
# 在Streamlit应用程序中显示图表
style_metric_cards()

while True:
    new_monitoring(latest_data)
    time.sleep(1)
