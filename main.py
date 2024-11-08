import streamlit as st
import pandas as pd
import psycopg2
import matplotlib.pyplot as plt

# # Database connection parameters
# connection_params = {
#     'user': 'postgres',
#     'password': 'pawel',
#     'host': '127.0.0.1',
#     'port': '5432',
#     'database': 'postgres'
# }


# def fetch_data_to_dataframe():
#     try:
#         # Establish the connection
#         connection = psycopg2.connect(**connection_params)
#
#         # Define the SQL query to fetch data
#         sql_query = "SELECT * FROM mobile"
#
#         # Use pandas to read the SQL query into a DataFrame
#         df = pd.read_sql_query(sql_query, connection)
#
#         return df
#
#     except (Exception, psycopg2.Error) as error:
#         st.error("Error while fetching data from PostgreSQL: {}".format(error))
#
#     finally:
#         # Closing the database connection
#         if connection:
#             connection.close()


# Streamlit application
st.title("Mobile Data Visualization from PostgreSQL")

# Fetch data
# mobile_df = fetch_data_to_dataframe()
mobile_df = pd.read_csv("mobile_df.csv")
# Display data in a table
if mobile_df is not None:
    st.write("### Mobile Data")
    st.dataframe(mobile_df)

    # Sidebar for settings
    st.sidebar.header("Visualization Settings")

    # Select column for visualization
    column_options = mobile_df.columns.tolist()
    selected_column = st.sidebar.selectbox("Select a column to visualize:",
                                           column_options)

    # Select chart type
    chart_type = st.sidebar.radio("Select chart type:",
                                  ("Line Chart", "Bar Chart", "Histogram"))

    # Visualization button
    if st.sidebar.button("Show Visualization"):
        plt.figure(figsize=(10, 5))

        if chart_type == "Line Chart":
            plt.plot(mobile_df[selected_column])
            plt.title(f"Line Chart of {selected_column}")
            plt.xlabel("Index")
            plt.ylabel(selected_column)

        elif chart_type == "Bar Chart":
            mobile_df[selected_column].value_counts().plot(kind='bar')
            plt.title(f"Bar Chart of {selected_column}")
            plt.xlabel(selected_column)
            plt.ylabel("Count")

        elif chart_type == "Histogram":
            plt.hist(mobile_df[selected_column], bins=10, edgecolor='black')
            plt.title(f"Histogram of {selected_column}")
            plt.xlabel(selected_column)
            plt.ylabel("Frequency")

        st.pyplot(plt)
else:
    st.write("No data available.")
