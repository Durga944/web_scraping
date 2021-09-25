# from Task5 import *

# director_dict={}
# def analys_director_and_language(movie_list):
#     for movie in movie_list:
#         for director in movie["Director"]:
#             director_dict[director]={}

#     for count in range(0,len(movie_list)):
#         for director in director_dict:
#             if director in movie_list[count]["Director"]:
#                 for language in movie_list[count]["Language"]:
#                     director_dict[director][language]=0
    
#     for count in range(0,len(movie_list)):
#         for director in director_dict:
#             if director in movie_list[count]["Director"]:
#                 for language in movie_list[count]["Language"]:
#                     director_dict[director][language]+=1        

#     with open("Task10.json","w+") as json_data:
#         json.dump(director_dict,json_data,indent=4)  

#     pprint(director_dict)

# analys_director_and_language(movie_data)

# #Task 10

# #2nd way
# for name in movie_list:
#         count_language=0
#         movie_language={}
#         for info in movie_list:
    #         if name["Director"]==info["Director"] and name["Language"]==info["Language"]:
    #             director_name=str(name["Director"])[2:-2]
    #             language=str(name["Language"])[2:-2]
    #             count_language+=1
    #             movie_language[language]=count_language
    #     movie_dict[director_name]=movie_language
    # pprint(movie_dict)
