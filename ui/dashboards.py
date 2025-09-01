import streamlit as st
import plotly.express as px
import pandas as pd


def gen_chart(fig,name):

    st.plotly_chart(fig, use_container_width=True)