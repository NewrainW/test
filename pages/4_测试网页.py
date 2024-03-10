"""
作者：wxy
日期：2024年01月27日
"""
import matplotlib.pyplot as plt
import mpld3
import streamlit as st
import streamlit.components.v1 as components
import pybamm
import pandas as pd

# 在页面中间让用户选择模型
model_name = st.selectbox(
    "选择一个模型",
    ("SPM", "SPMe", "DFN")
)

# 创建一个开始仿真的按钮
if st.button('开始仿真', type="primary"):
    # 根据用户选择的模型创建模型对象
    parameter_values = pybamm.ParameterValues("Chen2020")
    if model_name == "SPM":
        model = pybamm.lithium_ion.SPM()
    elif model_name == "SPMe":
        model = pybamm.lithium_ion.SPMe()
    else:
        model = pybamm.lithium_ion.DFN()

    experiment = pybamm.Experiment([
                                       "Discharge at C/10 for 10 hours or until 3.3 V",
                                       "Rest for 1 hour",
                                       "Charge at 1 A until 4.1 V",
                                       "Hold at 4.1 V until 50 mA",
                                       "Rest for 1 hour",
                                   ] * 3)
    # 创建并解决仿真
    sim = pybamm.Simulation(model, experiment=experiment, parameter_values=parameter_values)
    solution = sim.solve()

    # 将仿真结果转换为 DataFrame
    data = solution["Terminal voltage [V]"].entries
    time = solution["Time [s]"].entries
    chart_data = pd.DataFrame({"time": time, "voltage": data})

    # 获取电流数据
    current_data = solution["Current [A]"].entries

    # 创建你的图表并获取图表对象
    fig1, ax1 = plt.subplots()
    ax1.plot(time, data)
    # 设置y轴的范围
    ax1.set_ylim([3.2, 4.2])  # 你可以根据需要设置y_min和y_max
    # 设置x轴和y轴的标签，并设置标签大小
    ax1.set_xlabel("时间/s", fontsize=14)  # x轴标签
    ax1.set_ylabel("电压/V", fontsize=14)  # y轴标签
    # 使用mpld3将图表转换为HTML
    fig1_html = mpld3.fig_to_html(fig1)
    # 在Streamlit中显示这个HTML
    components.html(fig1_html, height=400)


    # 创建你的图表并获取图表对象
    fig2, ax2 = plt.subplots()
    ax2.plot(time, current_data)
    # 设置x轴和y轴的标签，并设置标签大小
    ax2.set_xlabel("时间/s", fontsize=14)  # x轴标签
    ax2.set_ylabel("电流/A", fontsize=14)  # y轴标签
    # 使用mpld3将图表转换为HTML
    fig2_html = mpld3.fig_to_html(fig2)
    # 在Streamlit中显示这个HTML
    components.html(fig2_html, height=600)
