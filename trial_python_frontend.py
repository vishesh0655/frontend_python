import streamlit as st

# Website Title
st.set_page_config(page_title="Vishesh Saini Portfolio", page_icon="👨‍💻")

# Header Section
st.title("👨‍💻 Vishesh Saini")
st.subheader("B.Tech CSE (AIML) | Python & AI Learner | Web Developer")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About Me", "Projects", "Contact"])

# About Me Section
if page == "About Me":
    st.header("About Me")
    st.write("""
        Hello! I'm Vishesh, a computer science student passionate about AI, ML, and building cool web apps with Python.
        
        - 💻 Learning Python, Data Science & AI
        - 🌐 Exploring frontend development with Python tools
        - 📚 Currently enrolled in IBM's Python for Data Science course
    """)

# Projects Section
elif page == "Projects":
    st.header("Projects")
    st.write("Here are some projects I've worked on:")
    st.markdown("""
    - 🧠 **AI Handwriting Generator**: Built using PyTorch + Streamlit
    - 📊 **Covid-19 Dashboard**: Built using Dash/Plotly
    - 📋 **Resume Builder**: Auto-generates resume from input
    """)

# Contact Section
elif page == "Contact":
    st.header("Contact Me")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Send"):
        st.success("Thanks! I will get back to you soon.")

# Footer
st.markdown("---")
st.markdown("made by vishesh")
