import streamlit as st

def display_about():
    st.markdown('## About')

    st.markdown('By leveraging Streamlit with [JMeter](http://jmeter.apache.org) which brings machine learning capabailities to detect the anamolies and to study the performance of your application.\
            Using this repo, you can run your JMeter scripts and visualize the results instantly. \
            Streamlit brings intuitive user interface for your JMeter execution and results analysis.')
    
    st.markdown('![JMeter Streamlit](https://raw.githubusercontent.com/QAInsights/Streamlit-JMeter/master/images/header.jpg)')
    st.markdown('### Limitations')
    st.markdown('* Supports only CSV results ')
    st.markdown('* By default, it fetches all the files from the `JMETER_HOME` folder.')
    st.markdown('* Limited number of charts has been added, other type of charts can be added by custom coding.')

    st.markdown('### Known Issues')
    st.markdown('* Doesn\'t execute if the JMeter file name which has space')
    st.markdown('* Quick Navigation between Execute and Analyze may break the code, you may need to launch the app again.')
    st.markdown('* Doesn\'t display the JMeter test results runtime')


def display_sidebar():
    st.sidebar.markdown('---')
    
    st.sidebar.title('Contribute')
    st.sidebar.info('This is an open source project, you are very welcome to contribute something awesome by commenting, \
        feature requests, pull requests, and by raising [defects](https://github.com/QAInsights/Streamlit-JMeter/issues).')
    st.sidebar.title('About')

    st.sidebar.info('This app has been developed by [NaveenKumar Namachivayam](https://qainsights.com) using [Python](https://www.python.org/), \
    [Streamlit](https://streamlit.io/), and [Vega Lite](https://vega.github.io/vega-lite/). You can checkout the source code at \
    [GitHub](https://github.com/QAInsights/Streamlit-JMeter).')