from openai import OpenAI
import streamlit as st

f= open('Keys/.openai_api_key.txt')
key = f.read()
client =  OpenAI(api_key=key)


st.snow()
st.title('Welcome to the MCQ Generator 💬 ')
st.subheader('Soon going to be a billion dollar app 💲')


#take the input 
prompt = st.text_input('Enter the Data Science Topic here..')

# If the button is clicked , geneerate the response 
if st.button('Generate')== True:

    st.balloons()

    response = client.chat.completions.create(

        model = 'gpt-3.5-turbo',
        messages= [
            {'role' : 'system' ,'content': '''You re an helpfun AI assistant.
            
            Given an Data Science Topic you always  generate a 3 MCQ type questions along with the answers ''' },

            {'role': 'user', 'content': prompt}
        ]

    )

#Print the response in web page
st.write(response.choices[0].message.content)