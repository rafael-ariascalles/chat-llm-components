import streamlit as st


def main():
    # Set Streamlit app title and header
    st.title('Chat with your PDF')
    st.write('Upload your PDF files and ask questions about them. Already uploaded your files? Skip to the chat below.')


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        st.write(f"Something went wrong. Please try again. {str(e)}")
