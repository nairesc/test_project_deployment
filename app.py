import streamlit as st

st.header("Testing deployment")

selector = st.selectbox("Select what do you want to see",("Ballons", "Message"))

if selector == "Ballons":
    st.balloons()
if selector == "Message":
    st.error("We're just testing")


st.header('Something cool', divider='rainbow')
st.header('_Streamlit_ is :blue[cool] :sunglasses:')
