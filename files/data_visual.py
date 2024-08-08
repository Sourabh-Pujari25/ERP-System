import streamlit as st
import pandas as pd
import io
from datetime import date
import base64
from fpdf import FPDF


def data_vis():
    # Sample data for projects
    projects = ["Project A", "Project B", "Project C"]

    # Sample data for project work (you would replace this with your actual data)
    data = {
        "Project A": pd.DataFrame({
            "Date": [date.today()],
            "Name of Work": ["Excavation"],
            "Excavation Number": [1],
            "Excavation Length": [10],
            "Excavation Width": [5],
            "Excavation Depth": [3],
            "Excavation Total": [150],
            "JCB Bucket": [1],
            "JCB Breaker": [0],
            "Vardhaman Material": [True],
            "MMC Material": [False],
            "Dewatering": [True],
            "Notes": ["N/A"],
            "Site Photos": ["site_photo_1.jpg"],
            "Labour": ["Labour 1"],
            "Drawing Photos": ["drawing_photo_1.jpg"],
            "User Name": ["User 1"]
        }),
        "Project B": pd.DataFrame({
            "Date": [date.today()],
            "Name of Work": ["Foundation"],
            "Excavation Number": [2],
            "Excavation Length": [12],
            "Excavation Width": [6],
            "Excavation Depth": [4],
            "Excavation Total": [288],
            "JCB Bucket": [1],
            "JCB Breaker": [1],
            "Vardhaman Material": [True],
            "MMC Material": [True],
            "Dewatering": [False],
            "Notes": ["N/A"],
            "Site Photos": ["site_photo_2.jpg"],
            "Labour": ["Labour 2"],
            "Drawing Photos": ["drawing_photo_2.jpg"],
            "User Name": ["User 2"]
        }),
        "Project C": pd.DataFrame({
            "Date": [date.today()],
            "Name of Work": ["Construction"],
            "Excavation Number": [3],
            "Excavation Length": [15],
            "Excavation Width": [7],
            "Excavation Depth": [5],
            "Excavation Total": [525],
            "JCB Bucket": [2],
            "JCB Breaker": [1],
            "Vardhaman Material": [False],
            "MMC Material": [True],
            "Dewatering": [True],
            "Notes": ["N/A"],
            "Site Photos": ["site_photo_3.jpg"],
            "Labour": ["Labour 3"],
            "Drawing Photos": ["drawing_photo_3.jpg"],
            "User Name": ["User 3"]
        })
    }

    # Function to convert DataFrame to Excel
    def to_excel(df):
        output = io.BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df.to_excel(writer, index=False, sheet_name='Sheet1')
        #writer.save()
        processed_data = output.getvalue()
        return processed_data

    # Function to convert DataFrame to PDF
    def to_pdf(df):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 12)
        
        for i, row in df.iterrows():
            for j, value in enumerate(row):
                pdf.cell(200, 10, txt = f"{df.columns[j]}: {value}", ln = True)
            pdf.cell(200, 10, txt = "", ln = True)  # add empty line
        
        return pdf.output(dest='S').encode('latin1')

    # Function to get download link for file
    def get_download_link(file_data, file_name, file_type):
        b64 = base64.b64encode(file_data).decode()
        href = f'<a href="data:file/{file_type};base64,{b64}" download="{file_name}">Download {file_type.upper()}</a>'
        return href

    # Function to download all photos
    def download_photos(project_name, df):
        zip_file = io.BytesIO()
        
        zip_file.seek(0)
        b64 = base64.b64encode(zip_file.read()).decode()
        href = f'<a href="data:application/zip;base64,{b64}" download="{project_name}_photos.zip">Download Photos</a>'
        return href

    # Streamlit UI
    st.title("Data Visualization")

    # Dropdown to select project name
    project_name = st.selectbox("Select Project Name", projects)

    if project_name:
        st.subheader(f"Data for {project_name}")
        df = data[project_name]
        st.dataframe(df,use_container_width=True,hide_index=True)
        
        # Download buttons
        excel_data = to_excel(df)
        st.markdown(get_download_link(excel_data, f"{project_name}_data.xlsx", "xlsx"), unsafe_allow_html=True)
        
        pdf_data = to_pdf(df)
        st.markdown(get_download_link(pdf_data, f"{project_name}_data.pdf", "pdf"), unsafe_allow_html=True)
        
        # Download photos
        st.markdown(download_photos(project_name, df), unsafe_allow_html=True)


if __name__=="__main__":
    data_vis()