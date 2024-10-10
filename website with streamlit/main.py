import streamlit as st      # https://docs.streamlit.io/get-started/fundamentals/main-concepts
import pandas as pd
import matplotlib.pyplot as plt

st.title('Simple Data Dashboard')

uploaded_file = st.sidebar.file_uploader('Choose a CSV file', type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    with st.expander('See Data Preview'):
        st.subheader('Data Preview')
        st.write(df.head())
    
    with st.expander('See Data Summary'):
        st.subheader('Data Summary')
        st.write(df.describe())

    # Filtered Data
    st.subheader('Filter Data')
    columns = df.columns.to_list()
    selected_column = st.selectbox('Select Column to filter by', columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox('Select Value', unique_values)
    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    # Plot Data
    st.subheader('Plot Data')
    x_column = st.selectbox('Select x-axis column', columns)
    y_column = st.selectbox('Select y-axis column', columns)

    if st.button('Generate Plot'):
        if x_column != y_column:
            st.line_chart(filtered_df.set_index(x_column)[y_column])
        else:
            st.write('Choose different variables to Plot')
else:
    st.write('Waiting on file upload')