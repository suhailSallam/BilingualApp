import streamlit as st
Arabic, English = st.tabs(['العربية','English'])
with Arabic:
    st.header('السلام عليكم، هذا التطبيق باللغة العربية')
with English:
    st.header('Hello, this application is in English Language')
