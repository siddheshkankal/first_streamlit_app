import streamlit
import snowflake.connector
import requests
import pandas as pd
from urllib.error import URLError
streamlit.title('My Parents New Healthy Diner ')

streamlit.header(' Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# setting Fruit column as as index
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# filter the fruits to display
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# new section to display fruitvicy api response


streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  # fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')

  if not fruit_choise:
    streamlit.error("Please select a fruit to get information.")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
    
# except URLError as e:
#   streamlit.error()
  
    #     streamlit.write('The user entered ', fruit_choice)

    # fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
    # fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")
    #     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    # streamlit.text(fruityvice_response.json())
    #     fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    # write your own comment - what does this do?
    #     streamlit.dataframe(fruityvice_normalized)
# except URLError as e:
#   streamlit.error()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)

# my_cur.execute("SELECT * from FRUIT_LOAD_LIST") 
# my_data_row = my_cur.fetchone()
# streamlit.text("Fruit Load List Contains :")
# streamlit.text(my_data_row)

my_cur.execute("SELECT * from FRUIT_LOAD_LIST") 
my_data_row = my_cur.fetchall()
streamlit.header("Fruit Load List Contains :")
streamlit.dataframe(my_data_row)



add_my_fruit = streamlit.text_input('what fruit would you like to add ??','jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)
