import streamlit as st
import pandas as pd
import os
from os.path import isfile, join

base_path = './data'
file_ls = [f for f in os.listdir(base_path) if isfile(join(base_path, f))]
file_no_ext = [os.path.splitext(f)[0] for f in file_ls]

# TODO: Remove logo background
logo = st.sidebar.image(image='./assets/Mathnasium_Logo.jpg')


student = st.sidebar.selectbox(label='Student',
                               options=file_no_ext,
                               key='student')

new_test = st.sidebar.button(label='Enter a new assessment result',
                             key='new_test')

header = st.header(f'{st.session_state.get("student")}')

if st.session_state.get('new_test') or st.session_state.get('back') is False:
    grade = st.number_input(label='Grade',
                            min_value=0,
                            max_value=12,
                            step=1,
                            key='grade')

    test_number = st.number_input(label='Checkup Number',
                                  min_value=0,
                                  max_value=12,
                                  step=1,
                                  key='test_number')

    test_score = st.number_input(label='Score (%)',
                                 min_value=0,
                                 max_value=100,
                                 step=1,
                                 key='test_score')
    leftcol, rightcol = st.columns([9, 1])

    with leftcol:
        st.button(label='Back',
                  key='back')

    with rightcol:
        st.button(label='Save',
                  key='save')

if st.session_state.get('back') is True or st.session_state.get('back') is None:
    student_options = st.selectbox(label=' ',
                                   options=('Test Results', 'Student Profile'),
                                   key='student_options')

    if st.session_state.get('student_options') == 'Test Results':
        df = pd.read_csv(f'./data/{student}.csv')
        past_results = st.write(df)
    elif st.session_state.get('student_options') == 'Student Profile':
        st.write('not done yet')
