import os
import streamlit as st
from PIL import Image
from lyzr import FormulaGen
#from utils import utils  # Assuming utils.py contains the function save_uploaded_file

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = st.secrets["apikey"]

# Create directory if it doesn't exist
data = "data"
os.makedirs(data, exist_ok=True)

# Setup Streamlit page config
st.set_page_config(
    page_title="Lyzr",
    layout="centered",
    initial_sidebar_state="auto",
    page_icon="./logo/lyzr-logo-cut.png"
)

# Load and display the logo
image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("Regex Generator💡")
st.markdown("### Built using Lyzr SDK🚀")
st.markdown(
"Generate regular expressions effortlessly with Lyzr SDK's Regex Generator, simplifying complex pattern queries into actionable insights")

# Custom function to style the app
def style_app():
    st.markdown("""
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    </style>
    """, unsafe_allow_html=True)

# Initialize FormulaGen
generate = FormulaGen()

# Define the Streamlit app
def main():

    # Input field for user to enter the pattern
    pattern_input = st.text_input("Enter your pattern/query :")

    if st.button("Generate Regular Expression"):
        # Generate regular expression using FormulaGen
        result = generate.regular_expression(pattern_input)

        # Display the result
        st.write("Generated Regular Expression:")
        st.write(result)

# Run the app
if __name__ == "__main__":
    main()

    with st.expander("ℹ️ - About this App"):
        st.markdown("""
This app harnesses the FormulaGen module to streamline regular expression generation, simplifying intricate pattern queries into intuitive prompts for seamless data analysis. For any inquiries or issues, please contact Lyzr.
    
        """)
        st.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width = True)
        st.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width = True)
        st.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width = True)
        st.link_button("Slack", url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw', use_container_width = True)
