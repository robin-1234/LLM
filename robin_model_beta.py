import streamlit as st
import ollama

def main():
        st.title("Hello this is Robinbot, you can ask some question")


        user_input = st.text_area("Insert your quaeion","")

        
        if st.button("Enter"):
                if user_input:
                        response = ollama.chat(model = 'robin_model_beta',messages=[{'role':'user','content':user_input}])


                        st.text('Response:')
                        st.write(response["message"]['content'])
                else:
                        st.warning('Please ask some questions!')

if __name__ == "__main__":
        main()