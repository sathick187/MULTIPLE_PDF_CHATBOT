import streamlit as st

def main():
    st.set_page_config(page_title="Chat with multiple PDF",page_icon=":books:")
    st.header("chat with multiple PDF :books:")

    st.text_input("Ask a question about your documents")

    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upload your PDF here and click on the 'Process'")
        st.button('process')

if __name__ == "__main__":
    main()