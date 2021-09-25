from pprint import pprint
from task4 import*
import json

def get_movie_list_details():
    ask_user=int(input("Enter The Movie Number:--"))
    url_list=[]
    movie_index=0
    while movie_index<len(return_value[:ask_user]):
        url_list.append(scrap_movie_details(return_value[movie_index]["url"]))
        movie_index=movie_index+1

    with open ("task5.json","w") as movie_data:
        json.dump(url_list,movie_data,indent=4)
        return url_list

movie_data=get_movie_list_details()
pprint(movie_data)




