import streamlit as st
import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.markdown('''
# ** EDA App**

This is an **EDA App** created in Streamlit using pandas-profiling library

**Credit:** App built in 'Python' + 'Streamlit by Chanin Nantasenamat aka the Data Professor

___
''')

with st.sidebar.header("1. Upload your CSV or Excel data"):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV or Excel file", type=['csv','xlsx'])
    st.sidebar.markdown('[Example CSV input file](https://raw.githubusercontent.com/ldruizsan/eda-app/main/delaney_solubility_with_descriptors.csv)')

if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    
    @st.cache
    def load_excel():
        excel = pd.read_excel(uploaded_file)
        return excel

    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded')
    if st.button("Press to use sample dataset"):
        @st.cache
        def load_data():
            a = pd.DataFrame(np.random.rand(100,5),
                            columns=['a','b','c','d','e'])
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)