import random ,time
from pprint import pprint
from task1 import*
import os,json

file=open("task1.json","r")
movie_data=json.load(file)

all_movie_dic = return_value
movie_index = 0
all_movie_url = []
all_movie_name = []

while movie_index<len(all_movie_dic):
    movie_name = all_movie_dic[movie_index]["name"]
    all_movie_name.append(movie_name)
    url = all_movie_dic[movie_index]["url"]
    all_movie_url.append(url)
    movie_index=movie_index+1

choice_movie_name = int(input("Enter any movie index"))
print("Movie:----",all_movie_name[choice_movie_name-1])

def scrap_movie_details(movie_url):
    random_sleep=random.randint(1,3)
    movie_id=""
    for id in movie_url[27:]:
        if "/" not in id:
            movie_id+=id
        else:
            break
    file_name = movie_id +" .json"

    text=None
    if os.path.exists("task8.json"+file_name):
        f = open("task8.json"+file_name)
        text=f.read()
        # pprint(text)
        return(text)
    if text is None:
        time.sleep(random_sleep)
        page=requests.get(movie_url)
        soup=BeautifulSoup(page.text,"html.parser")

        title_div=soup.find("div",class_="title_wrapper").h1.get_text()
        movie_name=""
        for i in title_div:
            if "(" not in i:
                 movie_name=(movie_name+i).strip()
            else:
                break
        
        sub_div=soup.find("div",class_="subtext")
        runtime=sub_div.find('time').get_text().strip()
        # print(runtime) 
        runtime_hourse=int(runtime[0])*60
        movie_runtime=0
        if "min" in runtime:
            runtime_minutes=int(runtime[3:].strip("min"))
            movie_runtime=runtime_hourse+runtime_minutes
        else:
            movie_runtime=runtime_hourse

        gener=sub_div.find_all('a')
        gener.pop()
        movie_gener=[i.get_text() for i in gener]
        summary=soup.find("div",class_="plot_summary")
        
        movie_bio=summary.find('div',class_="summary_text").get_text().strip()
        director=summary.find('div',class_="credit_summary_item")
        director_list=director.find('a').get_text().strip()
        
        movie_directors=""
        for i in director_list:
            movie_directors=movie_directors+i
        # print(movie_directors)

        extra_details=soup.find('div',attrs={"class":"article","id":"titleDetails"})
        list_of_divs=extra_details.find_all('div')
        for div in list_of_divs:
            tag_h4=div.find_all('h4')
            for text in tag_h4:
                if 'Language:' in text:
                    tag_anchor=div.find_all('a')
                    movie_language=[language.get_text() for language in tag_anchor]
                elif 'Country:'in text:
                    tag_anchor=div.find_all('a')
                    movie_country="".join([country.get_text() for country in tag_anchor])
        
        movie_poster_link=soup.find('div',class_="poster").a.get_text().strip()
        movie_poster="https://www.imdb.com" +movie_poster_link

        movie_details_dic={"movie_name":'',"director":'',"runtime":'',"gener":'',"language":'',"country":'',"poster_img_url":''}

        movie_details_dic["movie_name"]=movie_name
        movie_details_dic["director"]=movie_directors
        movie_details_dic["runtime"]=movie_runtime
        movie_details_dic["bio"]=movie_bio
        movie_details_dic["gener"]=movie_gener
        movie_details_dic["language"]=movie_language
        movie_details_dic["country"]=movie_country
        movie_details_dic["poster_img_url"]=movie_poster

        file=open("task9"+file_name,"w")
        var=json.dumps(movie_details_dic,indent=4)
        file.write(var)
        file.close()
        # pprint(file)

        return movie_details_dic
    


def get_movie_list_details(movie_list):
    list=[]
    for i in movie_list:
        detail=scrap_movie_details(i["url"])
        list.append(detail)
    json_data=open("task9.json","w")
    convert=json_data.dumps(list,indent=4)
    json_data.write(convert)
    json_data.close()
    return list

movie=get_movie_list_details(movie_data)