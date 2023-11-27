import streamlit as st
import joblib

# Load the trained Decision Tree model and scaler
model_data = joblib.load('decision_tree_model.joblib')
best_dtree = model_data['model']
scaler = model_data['scaler']

# Streamlit App
st.title("Hotel Recommendation Expedia")

# Add background image to the entire app
st.markdown(
    '''
    <style>
    .main {
        background: url('https://img.freepik.com/free-vector/soft-yellow-watercolor-simple-texture-background-vector_1055-13125.jpg?w=1480&t=st=1701024711~exp=1701025311~hmac=2464ad0abf81cdc5a4f27bd4f5078a75e58696efd893f2bce3e85cc4c2db5e70');
    }
   </style>
    ''',
    unsafe_allow_html=True
)



# Selected features based on correlation coefficients
selected_features = ['posa_continent', 'user_location_country', 'user_location_region', 'user_location_city', 'orig_destination_distance', 'user_id', 'is_mobile', 'is_package',
'channel', 'srch_adults_cnt', 'srch_children_cnt', 'srch_rm_cnt', 'srch_destination_id', 'srch_destination_type_id', 'is_booking', 'cnt', 'hotel_continent',
'hotel_country', 'hotel_market', 'number_of_days', 'interaction_day', 'check_in_year', 'check_in_month', 'check_in_day']

# Sidebar Input with Single Option
country_options = {'Canada': 50, 'USA': 198}
selected_country = st.selectbox('In which country do you intend to travel?', list(country_options.keys()))

srch_destination_id = country_options[selected_country]

# Sidebar Input
days_in_hotel = st.text_input('What is the intended duration of your stay at the hotel?',  '1')

# Map the selected country to its corresponding value
country = country_options[selected_country]

# Sidebar Input for Check-in Day
st.write("### Check-in Day")

# Use columns to display Month and Day side by side
col1, col2 = st.columns(2)

# Month
with col1:
    month = st.selectbox('Month:', list(range(1, 13)))

# Day
with col2:
    day = st.selectbox('Day:', list(range(1, 32)))

# Space between Check-in Day and Number of Adults
st.write("     ")  # Add an empty line for spacing
st.write("     ")  # Add an empty line for spacing
st.write("     ")  # Add an empty line for spacing

# Set the background color of the slider to blue
st.markdown(
    """
    <style>
        .slider-container .slider-frame {
            background-color: #3498db;  /* Use any desired color code for blue */
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Create a dictionary with the selected features
input_data = {
    'posa_continent':3,
    'user_location_country':205, 
    'user_location_region':330,
    'user_location_city':13971, 
    'orig_destination_distance':257.7114, 
    'user_id':95263, 
    'is_mobile':0, 
    'is_package':0,
    'channel':9,
    'srch_adults_cnt':st.slider('Number of adults', 0, 10, 1), 
    'srch_children_cnt':st.slider('Number of children', 0, 10, 0), 
    'srch_rm_cnt':st.slider('Number of room', 0, 10, 0), 
    'srch_destination_id':26272, 
    'srch_destination_type_id':6, 
    'is_booking':1, 
    'cnt':1, 
    'hotel_continent':2,
    'hotel_country':country, 
    'hotel_market':975, 
    'number_of_days':float(days_in_hotel), 
    'interaction_day':24, 
    'check_in_year':2014,  
    'check_in_month':month,   # 10
    'check_in_day':day  # can change depois 27
}

if st.button('Recommend'):
    # Check if the value of 'srch_adults_cnt' is less than 1
    if input_data['srch_adults_cnt'] < 1:
        st.error('Number of adults must be 1 or more.')
    # Check if the value of 'srch_rm_cnt' is less than 1
    elif input_data['srch_rm_cnt'] < 1:
        st.error('Number of rooms must be 1 or more.')
    else:
        # Create a dictionary with the selected features
        input_data = {key: value for key, value in input_data.items() if key in selected_features}

        # Ensure the input_data has the same number of features as the training data
        user_input_scaled = scaler.transform([list(input_data.values())])

        # Make predictions using the loaded model and scaler
        prediction = best_dtree.predict(user_input_scaled)

        st.write(f'The recommended hotel cluster is: {prediction[0]}')

