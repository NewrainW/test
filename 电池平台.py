import streamlit as st

st.set_page_config(
    page_title="哈尔滨工业大学威海-云里悟锂电池数据分析云平台",
    page_icon="👋",
)

st.write("# 哈工大（威海)云里悟锂电池平台 ")

st.sidebar.success("请选择要使用的模块")

st.markdown(
    """
    😊欢迎来到这里，本网站由哈尔滨工业大学（威海）-新能源车辆实验室建立，
    用于构建大数据分析及电池管理云平台。通过本网站可以对电池数据进行远程实时监测，并对电池进行精准的状态估计。
    ### 
    - [导师主页](http://homepage.hit.edu.cn/lijunfu)
"""
)
