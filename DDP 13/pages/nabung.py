import streamlit as st

st.title("Ini Halaman Nabung")

with st.form("nabung"):
    nama = st.text_input("Nama")
    nominal = st.number_input("Masukkan Nominal Nabung")
    submitButton = st.form_submit_button("Simpan")

    if submitButton:
        st.write(nama)
        st.session_state['Nabung'].append({
            "Nama" : nama,
            "Nominal" : nominal,
        })
        st.success("Berhasil Menabung!")