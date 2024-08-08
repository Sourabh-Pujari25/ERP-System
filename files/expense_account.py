import streamlit as st
import pandas as pd
from datetime import date


def expence_acc():
    # Initialize session state to store data
    if 'credit' not in st.session_state:
        st.session_state.credit = pd.DataFrame(columns=["Sr.No", "Date", "Description", "Amount"])
    if 'debit' not in st.session_state:
        st.session_state.debit = pd.DataFrame(columns=["Sr.No", "Date", "Description", "Amount"])

    st.title("Expense Account")

    # Sections for Credit and Debit
    st.subheader("Credit")
    with st.form(key='credit_form'):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            sr_no_credit = st.text_input("Sr.No", key="credit_sr_no")
        with col2:
            date_credit = st.date_input("Date", value=date.today(), key="credit_date")
        with col3:
            desc_credit = st.text_input("Description", key="credit_desc")
        with col4:
            amount_credit = st.number_input("Amount", min_value=0.0, step=0.01, key="credit_amount")
        submit_credit = st.form_submit_button(label='Add to Credit')

    if submit_credit:
        new_entry = {
            "Sr.No": sr_no_credit,
            "Date": date_credit,
            "Description": desc_credit,
            "Amount": amount_credit
        }
        st.session_state.credit = st.session_state.credit.append(new_entry, ignore_index=True)
        st.success("Credit entry added successfully!")

    st.dataframe(st.session_state.credit,use_container_width=True,hide_index=True)

    st.subheader("Debit")
    with st.form(key='debit_form'):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            sr_no_debit = st.text_input("Sr.No", key="debit_sr_no")
        with col2:
            date_debit = st.date_input("Date", value=date.today(), key="debit_date")
        with col3:
            desc_debit = st.text_input("Description", key="debit_desc")
        with col4:
            amount_debit = st.number_input("Amount", min_value=0.0, step=0.01, key="debit_amount")
        submit_debit = st.form_submit_button(label='Add to Debit')

    if submit_debit:
        new_entry = {
            "Sr.No": sr_no_debit,
            "Date": date_debit,
            "Description": desc_debit,
            "Amount": amount_debit
        }
        st.session_state.debit = st.session_state.debit.append(new_entry, ignore_index=True)
        st.success("Debit entry added successfully!")

    st.dataframe(st.session_state.debit,use_container_width=True,hide_index=True)

    # Calculate balance
    total_credit = st.session_state.credit['Amount'].sum()
    total_debit = st.session_state.debit['Amount'].sum()
    balance = total_credit - total_debit

    st.subheader("Balance")
    st.write(f"Total Credit: {total_credit:.2f}")
    st.write(f"Total Debit: {total_debit:.2f}")
    st.write(f"Balance: {balance:.2f}")


if __name__=="__main__":
    expence_acc()