import streamlit as st
from files.add_drawing import *
from files.data_visual import *
from files.expense_account import *
from files.labour_attendance import *
from files.new_work import *
from files.stock_list import *
from css_ import *
import json

import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(layout="wide")

def main():
    header_hide()
    hide_pages()
    sidebar_colour()
    margin_top()

    st.sidebar.image('images/logo.png', use_column_width=True)
   
    st.sidebar.markdown(f"""
<html>
    <p style="color: white;">Select an option</p>
</html>
""",unsafe_allow_html=True)
    app_options=st.sidebar.selectbox("",["Dashboard","Add Work","Labour Attendance","Add Drawing","Stock List","Expense Account","Labour Advance"],label_visibility="collapsed")
    
    if app_options=="Add Work":
        new_work_fun()
    elif app_options=="Labour Attendance":
        lab_attendance()
    elif app_options=="Add Drawing":
        add_drawinng_fun()
    elif app_options=="Stock List":
        stock_list_fun()
    elif app_options=="Expense Account":
        expence_acc()
    elif app_options=="Labour Advance":
        pass
    elif app_options=="Dashboard":
        dashboard()


def dashboard():
    st.title("Dashboard")
    with st.expander("Work Information",expanded=True):
        col1,col2 = st.columns([45,55])
        with col1:
            with st.container(border=True):
                with open("database/workdata.json",'r') as f:
                    workdata=f.read()
                
                workdata=json.loads(workdata)
                work_dataframe=pd.DataFrame(workdata)
                work_dataframe.insert(0,"Select",False)
                st.data_editor(work_dataframe,use_container_width=True,hide_index=True)
                but1_col,but2_col=st.columns([1,4])
                with but2_col:
                    with st.popover("Open popover",use_container_width=True):
                        st.markdown("Add New Work 🏗️")
                        work_name = st.text_input("Enter Work Name")
                        work_data = st.date_input("Select Date")
                        add_work=st.button("Add New Work",use_container_width=True,type="primary")
                with but1_col:
                    delete_work=st.button("🗑️",use_container_width=True)
        with col2:
            demo_graph()
            with st.container(border=True):
                with open("database/labourdetails.json",'r') as f:
                    labour_details=f.read()
                labour_details=json.loads(labour_details)
    labour_dataframe=pd.DataFrame(labour_details)
    st.data_editor(labour_dataframe,use_container_width=True,hide_index=True)
    if add_work:
        st.switch_page("pages/new_work.py")



    
        



        

def demo_graph():

    work_details = [
        {"Work Name": "Construction of Building A", "Date": "2024-07-30"},
        {"Work Name": "Road Repair Project", "Date": "2024-07-29"},
        {"Work Name": "Bridge Maintenance", "Date": "2024-07-28"},
        {"Work Name": "Park Landscaping", "Date": "2024-07-27"},
        {"Work Name": "Office Renovation", "Date": "2024-07-26"},
        {"Work Name": "School Expansion", "Date": "2024-07-25"}
    ]

    labour_details = [
        {"Labour Name": "John Doe", "Work Name": "Construction of Building A", "Attendance %": 95},
        {"Labour Name": "Jane Smith", "Work Name": "Road Repair Project", "Attendance %": 88},
        {"Labour Name": "Alice Johnson", "Work Name": "Bridge Maintenance", "Attendance %": 92},
        {"Labour Name": "Bob Brown", "Work Name": "Park Landscaping", "Attendance %": 85},
        {"Labour Name": "Charlie Davis", "Work Name": "Office Renovation", "Attendance %": 90},
        {"Labour Name": "Diana White", "Work Name": "School Expansion", "Attendance %": 87}
    ]

    # Convert to DataFrames
    df_work = pd.DataFrame(work_details)
    df_labour = pd.DataFrame(labour_details)

    # Merge DataFrames on 'Work Name'
    df_combined = pd.merge(df_labour, df_work, on="Work Name")

    # Streamlit App
    st.write("Labour Data Visualizations")

    # Plotting
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Histogram
    sns.histplot(df_combined["Attendance %"], kde=True, bins=10, color="skyblue", ax=axes[0, 0])
    axes[0, 0].axvline(df_combined["Attendance %"].mean(), color="black", linestyle="--", linewidth=2, label=f"Mean: {df_combined['Attendance %'].mean():.1f}")
    axes[0, 0].set_title("Histogram of Labour Attendance Percentages")
    axes[0, 0].set_xlabel("Attendance Percentage")
    axes[0, 0].set_ylabel("Frequency")
    axes[0, 0].legend()
    axes[0, 0].grid(True)

    # Bar Chart
    sns.barplot(x="Work Name", y="Attendance %", data=df_combined, palette="viridis", ax=axes[0, 1])
    axes[0, 1].set_title("Bar Chart of Labour Attendance Percentages by Work")
    axes[0, 1].set_xlabel("Work Name")
    axes[0, 1].set_ylabel("Attendance Percentage")
    axes[0, 1].tick_params(axis='x', rotation=45)
    axes[0, 1].grid(True)

    # Scatter Plot
    sns.scatterplot(x="Date", y="Attendance %", hue="Labour Name", data=df_combined, palette="viridis", ax=axes[1, 0])
    axes[1, 0].set_title("Scatter Plot of Attendance % by Date")
    axes[1, 0].set_xlabel("Date")
    axes[1, 0].set_ylabel("Attendance Percentage")
    axes[1, 0].tick_params(axis='x', rotation=45)
    axes[1, 0].grid(True)

    # Box Plot
    sns.boxplot(x="Work Name", y="Attendance %", data=df_combined, palette="Set2", ax=axes[1, 1])
    axes[1, 1].set_title("Box Plot of Labour Attendance Percentages by Work")
    axes[1, 1].set_xlabel("Work Name")
    axes[1, 1].set_ylabel("Attendance Percentage")
    axes[1, 1].tick_params(axis='x', rotation=45)
    axes[1, 1].grid(True)

    plt.tight_layout()
    st.pyplot(fig)

    


if __name__ == "__main__":
    main()