#import core pkgs
import streamlit as st
import streamlit.components.v1 as stc

#EDA pkgs
import pandas as pd

#utils
from datetime import datetime

#database
from database_fxn import view_all_data
from database_fxn import view_unique_tasks,get_task,edit_task_data



##############################################################
#show table
def show_table(title):
    # view_all_data() returns all existing todo work in our DATA BASE
    result_all_data2 = view_all_data()
    all_data_df2 = pd.DataFrame(result_all_data2,columns=['Task','Status','Due'])
    
    with st.expander(f'{title}'):
        st.dataframe(all_data_df2,use_container_width=True)


def updateSection():
    st.subheader('Edit/Update Items')
    show_table(title='Current To-Do List')

    list_of_task =[i[0] for i in view_unique_tasks()] 
    # i in view_unique_tasks means we are iterating through our data(to-do list)
    # i[0] is the first data of each to-do task i.e. TASK NAME
    
    #select task to edit
    selected_task = st.selectbox("Task To Edit",list_of_task)
    
    #call database fxn to get all elements of selected Task
    selected_result = get_task(selected_task)

    # here updated elements will be taken as input
    if selected_result:
        task = selected_result[0][0]
        task_status = selected_result[0][1]
        task_due_date = selected_result[0][2]

        #update layout
        col1,col2 = st.columns(2)

        with col1:
            new_task = st.text_area("Task To Do",task)
        with col2:
            new_task_status = st.selectbox(task_status,['ToDo','Doing','Done'])
            new_task_due_date = st.date_input(task_due_date,min_value=datetime.now())

        if st.checkbox('Confirm Update') and st.button('Update Task'):
            #call database fxn to EDIT data
            edit_task_data(new_task,new_task_status,new_task_due_date,task,task_status,task_due_date)
            
            st.success(f"Sucessfuly Updated: '{task}'")
            #you can show the updated data/table
            show_table(title='Updated To-Do List')


if __name__ == '__main__':
    main()