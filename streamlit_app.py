import streamlit as st
from predict import load_model_and_columns, predict_price
import base64

# PAGE CONFIG
st.set_page_config(
    page_title="Bengaluru Home Price Predictor",
    page_icon="🏘️",
    layout="centered",
)

# BACKGROUND IMAGE + CSS
def add_bg(local_image_path):
    with open(local_image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    css = f"""
    <style>
    /* Background image */
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Center container and reduce wide feel */
    .block-container {{
        max-width: 900px;
        margin: auto;
        padding-top: 0.5rem !important;
        padding-bottom: 1.5rem !important;
    }}

    /* Header: smaller bottom gap */
    h1 {{
        margin-bottom: 0.25rem !important;
        padding-bottom: 0 !important;
    }}

    /* Remove the default Streamlit top whitespace immediately after header */
    .element-container, .stMarkdown {{
        margin-top: 0 !important;
    }}

    /* Improved Labels: Bigger, bolder, high contrast */
    label, .stTextInput label, .stNumberInput label {{
       color: #111111 !important;  /* Pure dark gray/black, works on dark & light BG */
       font-weight: 800 !important; 
       font-size: 22px !important;
       text-shadow: 0px 1px 2px rgba(255,255,255,0.85); /* subtle outline for visibility over dark BG */
}}


    /* Make text inside inputs clearly black and full-width */
    input[type="text"], input[type="number"] {{
        color: #000 !important;
        background: rgba(255,255,255,0.92) !important;
        border-radius: 8px !important;
        padding: 10px 12px !important;
        height: 42px !important;
    }}

    /* Ensure placeholders are darker (not washed out) */
    input::placeholder {{
        color: #444 !important;
        opacity: 1 !important;
    }}

    /* Streamlit number-input layout fix: make the input expand and keep +/- as small buttons */
    .stNumberInput > div, .stNumberInput > div > div {{
        display: flex !important;
        align-items: center !important;
    }}

    /* make the numeric input take available space */
    .stNumberInput input[type="number"] {{
        flex: 1 1 auto !important;
        width: 100% !important;
        -webkit-appearance: none;
        margin-right: 8px !important;
    }}

    # /* style the small increment/decrement button group */
    # .stNumberInput button {{
    #     background: #2b2b2b !important;
    #     color: #fff !important;
    #     border: none !important;
    #     border-radius: 6px !important;
    #     padding: 6px 10px !important;
    #     height: 36px !important;
    }}

    /* small spacing between fields in a row */
    .stColumn > div.row-widget.stTextInput, 
    .stColumn > div.row-widget.stNumberInput {{
        margin-bottom: 10px !important;
    }}

    /* Predict button styling */
    div.stButton > button:first-child {{
        background-color: #D9B176 !important;
        color: white !important;
        border-radius: 10px !important;
        height: 46px !important;
        width: 100% !important;
        font-size: 18px !important;
        font-weight: 700 !important;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.12) !important;
    }}

    /* Remove Streamlit footer / badge */
    footer, .viewerBadge_container__1QSob {{
        display: none !important;
    }}

    /* Style for success message box */
    .stAlert {{
        background: rgba(182, 142, 92, 0.92) !important;   /* warm brown with opacity */
        color: #ffffff !important;                         /* white readable text */
        border-left: 6px solid #8B5E34 !important;         /* darker accent */
        border-radius: 10px !important;
        font-size: 20px !important;
        font-weight: 700 !important;
        padding: 14px !important;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.25) !important;
    }}


    /* Small responsive tweak: stack columns on very small screens */
    @media (max-width: 640px) {{
        .stBlock > .element-container .row-widget.stColumns {{
            display:block;
        }}
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# put your image name 
add_bg("img1.jpg")

# LOAD MODEL
model, cols = load_model_and_columns()

# HEADER (snug)
st.markdown(
    """
    <h1 style="
        text-align:center;
        background-color:#B68E5C;
        color:white;
        padding:12px;
        border-radius:10px;
        font-size:34px;
        margin-bottom:0px;
        ">
        Bengaluru Home Price Predictor
    </h1>
    """,
    unsafe_allow_html=True,
)

# FORM BOX (no large gap)
st.markdown('<div class="form-box">', unsafe_allow_html=True)
st.markdown("### Enter Property Details:")

# Use two columns, inputs fill available width now
col1, col2 = st.columns(2, gap="large")

with col1:
    location = st.text_input("Location", "Whitefield")
    sqft = st.number_input("Total Sqft", min_value=200, value=1000, step=50)

with col2:
    bhk = st.number_input("BHK Count", min_value=1, value=2, step=1)
    bath = st.number_input("Bathroom Count", min_value=1, value=2, step=1)

# Predict button and result
st.markdown("")  # small spacer
if st.button("Predict Price"):
    try:
        price = predict_price(model, cols, location, sqft, bath, bhk)
        st.success(f"Estimated Price: **₹ {price:.2f} Lakhs**")
        st.balloons()
    except Exception as e:
        st.error(f"Prediction failed: {e}")

st.markdown('</div>', unsafe_allow_html=True)
