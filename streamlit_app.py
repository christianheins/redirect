import streamlit as st

st.title('Proplist, Property Listings')

url = "https://proplist.streamlit.app"
link_text = "Click here to visit Proplist, Property Listings."

# Create the clickable URL using Markdown
st.markdown(f"[{link_text}]({url})")
