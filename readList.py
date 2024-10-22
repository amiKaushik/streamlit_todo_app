#import core pkgs
import streamlit as st
import streamlit.components.v1 as stc

#database
#view data
from database_fxn import view_all_data

#EDA pkgs
import pandas as pd

#data viz pkgs
import plotly.express as px


#utils
from datetime import datetime

def readSection():
    st.subheader('View Items')
    #READ
    # dictionary format
    result_all_data = view_all_data()
    
    df_result = pd.DataFrame(result_all_data,columns=['Task','Status','Due Date'])
        
    with st.expander('View All'):
        #data frame table
        st.dataframe(df_result,use_container_width=True)

    with st.expander('Status'):
        #count 'Status' s
        task_status_df = df_result['Status'].value_counts().to_frame()
        task_status_df = task_status_df.reset_index()

        #using plotly  PIE CHART
        task_status_df.columns = ['Index','Status']
        p1 = px.pie(task_status_df,names='Index',values='Status')
        st.plotly_chart(p1,use_container_width=True)

    col1,col2 = st.columns(2)
    with col1:
        with st.expander('See Raw'):
            st.write(result_all_data)

    with col2:
        with st.expander('See Raw Status'):
            st.dataframe(task_status_df)



    


if __name__ == '__main__':
    main()