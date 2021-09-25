from task5 import *
# from pprint import pprint

def analyse_movies_launguage(movies_list):
    language_dict={}
    index1=0
    while index1<len(movies_list):
        index2=0
        count=0
        while index2<len(movies_list):
            if movies_list[index1]["language"]==movies_list[index2]["language"]:
                count+=1
                language=str(movies_list[index1]["language"])[2:-2]
                language_dict[language]=count
            index2=index2+1
        index1=index1+1
    with open("task6.json","w+") as language_data:
        json.dump(language_dict,language_data,indent=4)
    # pprint(language_dict)
analyse_movies_launguage(movie_data)





    