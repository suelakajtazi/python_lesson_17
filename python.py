import streamlit as st 

col1,col2,col3,col4,col5 =st.columns (5,gap="small",vertical_alignment="center")

with col1 :
    st.header("culumn 1")
    st.write("this is column")

with col2 :
    st.header("culumn 2")
    st.write("this is column")

with col3 :
    st.header("culumn 3")
    st.write("this is column")

with col4 :
    st.header("culumn 4")
    st.write("this is column")

with col5 :
    st.header("culumn 5")
    st.write("this is column")

with st.container():
    st.header("hiiiiiiiiiiii")
    st.write("aeiofhwwasdmk efiohfuiewfcds")
    st.write("aeiofhwwasdmk efiohfuiewfcds")
    st.write("aeiofhwwasdmk efiohfuiewfcds")
    st.write("aeiofhwwasdmk efiohfuiewfcds")

st.write("aeiofhwwasdmk efiohfuiewfcds")