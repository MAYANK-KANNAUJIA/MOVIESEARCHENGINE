import urllib.request as url
import bs4


#@st.cache(suppress_st_warning=True)
def mysearch(movie_name):
    movie_name=movie_name.replace(" ","+")
    path=f"https://www.imdb.com/search/={movie_name}"
    response=url.urlopen(path)
    page=bs4.BeautifulSoup(response,"lxml")
    titles=page.find_all("h1",{"class":"sc-b73cd867-0 eKrKux"})
                         
    ratingList=page.find_all("span",{"class":"sc-7ab21ed2-1 jGRxWM"})
    for i in range(len(ratingList)):
        print(("Title:{}".format(titles[i].text)))
        print(("Rating:{}".format(ratingList[i].text)))
        print("#"*2)
print("MOVIE SEARCH ENGINE.........")
print("Simple movie search engine .......")
m=input("ENETR MIVIE NAME=")
movie_name=m.replace(" ","+")
print("SEARCH IN PROGESS..........................................")
mysearch(movie_name)

#form=st.form(key="search_form")
#movie_name=form.text_input(label="ENTER MOVIE NAME:")
#submit_btn=form.form_submit_button(label="Start searching")
#if submit_btn:
    #st.write("YOU CLICKED ON SUBMIT.......")
    #mysearch(movie_name)
