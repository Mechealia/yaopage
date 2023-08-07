import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Qiyao Certificates",
    page_icon="📈",
)

with st.container():
    left, right = st.columns((2, 3), gap='large')
    with right:
        st.title("PROFESSIONAL SCRUM MASTER I")
        image = Image.open('cer1.png')
        st.image(image, width=300)

    with left:
        st.title("SIX SIGMA")
        image = Image.open('cer2.png')
        st.image(image, width=300)