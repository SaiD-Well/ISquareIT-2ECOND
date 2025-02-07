import numpy as np
import pandas as pd
import streamlit as st

st.title("This is REX")
st.write("Python requires alot of practice!!!")

data = pd.DataFrame({'c1':[10,20,30,40],'c2':['A','B','C','D']})

st.write("Below is table for Data")

st.write(data)
chart_data = pd.DataFrame(np.random.randn(20,3),columns=['A','B','C'])
st.line_chart(chart_data)
st.bar_chart(chart_data)
st.area_chart(chart_data)
