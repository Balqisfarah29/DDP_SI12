import streamlit as st

st.title("Ini Halaman dashboard")
st.session_state['Nabung']

jumlah = 0
for session in st.session_state['Nabung']:
    jumlah += session['Nominal']

st.write("Total Nominal Menabung Sebesar", jumlah)