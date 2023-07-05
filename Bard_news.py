import streamlit as st
import re
from bardapi import Bard
import os
import requests
import config

st.title("Ask me News !!")

os.environ['_BARD_API_KEY'] = config.Bard_api
session = requests.Session()
session.headers = {
    "Host": "bard.google.com",
    "X-Same-Domain": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Origin": "https://bard.google.com",
    "Referer": "https://bard.google.com/",
}
session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY"))

user_query = st.text_input("Enter the news you want ")

ans = Bard().get_answer(user_query)['content']

# Remove unnecessary characters and formatting
clean_text = re.sub(r'\*\*|\n+', '', ans)

# Convert bullet points to newlines
clean_text = re.sub(r'\n\* ', '\n- ', clean_text)

news_updates = clean_text.split('*')

for index, news_update in enumerate(news_updates[1:], start=1):
    st.write(f'{index}. {news_update}\n')
