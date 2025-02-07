import numpy as np
import pandas as pd
import streamlit as st




st.title("Welcome Everyone")
st.write("Hello Guys !")
data=pd.DataFrame({'c1':[10,20,30,40],'c2':['a','b','c','d'],'c3':['varun','dhiraj','dinesh','sagar']})
st.write(data)

chart_data=pd.DataFrame(np.random.rand(20,4),columns=['A','B','C','D'])
st.line_chart(chart_data)