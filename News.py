import streamlit as st
import requests

# USE THIS SEARCH variables and URL for news from NEWSAPI.ORG
#  Results = "articles"
#  api_key="3920a536eb914ab89c1165387c6df186"
# "https://newsapi.org/v2/everything?" \
#  f"q={NewsAbout}" \
#  f"&sortBy=publishedAt" \
#  f"apiKey="{api_key}" \
#  f"&language=en"

Results = "results"
api_key="pub_366338c2dd6f876fa7fd4f5a9b5b527955265"

NewsKeyWord = st.text_input(help="Search for anything",max_chars=25,key="keyword", label="keyword")
Button = st.button("Search News")

if Button:
    url="https://newsdata.io/api/1/news?" \
         f"&apikey={api_key}" \
         f"&q={NewsKeyWord}" \
         "&language=en"

    response = requests.get(url)
    data=response.json()

    for i in range(0,10,2):
        col1, col2 = st.columns(2)
        article = data[Results][i]
        with col1:
            title=article["title"]
            st.write(f"**{title}**")
            st.write(article["description"][:150])
        article = data[Results][i+1]
        with col2:
            title=article["title"]
            st.write(f"**{title}**")
            st.write(article["description"][:150])