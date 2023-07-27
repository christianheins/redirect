import streamlit as st

st.title('Proplist, Property Listings')
st.subheader('This URL is an old one')

url = "https://proplist.streamlit.app"
link_text = "Click here to visit Proplist, Property Listings. under proplist.streamlit.app"

# Create the clickable URL using Markdown
st.markdown(f"[{link_text}]({url})")
