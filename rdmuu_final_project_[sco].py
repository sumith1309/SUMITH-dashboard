import streamlit as st
import os
from PIL import Image

st.set_page_config(page_title='Supply Chain Optimization Dashboard', layout='wide')

# Check if images exist and load them
state_values_img_path = 'state_values.png'
historical_performance_img_path = 'historical_performance.png'

if os.path.exists(state_values_img_path):
    state_img = Image.open(state_values_img_path)
else:
    state_img = None

if os.path.exists(historical_performance_img_path):
    hist_img = Image.open(historical_performance_img_path)
else:
    hist_img = None

# Title of the dashboard
st.title('Supply Chain Optimization Dashboard')

# Create sidebar for navigation
st.sidebar.title('Navigation')
app_mode = st.sidebar.selectbox('Choose the view', ['Dashboard', 'Simulation', 'About'])

if app_mode == 'Dashboard':
    st.header('Dashboard Overview')
    st.markdown('''
    This dashboard presents the optimal decision-making framework for our supply chain optimization.
    **Features Include:**
    - Visual representation of state values and performance metrics
    - Dynamic rendering of simulation outputs
    - Intuitive controls for interactive visualization
    ''')

    # Two columns for images
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('State Values')
        if state_img:
            st.image(state_img, use_column_width=True, caption='State Values from MDP Simulation')
        else:
            st.error('State values image not found.')
    with col2:
        st.subheader('Historical Performance')
        if hist_img:
            st.image(hist_img, use_column_width=True, caption='Historical Performance Data')
        else:
            st.error('Historical performance image not found.')

    # Adding innovative interactive element: user can change the theme
    st.markdown('---')
    st.subheader('Customize Visuals')
    theme_option = st.selectbox('Select a color theme for visualizations:', ['Default', 'Dark', 'Light'])
    st.write('Theme selected: ' + theme_option)

    # Display additional interactive element: simulate random decision performance
    st.markdown('### Decision Performance Simulator')
    import numpy as np
    random_perf = np.random.normal(loc=0, scale=1, size=10)
    st.line_chart(random_perf)

elif app_mode == 'Simulation':
    st.header('Real-Time Simulation')
    st.markdown('This section simulates real-time decisions based on supply chain dynamics.')
    # Example simulation: update every 1 second
    import time
    if st.button('Start Simulation'):
        progress_bar = st.progress(0)
        simulation_text = st.empty()
        for i in range(101):
            simulation_text.text('Simulation Progress: ' + str(i) + '%')
            progress_bar.progress(i)
            time.sleep(0.05)  # simulate update delay
        st.success('Simulation Completed!')
    else:
        st.info('Press the button to start the simulation.')

elif app_mode == 'About':
    st.header('About This Dashboard')
    st.markdown('''
    Developed using **Streamlit** for an interactive experience.

    The dashboard integrates advanced optimization techniques using Markov Decision Processes (MDPs), value iteration, POMDPs, and Nash equilibrium concepts to manage supply chain operations effectively.

    **Features:**
    - Responsive layout for easy navigation
    - Interactive visualizations and simulations for real-time decision-making
    - Customization options for more personalized insights

    Created by S.JYOTHI SWAROOP
    ''')

st.markdown('---')
st.caption('S.JYOTHI SWAROOP')

print('Streamlit dashboard code executed successfully.')
