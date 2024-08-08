import streamlit as st
from app_utils import *
# page_congig()

def new_work_fun():
    
    st.title("Add New Work")
    
    # Project Details
    st.header("Project Details")
    work_name=st.text_input("Add Project Name")
    work_date=st.date_input("Select Project Date")
    
    st.header("Materials")
    vard_material=st.selectbox("Vardhaman Material",options=["Option 1","Option 2","Option 3"]) # QTY with this
    vard_material_qty = st.number_input("Select Quantity",min_value=1)
    mcc_material=st.selectbox("Vardhaman Material",key="mcc",options=["Option 1","Option 2","Option 3"]) # QTY with this
    mcc_material_qty = st.number_input("Select Quantity",key="mcc_qty",min_value=1)
    
    # Excavaition
    st.header("Excavation")

    excavation_len=st.number_input("Length",min_value=0.1,placeholder="m",key="exc_len")
    excavation_width=st.number_input("Width",min_value=0.1,placeholder="m",key="exc_width")
    excavation_depth=st.number_input("Depth",min_value=0.94,placeholder="m",key="exc_depth")
    excavation_material=st.selectbox("Excavation Material",key="excavation_material",options=["Option 1","Option 2","Option 3"]) 

    #JCB
    st.header("JCB")


    jcb_bucket_start_time=st.time_input("Start Time",value="now")
    jcb_start_photo = st.file_uploader("Upload Start Time Photo",accept_multiple_files=True)
    jcb_bucket_end_time=st.time_input("End Time",value="now")
    jcb_end_photo = st.file_uploader("Upload End Time Photo",accept_multiple_files=True)

    #Dewartering
    st.header("Dewatering")

    dewatering_inp = st.number_input("Select Quantity",key="dewatering_inp",min_value=1)

    st.header("Additional Details")
    site_pic = st.file_uploader("Upload Site Photos",accept_multiple_files=True)
    drawing_pic = st.file_uploader("Upload Drawing Documents",accept_multiple_files=True)
    select_labours=st.multiselect("Select labours",options=["Option 1","Option 2","Option 3"])

    #notes
    notes = st.text_area("Add Additional Notes",height=200)

    submit_works=st.button("Save & Submit")




if __name__=="__main__":
    new_work_fun()