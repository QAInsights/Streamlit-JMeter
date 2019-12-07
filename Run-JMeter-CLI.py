import streamlit as st
import subprocess
import os
import pandas as pd
import numpy as np
import datetime
import numpy as np

# JMETER_HOME
JMETER_HOME = 'C:/Users/Navee/OneDrive/Documents/Tools/apache-jmeter-5.2/bin'
# Get Script Path
scriptLoc = st.text_input('Input your JMeter script path:') 
# Get Results File
resultsLoc = st.text_input('Input your JMeter results path:')

if st.button('START'):
    os.chdir(JMETER_HOME)
    st.text(os.getcwd())
    cmd = "jmeter -n -t Sample.jmx"
    returned_value = os.system(cmd)
    st.text(returned_value)
from pandas import DataFrame
DATA_URL = (resultsLoc)

st.title('Apache JMeter Load Test Results')

data = pd.read_csv(DATA_URL)

st.subheader('Summary Report - Response Time')
st.write(data.groupby('label')['elapsed'].describe(percentiles=[0.75,0.95,0.99]))

chart_data = pd.DataFrame(data,columns=['timeStamp','Latency','label','responseCode','elapsed','Connect','bytes'])

st.subheader("Graph between Timestamp and Latency")
        
st.vega_lite_chart(chart_data, {
        "mark": {"type": "bar", "color": "maroon"},    
        "selection": {
            "grid": {
            "type": "interval", "bind": "scales"
            }
        }, 
        'encoding': {
            "tooltip": [
        {"field": "timeStamp", "type": "temporal"},
        {"field": "label", "type": "nominal"},
        {"field": "Latency", "type": "quantitative"}
        ],
        'x': {'field': 'timeStamp', 'type': 'temporal'},
        'y': {'field': 'Latency', 'type': 'quantitative'},
        },
        })

#if st.button('STOPS'):
    #os.chdir(JMETER_HOME)
    #cmd = "stoptest.cmd"
    #returned_value = os.system(cmd)
    #cmd = "a"
    #returned_value = os.system(cmd)
    #st.text('Test has been stopped')

#if st.button('SHTUDOWN'):
    #os.chdir(JMETER_HOME)
    #cmd = "shutdown.cmd"
    #returned_value = os.system(cmd)
    #cmd = "a"
    #returned_value = os.system(cmd)
    #st.text('Test has been shutdowned')