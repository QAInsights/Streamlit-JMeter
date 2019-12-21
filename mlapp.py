import numpy as np
import pandas as pd

import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms
from sklearn.cluster import KMeans


st.title("Machine Learning")
url = "one.csv"
names = ['elapsed','label']
dataset = pd.read_csv(url, names=names)
st.write(dataset)