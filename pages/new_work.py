import streamlit as st
from app_utils import *
import pandas as pd
import datetime
# page_congig()

st.set_page_config(layout="wide")

def new_work_fun():
    if "stage" not in st.session_state:
        st.session_state.stage = "material_"
    
    st.session_state.stage= st.sidebar.radio("Select a step",["Material Details","Excavation Details","Additional Details"])
    tab1, tab2 = st.tabs(["Table", "App"])
    with tab1:
        path = "database/work/material_details.txt"
        path_1="database/work/Excavation_details.txt"
        data_dict = read_and_parse_file(path)
        data_dict2 = read_and_parse_file(path_1)
        st.subheader("Material Details")
        st.data_editor(pd.DataFrame(data_dict),use_container_width=True,hide_index=True)
        st.subheader("Excavation and JCB Details")
        st.data_editor(pd.DataFrame(data_dict2),use_container_width=True,key="11",hide_index=True)
   
    with tab2:

        if st.session_state.stage == "Material Details":
            material_details()
        elif st.session_state.stage == "Excavation Details":
            excavation()
        elif st.session_state.stage == "Additional Details":
            additional()

def material_details():
    id=get_work_id()
    with st.container(border=True):
        st.subheader("Step 1: Add Material Details")
        col1,col2=st.columns([4,1])
    
        with col1:
            ard_material=st.selectbox("Vardhaman Material",options=["Option 1","Option 2","Option 3"]) # QTY with this
            mcc_material=st.selectbox("MCC Material",key="mcc",options=["Option 1","Option 2","Option 3"]) # QTY with this
        with col2:
            vard_material_qty = st.number_input("Select Quantity",min_value=1)
            mcc_material_qty = st.number_input("Select Quantity",key="mcc_qty",min_value=1)
        col_1,col_2,col_3=st.columns([1,1,1])
        # with col_2:
        #     save_prog=st.button("",use_container_width=True)
        with col_3:
            excav_prog=st.button("Save and Next",use_container_width=True,type="primary")
            if excav_prog:
                material_details_var=str({"work_id":id+1,"vardhaman_material": ard_material,"mcc_material":mcc_material,"mcc_material_qty":mcc_material_qty})+','
                with open(f"database/work/material_details.txt",'a') as f:
                    f.write(material_details_var)
                


def excavation():
    st.session_state.stage = "excavation_"
    # with st.container(border=True):
    st.subheader("Step 2: Add Excavation and JCB Details ")
    with st.container(border=True):
        col1,col2=st.columns([1,2])
    
        with col1:
            excavation_material=st.selectbox("Excavation Material",key="excavation_material",options=["Option 1","Option 2","Option 3"]) 
            excavation_len=st.number_input("Length",min_value=0.1,placeholder="m",key="exc_len")
            excavation_width=st.number_input("Width",min_value=0.1,placeholder="m",key="exc_width")
            excavation_depth=st.number_input("Depth",min_value=0.94,placeholder="m",key="exc_depth")
            with st.container(border=True):
                st.subheader("Dewatering")
                dewatering_inp = st.number_input("Select Quantity",key="dewatering_inp",min_value=1)
            
            
    # QTY with this
        with col2:
            with st.container(border=True):
                jcb_bucket_start_time=st.time_input("Start Time",value="now")
                jcb_start_photo = st.file_uploader("Upload Start Time Photo",accept_multiple_files=True)
                jcb_bucket_end_time=st.time_input("End Time",value="now")
                jcb_end_photo = st.file_uploader("Upload End Time Photo",accept_multiple_files=True)
            space_col,pre_col,next_col=st.columns([1,1,1])
            with pre_col:
                back_prog=st.button("Previous",use_container_width=True)
            with next_col:
                additional_prog=st.button("Save and next",use_container_width=True,type="primary",key="jhsvdj")
            if additional_prog:
                excavation_details_var=str({"excavation_material": excavation_material,"excavation_len":excavation_len,"excavation_width":excavation_width,"excavation_depth":excavation_depth,"dewatering_inp":dewatering_inp,"jcb_bucket_start_time":jcb_bucket_start_time,"jcb_bucket_end_time":jcb_bucket_end_time})+','
                with open(f"database/work/Excavation_details.txt",'a') as f:
                    f.write(excavation_details_var)


            
            
def additional():
    st.header("Additional Details")
    site_pic = st.file_uploader("Upload Site Photos",accept_multiple_files=True)
    drawing_pic = st.file_uploader("Upload Drawing Documents",accept_multiple_files=True)
    select_labours=st.multiselect("Select labours",options=["Option 1","Option 2","Option 3"])

    #notes
    notes = st.text_area("Add Additional Notes",height=200)

    submit_works=st.button("Save & Submit")

def read_and_parse_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    data_dict = eval(content)
    return data_dict

def get_work_id():
    file_path = 'database/work/material_details.txt'
    with open(file_path, 'r') as file:
        content = file.read()
        data_list = eval(f"[{content}]")
        last_element = data_list[-1]
        last_work_id = last_element['work_id']
    return last_work_id
if __name__=="__main__":
    new_work_fun()