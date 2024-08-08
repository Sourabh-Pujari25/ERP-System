import streamlit as st
from datetime import date


def add_drawinng_fun():
    # Sample project names
    projects = ["Project A", "Project B", "Project C"]

    # Page 1: Select Project
    if 'project_selected' not in st.session_state:
        st.session_state.project_selected = False

    if not st.session_state.project_selected:
        st.title("Select Project")
        project_name = st.selectbox("Select Project Name", projects)
        if st.button("Next"):
            st.session_state.project_name = project_name
            st.session_state.project_selected = True
            st.experimental_rerun()
    else:
        # Page 2: Fill out the form
        st.title(f"Add Drawing for {st.session_state.project_name}")
        
        with st.form(key='drawing_form'):
            name_of_work = st.text_input("Name of Work")
            work_date = st.date_input("Date", value=date.today())
            drawings = st.file_uploader("Drawing Upload", accept_multiple_files=True)
            
            submit_button = st.form_submit_button(label='Submit')
            
        if submit_button:
            st.success("Form submitted successfully!")
            st.write("Details Submitted:")
            st.write(f"Name of Work: {name_of_work}")
            st.write(f"Date: {work_date}")
            if drawings:
                st.write("Drawings Uploaded:")
                for drawing in drawings:
                    st.write(f"- {drawing.name}")

        if st.button("Back"):
            st.session_state.project_selected = False
            st.experimental_rerun()


if __name__ == "__main__":
    add_drawinng_fun()