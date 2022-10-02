import urllib.request as url
import bs4
import streamlit as st

@st.cache(suppress_st_warning=True)
def mysearch(movie_name):
    movie_name=movie_name.replace(" ","+")
    path=f"https://www.imdb.com/search/={movie_name}"
    response=url.urlopenen(path)
    page=bs4.BeautifulSoup(response,"lxml")
    titles=page.find_all("h1",{"class":"sc-b73cd867-0 eKrKux"})
                         
    ratingList=page.find_all("span",{"class":"sc-7ab21ed2-1 jGRxWM"})
    for i in range(len(ratingList)):
        st.write("Title:{}".format(titles[i].text))
        st.write("Rating:{}".format(ratingList[i].text))
        st.write("#"*20)
st.title("MOVIE SEARCH ENGINE.........")
st.write("Simple movie search engine .......")
form=st.form(key="search_form")
movie_name=form.text_input(label="ENTER MOVIE NAME:")
submit_btn=form.form_submit_button(label="Start searching")
if submit_btn:
    st.write("YOU CLICKED ON SUBMIT.......")
    mysearch(movie_name)
