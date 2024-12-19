import streamlit as st

st.write('')

dasboard = st.Page("./pages/dashboard.py", title="Dashboard")
nabung = st.Page("./pages/nabung.py", title="Nabung")

pg = st.navigation({
    "Dashboard": [dasboard],
    "Nabung": [nabung],
})

if "Nabung" not in st.session_state:
    st.session_state['Nabung'] = []

pg.run()