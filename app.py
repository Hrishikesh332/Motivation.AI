import openai
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from streamlit_chat import message

# def load_image(img):
#     im=Image.open(img)
#     return im
# size=20


page_element="""
<style>
[data-testid="stAppViewContainer"]{
background-image: url("");
background-size: cover;
}
[data-testid="stHeader"]{
background-color: rgba(0,0,0,0);
}
[data-testid="stToolbar"]{
right: 2rem;
background-image: url("");
background-size: cover;
}

[data-testid="stMarkdownContainer"]{

}
[data-testid="stSidebar"]> div:first-child{
background-image: url("");
background-size: cover;
}
</style>

"""
st.markdown(page_element, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;>Motivation.AI 💫</h1>", unsafe_allow_html=True)
st.markdown("---")

with st.sidebar:
    st.title("Motivation.AI 💫")
    st.write('''
    Motivation.AI is your personal guide to success! Based on the vision of Dr. APJ Abdul Kalam, our AI-powered chatbot provides personalized motivation, practical advice, and inspirational stories to help achieve goals 💫
    ''', unsafe_allow_html=False)

openai.api_key = st.secrets["API"]

def generate_response(prompt):


    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",

    messages=[
            {"role": "user", "content": f"Intimate as an APJ Abdul kalam and reply like him to : {prompt}"}
                ]
    )


    message1 = completion.choices[0].message.get("content")
    return message1


    st.title("🤖")


if 'generated' not in st.session_state:
        st.session_state['generated'] = []

if 'past' not in st.session_state:
        st.session_state['past'] = []


def get_text():
        input_text = st.text_input("You: ","Hello, how are you?", key="input")
        return input_text 


user_input = get_text()

if user_input:
        output = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(output)

if st.session_state['generated']:

        for i in range(len(st.session_state['generated'])-1, -1, -1):
            message(st.session_state["generated"][i], key=str(i))
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

            






