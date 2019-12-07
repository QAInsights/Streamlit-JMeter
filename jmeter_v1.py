import streamlit as st
import pandas as pd
import numpy as np
import datetime
import numpy as np
import subprocess
import os

from pandas import DataFrame

#Checkbox
jmeter_run = st.radio('Select',('Default','Execute','Analyze'))

if jmeter_run == 'Execute':
    JMETER_HOME = 'C:/Users/Navee/OneDrive/Documents/Tools/apache-jmeter-5.2/bin'
    #Upload File to execute
    def jmeter_selector(folder_path='.'):
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox('Select a file to analyze', filenames)
        os.chdir(JMETER_HOME)
        st.text(os.getcwd())
        cmd = "jmeter -n -t" + selected_filename
        returned_value = os.system(cmd)

    jmeterfilename = jmeter_selector()
    st.write('You selected `%s`' % jmeterfilename)

if jmeter_run == 'Analyze':

    #Upload File for Analysis
    def file_selector(folder_path='.'):
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox('Select a file to analyze', filenames)
        return os.path.join(folder_path, selected_filename)

    filename = file_selector()
    st.write('You selected `%s`' % filename)

    #DATA_URL = ('C:\\Users\\Navee\\OneDrive\\Documents\\Tools\\apache-jmeter-5.2\\bin\\Run2.csv')
    DATA_URL = filename

    st.title('Apache JMeter Load Test Results')

    data = pd.read_csv(DATA_URL)
    show_graphs = st.sidebar.checkbox('Show Graphs')

    #Display Start Time
    startTime = data['timeStamp'].iloc[0]/1000
    startTime = datetime.datetime.fromtimestamp(startTime).strftime('%Y-%m-%d %H:%M:%S')
    st.write('Start Time ', startTime)

    endTime = data['timeStamp'].iloc[-1]/1000
    endTime = datetime.datetime.fromtimestamp(endTime).strftime('%Y-%m-%d %H:%M:%S')
    st.write('End Time ', endTime)

    FMT = '%Y-%m-%d %H:%M:%S'
    delta = datetime.datetime.strptime(endTime, FMT) - datetime.datetime.strptime(startTime, FMT)

    st.write('Total duration of the test is HH:MM:SS ', delta)

    st.subheader('Summary Report - Response Time')
    st.write(data.groupby('label')['elapsed'].describe(percentiles=[0.75,0.95,0.99]))

    st.subheader('Error Count')
    errCount = data.groupby(['label','responseCode'])['responseCode'].count()
    st.write(errCount)

    if show_graphs:
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

        st.subheader("Graph between Timestamp and Response Code")
        st.vega_lite_chart(chart_data, {
            "mark": {"type": "bar", "color": "aqua"},    
            "selection": {
                "grid": {
                "type": "interval", "bind": "scales"
                }
            }, 
            'encoding': {
                "tooltip": [
            {"field": "timeStamp", "type": "temporal"},
            {"field": "label", "type": "nominal"},
            {"field": "responseCode", "type": "quantitative"}
            ],
            'x': {'field': 'timeStamp', 'type': 'temporal'},
            'y': {'field': 'responseCode', 'type': 'quantitative'},
            },
            })

        st.subheader("Graph between Timestamp and Response Time")
        st.vega_lite_chart(chart_data, {
            "mark": {"type": "bar", "color": "orange"},    
            "selection": {
                "grid": {
                "type": "interval", "bind": "scales"
                }
            }, 
            'encoding': {
                "tooltip": [
            {"field": "timeStamp", "type": "temporal"},
            {"field": "label", "type": "nominal"},
            {"field": "elapsed", "type": "quantitative"}
            ],
            'x': {'field': 'timeStamp', 'type': 'temporal'},
            'y': {'field': 'elapsed', 'type': 'quantitative'},
            },
            })

        st.subheader("Graph between Timestamp and Connect Time")
        st.vega_lite_chart(chart_data, {
            "mark": {"type": "bar", "color": "darkgreen"},    
            "selection": {
                "grid": {
                "type": "interval", "bind": "scales"
                }
            }, 
            'encoding': {
                "tooltip": [
            {"field": "timeStamp", "type": "temporal"},
            {"field": "label", "type": "nominal"},
            {"field": "Connect", "type": "quantitative"}
            ],
            'x': {'field': 'timeStamp', 'type': 'temporal'},
            'y': {'field': 'Connect', 'type': 'quantitative'},
            },
            })

        st.subheader("Graph between Timestamp and bytes")
        st.vega_lite_chart(chart_data, {
            "mark": {"type": "bar", "color": "darkblue"},    
            "selection": {
                "grid": {
                "type": "interval", "bind": "scales"
                }
            }, 
            'encoding': {
                "tooltip": [
            {"field": "timeStamp", "type": "temporal"},
            {"field": "label", "type": "nominal"},
            {"field": "bytes", "type": "quantitative"}
            ],
            'x': {'field': 'timeStamp', 'type': 'temporal'},
            'y': {'field': 'bytes', 'type': 'quantitative'},
            },
            })

        st.subheader("Graph between Timestamp and Response Time - Line Chart")
        st.vega_lite_chart(chart_data, {
        "mark": "line",
    "encoding": {
        "tooltip": [
            {"field": "timeStamp", "type": "temporal"},
            {"field": "label", "type": "nominal"},
            {"field": "elapsed", "type": "quantitative"}
            ],
        "x": {"field": "timeStamp", "type": "temporal"},
        "y": {"field": "elapsed", "type": "quantitative"},
        "color": {"field": "label", "type": "nominal"}
    },
            })
    
        st.subheader("Graph between Timestamp and Response Time - Bar Chart")
        st.vega_lite_chart(chart_data, {
        "mark": "bar",
    "encoding": {
        "tooltip": [
            {"field": "timeStamp", "type": "temporal"},
            {"field": "label", "type": "nominal"},
            {"field": "elapsed", "type": "quantitative"}
            ],
        "x": {"field": "timeStamp", "type": "temporal"},
        "y": {"field": "elapsed", "type": "quantitative"},
        "color": {"field": "label", "type": "nominal"}
    },
            })

        st.subheader("Histogram")
        st.vega_lite_chart(chart_data, {
            "transform": [{
            "filter": {"and": [
            {"field": "timeStamp", "valid": True},
            {"field": "elapsed", "valid": True}
            ]}
        }],
        "mark": "rect",
        "width": 300,
        "height": 200,
        "encoding": {
            "x": {
            "field": "timeStamp",
            "type": "temporal"
            },
            "y": {
            "field": "elapsed",
            "type": "quantitative"
            },
            "color": {
            "aggregate": "count",
            "type": "quantitative"
            }
        },
        "config": {
            "view": {
            "stroke": "transparent"
            }
        }
                })

        st.subheader("Histogram")
        st.vega_lite_chart(chart_data, {
            "transform": [{
            "filter": {"and": [
            {"field": "timeStamp", "valid": True},
            {"field": "Connect", "valid": True}
            ]}
        }],
        "mark": "rect",
        "width": 300,
        "height": 200,
        "encoding": {
            "x": {
            "field": "timeStamp",
            "type": "temporal"
            },
            "y": {
            "field": "Connect",
            "type": "quantitative"
            },
            "color": {
            "aggregate": "count",
            "type": "quantitative"
            }
        },
        "config": {
            "view": {
            "stroke": "transparent"
            }
        }
                })

        st.subheader("Scatter Plot between Timestamp and Response Time")
        st.vega_lite_chart(chart_data, {
                
            "selection": {
            "grid": {
            "type": "interval", "bind": "scales"
            }
        },
        "mark": "circle",
        "encoding": {
            "tooltip": [
                {"field": "timeStamp", "type": "temporal"},
                {"field": "label", "type": "nominal"},
                {"field": "elapsed", "type": "quantitative"}
                ],
            "x": {
            "field": "timeStamp", "type": "temporal"    },
            "y": {
            "field": "elapsed", "type": "quantitative"    },
            "size": {"field": "label", "type": "nominal"}
        },
                })
        
