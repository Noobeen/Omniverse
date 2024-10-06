import streamlit as st
import base64

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Get base64 images
nabin_img = get_img_as_base64("images/nabin.jpg")
prameya_img = get_img_as_base64("images/prameya.jpg")
kishor_img = get_img_as_base64("images/kishor.png")
navodit_img = get_img_as_base64("images/navodit.jpg")
sudip_img = get_img_as_base64("images/sudip.jpg")

st.markdown(
    """
    <style>
    /* Expand the content width without changing the nav bar or sidebar */
    .block-container {
        padding-left: 0rem;
        padding-right: 0rem;
        width: 100%;
    }
    .about-section {
        padding: 50px;
        text-align: center;
        color: white;
        background-color: rgba(0,0,0,0);
        width: 100%;
    }
    .team-member {
        text-align: center;
        background-color: #1e1e1e;
        padding: 20px;
        border-radius: 8px;
        color: white;
        height: 580px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        width: 100%;
    }
    .team-member img {
        width: 100%;
        border-radius: 8px;
        height: 200px;
        object-fit: cover;
    }
    .team-member h3 {
        font-size: 18px;  /* Reduced font size for the name */
    }
    .team-member p {
        font-size: 14px;  /* Reduced font size for the details */
    }
    .button {
        border: none;
        padding: 8px;
        color: black;
        background-color: white;
        text-align: center;
        cursor: pointer;
        width: 100%;
        text-decoration: none;
    }
    .button:hover {
        background-color: #555;
    }

    [data-testid="stHorizontalBlock"] {
        width: 100% !important; /* Set width to 100% */
        margin: 0; /* Reset margin */
    }

    </style>
    """,
    unsafe_allow_html=True
)

# About Section
st.markdown(
    """
    <div class="about-section">
        <h1 style="text-align: center; color: #fff; text-transform: uppercase; font-size: 50px;">About <span style="color: #00fecb;">Us</span></h1>
        <p style="border-color: tomato;font-family: monospace;">"Solo commitment, embedded movement"</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Welcome message
st.markdown(
    """
    <div style="background-color: rgba(0,0,0,0); padding: 20px;">
        <p style="color:#fff;">Welcome! We’re excited to introduce you to “Herschel,” our friendly chatbot that’s here to answer all your questions about exoplanets and the wonders of the universe. Herschel is your cosmic guide and is ready to share fascinating insights and discoveries with you. 
        But that’s just the start! We also have engaging quizzes that will challenge your knowledge and spark your curiosity about exoplanets. It is a fun way to learn more and see just how much you know about the universe.
        Join us on this exciting journey! Whether you’re a space enthusiast or just starting to explore, there’s so much to discover together. Let’s uncover the mysteries of the universe together!</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Team Section Title
st.markdown(
    """
    <h2 style="text-align:center;color:white;font-size: 30px;">Our Team</h2>
    <hr>
    """,
    unsafe_allow_html=True
)

# Team members information
team_members = [
    {
        "name": "Nabin Oli",
        "degree": "B.S. in Computer Science and Mathematics (Class of 2028)",
        "university": "Caldwell University, NJ",
        "email": "oli.nabin1729@gmail.com",
        "linkedin": "https://www.linkedin.com/in/nabin-oli-4b7132276/",
        "image": nabin_img,
    },
    {
        "name": "Prameya Dhaubadhel",
        "degree": "B.S. in Computer Science (Class of 2028)",
        "university": "Caldwell University, NJ",
        "email": "pdhaubhadel@caldwell.edu",
        "linkedin": "https://www.linkedin.com/in/prameya-dhaubhadel/",
        "image": prameya_img
    },
    {
        "name": "Kishor Baniya",
        "degree": "B.S. in Computer Science and Mathematics (Class of 2028)",
        "university": "Caldwell University, NJ",
        "email": "kishorbaniya15@gmail.com",
        "linkedin": "https://www.linkedin.com/in/kishor-baniya-7164bb213/",
        "image": kishor_img
    },
    {
        "name": "Navodit Kuikel",
        "degree": "B.S. in Computer Science (Class of 2028)",
        "university": "Caldwell University, NJ",
        "email": "nkuikel@caldwell.edu",
        "linkedin": "https://www.linkedin.com/in/navodit-kuikel-9bbb14291/",
        "image": navodit_img
    },
    {
        "name": "Sudip Kumar Thakur",
        "degree": "B.S. in Computer Science (Class of 2028)",
        "university": "Caldwell University, NJ",
        "email": "sthakur3@caldwell.edu",
        "linkedin": "https://www.linkedin.com/in/sudip-kumar-thakur-460599331/",
        "image": sudip_img
    }
]

# Display team members in rows and columns
cols = st.columns(len(team_members))  # Create dynamic columns for each member

for i, member in enumerate(team_members):
    with cols[i]:  # Access each column for each member
        st.markdown(
            f"""
            <div class="team-member">
                <img src="data:image/png;base64,{member['image']}" alt="{member['name']}">
                <div class="container">
                    <h3>{member['name']}</h3>
                    <p class="title">{member['degree']}</p>
                    <p>{member['university']}</p>
                    <p>{member['email']}</p>
                    <p><a class="button" target="_blank" href="{member['linkedin']}">Contact</a></p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("<hr style='width: 100%;'>", unsafe_allow_html=True)
