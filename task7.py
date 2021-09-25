from task5 import*

def analyse_movies_directors(movie_list):
    director_dict={}
    index1 =0
    while index1<len(movie_list):
        index2=0
        count=0
        while index2<len(movie_list):
            if movie_list[index1]["director"]==movie_list[index2]["director"]:
                count+=1
                director=str(movie_list[index1]["director"])[2:-2]
                director_dict[director]=count
            index2+=1
        index1+=1
    with open("task7.json","w+") as language_data:
        json.dump(director_dict,language_data,indent=4)
    pprint(director_dict)
analyse_movies_directors(movie_data)
