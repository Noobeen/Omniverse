import base64
import streamlit as st
from streamlit_option_menu import option_menu

#function to read python file 
def run_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        file_content = file.read()
    exec(file_content, globals())

selected = option_menu(
    menu_title=None,
    options=["Herschel", "Play with Data", "AboutUs"],
    icons=["robot", "bar-chart-line-fill", "people-fill"],
    default_index=0,
    orientation= "horizontal",
    styles={
                "container": {},
                "icon": {"color": "white"},
                "nav-link": {
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "#00004d",},
            },
        )

# function to add image
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("backkk.jpg")

# adding background picture
page_bg_image = f"""
<style>
[data-testid="stAppViewContainer"]{{
background-image: url("data:image/png;base64,{img}");
background-size: cover;
}}

[data-testid="stHeader"]{{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
color:white;
}}

[id="chatbot"]{{
    color:white;
}}

</style>
"""

#Nav Bar
st.markdown(page_bg_image, unsafe_allow_html=True)
if selected == "Herschel":
    run_file("herschel.py")
if selected == "Play with Data":
    run_file("play_with_data.py")
if selected == "AboutUs":
    run_file("about.py")