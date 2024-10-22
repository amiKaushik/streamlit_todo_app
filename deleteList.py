#import core pkgs
import streamlit as st
import streamlit.components.v1 as stc

#EDA pkgs
import pandas as pd

#utils
from datetime import datetime

#database
from database_fxn import view_all_data,view_unique_tasks,delete_task


#show table
def show_table(title):
    result_all_data2 = view_all_data()
    all_data_df2 = pd.DataFrame(result_all_data2,columns=['Task','Status','Due'])
    
    with st.expander(f'{title}'):
        st.dataframe(all_data_df2,use_container_width=True)


def deleteSection():
    st.subheader('Delete Item')
    show_table(title='Current To-Do List')
    
    list_of_task =[i[0] for i in view_unique_tasks()] 
    # i in view_unique_tasks means we are iterating through our data(to-do list)
    # i[0] is the first data of each to-do task i.e. TASK NAME
    
    
    selected_task = st.selectbox("Task To Edit",list_of_task)

    if st.checkbox('Confirm Delete') and st.warning(f'Do you really want to delete "{selected_task}" ?') and st.button('Delete'):
        
        delete_task(selected_task)
        st.text(f'"{selected_task}" has been deleted')

        #you can show the updated data/table
        show_table(title='Updated To-Do List')
        
if __name__ == '__main__':
    main()