import streamlit as st
import requests

api_key = "sKiHkp4cK3S1QpeTDAs6rNJ7XSyTHOY9xAot8NUP"
url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

response1 = requests.get(url)
data = response1.json()

print(data)

title = data['title']
image_url = data['url']
explanation = data['explanation']

image_filepath = 'img.png'
response2 = requests.get(image_url)
with open('img.png', 'wb') as file:
    file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.text = explanation