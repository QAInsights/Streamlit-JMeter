# Powering up Apache JMeter with Streamlit

## Overview

Apache JMeter is an open source load testing tool written in 100% pure Java. JMeter supports umpteen protocols including HTTP(S), FTP, SMTP, Web Services, JMS and much more. In JMeter, you can generate HTML results after you done with the execution or you can use Backend Listeners to monitor the runtime results. 

Streamlit is an open source framework for Machine Learning and Data Sciences team. You can build tools to visualize the data and interactive prototypes.

## Apache JMeter + Streamlit

By integrating Streamlit with Apache JMeter, you can build machine learning models to train to detect anomalies from your JMeter test results. This project is just a beginning where you can execute and visualize the test results in interactive charts.

## Prerequisities

* [Apache JMeter](https://jmeter.apache.org/download_jmeter.cgi)
* Your favorite IDE (I ❤ [VS Code](https://code.visualstudio.com/))
* [Python 2.7.0 or later / Python 3.6.x or later](https://www.python.org/downloads/)
* [PIP](https://pip.pypa.io/en/stable/installing/)
* [Streamlit](https://streamlit.io/docs/index.html)

Use the latest version as possible.

## Streamlit Installation

I prefer [Anaconda](https://www.anaconda.com/) to install the Streamlit, you can follow the instructions mentioned [here](https://streamlit.io/docs/getting_started.html).

## JMeter Installation

[Getting Started](https://jmeter.apache.org/usermanual/get-started.html#running) with JMeter.

## Streamlit Hello World

After installing all the necessary components, you could run a `hello` program by invoking `streamlit hello`. This will open a browser (or new tab). You can run Streamlit from your Github Gists, e.g. `streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/app.py`
