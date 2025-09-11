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


st.sidebar.header("Sidebar")
st.sidebar.write("this is sidebar")
st.sidebar.selectbox("Chose",["home","contact us","about us"])
st.sidebar.radio("Chose",["home","contact us","about us"])

with st.form("myform",clear_on_submit=True):
        name = st.text_input("enter ur name")
        surname = st.text_input("surname")
        age = st.slider("age")
        email = st.text_input("email")
        terms = st.checkbox("agree")
        submit_button = st.form_submit_button("submit")

if submit_button:
       st.write([name])
       st.write([surname])
       st.write([age])
       st.write([email])
       
       if terms:
            st.write("u agreed")
       else:
            st.write("u didnt agree")


tab1,tab2,tab3 = st.tabs(["home","about","contact"])

with tab1:
     st.header("tab1")

with tab2:
     with st.form("urform",clear_on_submit=True):
        name = st.text_input("enter ur name")
        surname = st.text_input("surname")
        age = st.slider("age")
        email = st.text_input("email")
        terms = st.checkbox("agree")
        submit_button = st.form_submit_button("submit")

if submit_button:
       st.write([name])
       st.write([surname])
       st.write([age])
       st.write([email])
       
       if terms:
            st.write("u agreed")
       else:
            st.write("u didnt agree")
with tab3:
     st.header("hiiiiiiiiiiiiii")