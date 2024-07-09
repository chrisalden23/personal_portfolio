import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from variables import variables
from groq import Groq
import os

st.set_page_config(layout = 'wide')

st.write('##')
st.subheader('Hey Guys :wave:')
st.title("My portfolio website")
# Add a text input field for the user to enter their prompt
prompt = st.text_input("""
Hi, I am Alden's personal asistant. Please ask me anything about him with a complete sentence.""", "What is Alden's current occupation?")

# Create a button to trigger the chatbot's response
button = st.button("Get Response")

#initializing chatbot
client = Groq(
    api_key = "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",
)
context = variables.context
context[4]["content"] = prompt
if button:
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages = context,
        temperature=0.93,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    result = "".join([chunk.choices[0].delta.content or "" for chunk in completion])
    # print(result)
    context.append({"role": "assistant", "content": result})
    st.write(result)

with st.container():
    selected = option_menu(
    menu_title = None,
    options = ['About', 'Resume', 'Projects', 'Magic Work',  'Contact'],
    icons = ['person', 'file-earmark-text', 'code-slash', 'suit-spade', 'chat'],   
    orientation = 'horizontal'
    )

if selected == 'About':

    with st.container():
        st.write("sasageyo")
        st.subheader("I am Alden Christian")
elif selected == 'Resume':
    with open(variables.resume_path, 'rb') as pdf_file:
        resume = pdf_file.read()
    st.download_button(
        label = "📄 Download Resume",
        data = resume,
        file_name = 'resume.pdf'
    )
    with st.container():
        st.subheader("Scholarships: ")
        st.write("""
        - CityU Top Scholarship:

         """)
        st.subheader("Work Experience:")
        st.write("""
        - Sigtica Limited:
        
         """)
elif selected == 'Projects':
    image_dimensions = (400, 200)
    with st.container():
        st.header("My Projects")
        st.write("###")
        col1, col2 = st.columns((1,2))
        with col1:
            img_swire = Image.open("media_resources\images\hr_view.png")
            st.image(img_swire)
        with col2:
            st.subheader("Automated CV Screening System")
            st.markdown(" - developed ...")
            st.markdown('[Visit Github Repository](https://github.com/chrisalden23/swire-hackathon)')
            # st.write("Personal website")
        st.write('##')
        col1, col2 = st.columns((1,2))
        with col1:
            img_swire = Image.open("media_resources\images\hr_view.png")
            st.image(img_swire)
        with col2:
            st.subheader("Automated CV Screening System")
            st.markdown(" - developed ...")
            st.markdown('[Visit Github Repository](https://github.com/chrisalden23/swire-hackathon)')
            # st.write("Personal website")

elif selected == 'Contact':
    with st.container():
        st.markdown("## Feel free to reach Alden out!")
        st.subheader("Email:")
        st.write("""
School: ac5698@columbia.edu \n
Work: aldenchristian.business@gmail.com

""")