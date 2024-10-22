#import core pkgs
import streamlit as st
import streamlit.components.v1 as stc

#database add data
from database_fxn import add_data

#EDA pkgs
import pandas as pd

#utils
from datetime import datetime



def createSection():
    st.subheader('Add Item')
    col1,col2 = st.columns(2)
    
    #basic layout
    with col1:
        task = st.text_area(label="Task To Do")
    with col2:
        task_status = st.selectbox("Status",['ToDo','Doing','Done'])
        task_due_date = st.date_input(label='Due Date',min_value=datetime.now())

    #CREATE
    if st.checkbox('Confirm') and st.button('Add Task'):
        if task and task_status and task_due_date:
            st.info(f'Added : "{task}" to Task')
            
            add_data(task,task_status,task_due_date)
            
        else:
            st.warning('Fill All The Sections')

    


if __name__ == '__main__':
    main()