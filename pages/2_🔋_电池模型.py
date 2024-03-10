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

experiment_choice = st.selectbox(
    "选择要仿真的工况",
    ("CCCV", "DST")
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

    if experiment_choice == "CCCV":
        experiment = pybamm.Experiment([
            "Discharge at C/2 for 10 hours or until 2.5 V",
            "Rest for 1 hour",
            "Charge at 1 A until 4.2 V",
            "Hold at 4.2 V until C/50",
        ])
    elif experiment_choice == "DST":
        experiment = pybamm.Experiment([
            "Discharge at 2C for 10 seconds",
            "Rest for 20 seconds",
            "Discharge at 1C for 10 seconds",
            "Rest for 20 seconds",
            "Charge at 1C for 10 seconds",
            "Rest for 20 seconds",
            "Charge at 2C for 10 seconds",
            "Rest for 20 seconds",
        ]*10)

    # 创建并解决仿真
    sim = pybamm.Simulation(model, experiment=experiment, parameter_values=parameter_values)
    solution = sim.solve()

    # 将仿真结果转换为 DataFrame
    data = solution["Terminal voltage [V]"].entries
    time = solution["Time [s]"].entries
    chart_data = pd.DataFrame({"time": time, "voltage": data})
    current_data = solution["Current [A]"].entries

    # 创建你的图表并获取图表对象
    fig, ax = plt.subplots()
    ax.plot(time, data)
    # 设置y轴的范围
    # ax.set_ylim([2.45, 4.3])  # 你可以根据需要设置y_min和y_max
    # 设置x轴和y轴的标签，并设置标签大小
    ax.set_xlabel("时间/s", fontsize=14)  # x轴标签
    ax.set_ylabel("电压/V", fontsize=14)  # y轴标签
    # 使用mpld3将图表转换为HTML
    fig_html = mpld3.fig_to_html(fig)
    # 在Streamlit中显示这个HTML
    components.html(fig_html, height=600)

    # 创建你的图表并获取图表对象
    fig2, ax2 = plt.subplots()
    ax2.plot(time, current_data, color="#00d596")
    # 设置x轴和y轴的标签，并设置标签大小
    ax2.set_xlabel("时间/s", fontsize=14)  # x轴标签
    ax2.set_ylabel("电流/A", fontsize=14)  # y轴标签
    # 使用mpld3将图表转换为HTML
    fig2_html = mpld3.fig_to_html(fig2)
    # 在Streamlit中显示这个HTML
    components.html(fig2_html, height=600)
