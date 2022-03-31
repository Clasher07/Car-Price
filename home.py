import streamlit as st

def app():
	st.header("Car Price Prediction App")
	name=st.text_input("enter Your name")
	st.write("Welcome" + name)
	st.write("""
            This web app allows a user to predict the prices of a car based on their 
            engine size, horse power, dimensions and the drive wheel type parameters.
        	""")