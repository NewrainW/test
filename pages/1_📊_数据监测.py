import streamlit as st
import altair as alt
import time
import pandas as pd
from streamlit_extras.metric_cards import style_metric_cards
import random


hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
temperature_placeholder = col1.empty()
voltage_placeholder = col2.empty()
current_placeholder = col3.empty()
num1 = random.uniform(20, 21)
num1 = round(num1, 2)
num2 = random.uniform(11, 11.15)
num2 = round(num2, 2)
num3 = random.uniform(2, 3)
num3 = round(num3, 2)

# 初始化数据
chart_data = pd.DataFrame({'time': [pd.Timestamp.now()], 'value': [num1]})
chart = alt.Chart(chart_data).mark_line().encode(
    x=alt.X('time:T', axis=alt.Axis(title='时间/t')),
    y=alt.Y('value:Q', axis=alt.Axis(title='温度/°C')),
).properties(
    title='温度监测图',
    width=600,
    height=400
)
# 在Streamlit应用程序中显示图表
style_metric_cards()
chart_placeholder = st.altair_chart(chart)

while True:
    last_temperature = num1
    last_current = num3
    last_voltage = num2
    num1 = random.uniform(20, 21)
    num1 = round(num1, 2)
    num2 = random.uniform(11, 11.15)
    num2 = round(num2, 2)
    num3 = random.uniform(2, 3)
    num3 = round(num3, 2)
    # temperature_text.text(f'Current temperature: {temperature}°C')
    temperature_placeholder.metric(label="温度", value=f"{num1}°C", delta=f"{round(num1-last_temperature,2)}°C")
    voltage_placeholder.metric(label="电压", value=f"{num2}V", delta=f"{round(num2-last_voltage,2)}V")
    current_placeholder.metric(label="电流", value=f"{num3}A", delta=f"{round(num3-last_current,2)}A")
    new_data = pd.DataFrame({'time': [pd.Timestamp.now()], 'value': [num1]})
    chart_data = pd.concat([chart_data, new_data])
    # 更新图表数据
    chart = alt.Chart(chart_data).mark_line().encode(
        x=alt.X('time:T', axis=alt.Axis(title='时间/t')),
        y=alt.Y('value:Q', axis=alt.Axis(title='温度/°C')),
    ).properties(
        title='温度监测图',
        width=600,
        height=400
    )
    # 在Streamlit应用程序中更新图表
    chart_placeholder.altair_chart(chart)
    time.sleep(1)
