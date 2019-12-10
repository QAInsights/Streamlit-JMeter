import streamlit as st

def display_about():
    st.title('About')
    st.markdown('---')
    st.markdown('![JMeter Streamlit](/images/header.jpg)')

def display_sidebar():
    st.sidebar.markdown('---')
    
    st.sidebar.title('Contribute')
    st.sidebar.info('This is an open source project, you are very welcome to contribute something awesome by commenting, \
        feature requests, pull requests, raising [issues](https://github.com/QAInsights/Streamlit-JMeter/issues).')
    st.sidebar.title('About')

    st.sidebar.info('This app has been developed by [NaveenKumar Namachivayam](https://qainsights.com) using [Python](https://www.python.org/), \
    [Streamlit](https://streamlit.io/), and [Vega Lite](https://vega.github.io/vega-lite/). You can checkout the source code at \
    [GitHub](https://github.com/QAInsights/Streamlit-JMeter).')
    

