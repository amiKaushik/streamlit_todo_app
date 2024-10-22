#import core pkgs
import streamlit as st
import streamlit.components.v1 as stc

#database
from database_fxn import create_table,add_data,view_all_data

#SECTIONS
from createList import createSection
from readList import readSection
from updateList import updateSection
from deleteList import deleteSection

#EDA pkgs
import pandas as pd

#utils
from datetime import datetime

#######################################
#header
HTML_BANNER = """
    <div style="background-color:#582167;padding:10px;border-radius:20px;">
    <h1 style="color:white;text-align:center;">To-Do List App</h1>
    </div>
    """
stc.html(HTML_BANNER)

#######################################
#main fxn
def main():
    #st.subheader('meow')
    #site-sidebar choice options
    create_table()
    choice = st.sidebar.selectbox("Menu",['Create','Read','Update','Delete','About'])
    
    if choice == 'Create':
        createSection()
        
    elif choice == 'Read':
        readSection()
    elif choice == 'Update':
        updateSection()
        
    elif choice == 'Delete':
        deleteSection()
    else:
        st.markdown("""
        ## Hello It's Kaushik
        + this is my first App
        + have a nice day
        """)


if __name__ == '__main__':
    main()

# Using CSS Flexbox for layout
st.markdown("""
    <style>
        .footer {
            background-color: #f1f1f1;
            padding: 10px;
            text-align: center;
            position: relative;
            width: 100%;
            bottom: 0;
        }
        .content {
            min-height: calc(100vh - 100px); /* Adjust as needed */
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
    </style>
    <div class="content">
        <div></div>
        <div class="footer">
            <p><b>Contact Us</b></p>
            <p>Ping me on GitHub: <a href="https://github.com/amiKaushik" target="_blank">https://github.com/amiKaushik</a></p>
        </div>
    </div>
""", unsafe_allow_html=True)