import streamlit as st#stream makes the creation of UI application very easily
from few_shot import FewShotPosts
from post_generator import generate_post


length_options=["Short","Medium","Long"]
language_options=["English","Hinglish"]

def main():
    st.title("LinkedIn Post Generator")
    col1,col2,col3=st.columns(3)
    fs=FewShotPosts()#here you create the obj of the class you have imported
    with col1:
        selected_tag=st.selectbox("Title",options=fs.get_tags())

    with col2:
        selected_length=st.selectbox("Length",options=length_options)
    with col3:
        selected_language=st.selectbox("Language",options=language_options)

    if st.button("Generate"):
        post=generate_post(selected_length,selected_language,selected_tag)
        st.write(post)


if __name__=="__main__":
    main()

#now we have to write the most important piece of code
#in main.py we have 3 parameters ans we need to pass these parameters to some functions and to maintain modularity we make another file(post_generator) for funtions
