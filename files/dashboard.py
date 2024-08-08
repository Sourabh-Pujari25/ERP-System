import streamlit as st
from files.add_drawing import *
from files.data_visual import *
from files.expense_account import *
from files.labour_attendance import *
from files.new_work import *
from files.stock_list import *
from streamlit_option_menu import option_menu




# st.set_page_config(page_title='Oliots ERP', page_icon='images/logo.ico',layout="wide")

def main():
    st.sidebar.image('images/logo.png', use_column_width=True)
    

    #st pages hide
    # st.markdown(f"""<style>[class="st-emotion-cache-10rjk4g eczjsme14"]{{display:none;}}</style>""",unsafe_allow_html=True)
    # st.markdown(f"""<style>[class="st-emotion-cache-1s3y5qe eczjsme13"]{{display:none;}}</style>""",unsafe_allow_html=True)
    # st.markdown(f"""<style>[class="st-emotion-cache-6qob1r eczjsme8"]{{background: linear-gradient(to bottom,#078a97, #053c47);}}</style>""",unsafe_allow_html=True)
    # st.markdown(f"""<style>[class="menu"]{{background: linear-gradient(to bottom,#078a97, #053c47);}}</style>""",unsafe_allow_html=True)
    
    

    #st.sidebar.title("Dashboard")
    # Dictionary of pages
    pages = {
        "Add Work": new_work_fun,
        "Labour Attendance": lab_attendance,
        "Add Drawing": add_drawinng_fun,
        "Stocklist": stock_list_fun,
        "Expense Account": expence_acc,
        "Data Visualization": data_vis
    }
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",menu_icon="plugin",
            options = list(pages.keys()),
            icons = ["","person-fill-gear","robot","database-check","rocket-takeoff","receipt","bi-x-diamond-fill"],styles={"container": {"border":" 2px inset rgba(0,204,241,0.55)"}},key="trial",


        )

        

   



        
    # Sideb
    
    # Call the selected page function
    page = pages[selected]
    page()

if __name__ == "__main__":
    main()