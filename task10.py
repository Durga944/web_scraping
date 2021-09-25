from task5 import*
from pprint import pprint

def analyse_language_and_directors(movie_list):
    directors_dic={}
    for movie_index in movie_list: 
        for director in movie_index["Director"]:
            directors_dic[director]={}
        # print(director)

    for index in range(len(movie_list)):
        for dir in directors_dic:
            if dir in  movie_list[index]['Director'] :
                for language  in movie_list[index]['Language']:
                     directors_dic[dir][language]=0
   


    for index in range(len(movie_list)):
        for dir in directors_dic:
            if dir in  movie_list[index]['Director'] :
                for language  in movie_list[index]['Language']:
                     directors_dic[dir][language]+=1
                  
    print(directors_dic)                

    with open("task10.json","w")as data:
        json.dump(directors_dic,data,indent=4)

    pprint(directors_dic)
analyse_language_and_directors(movie_data)