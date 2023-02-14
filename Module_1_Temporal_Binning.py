# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 16:35:55 2022

@author: Sielvie
"""

import os 
import json
from random import sample
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, CategoriesOptions
import ast
from langdetect import detect

def is_ascii(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True
        
folder = os.listdir( 'D:\\DATASETS\\16_09_2020\\Step_0_preprocessed' ) #FOLDER IN THE DIRECTORY WITH MULTIPLE JSON FILES
def hashtagextraction(dicti1):
##        print(dicti1)
        try:
                hasht=[]
                for i in range(0, len(dicti1['extended_tweet']['entities']['hashtags'])):
                        hashtag=(dicti1['extended_tweet']['entities']['hashtags'][i]['text'].lower())
                        if is_ascii(hashtag)==False:
                            continue
                        else:
                            hasht.append(hashtag)
                return(hasht)       
        except:
                hasht=[]
                for i in range(0, len(dicti1['entities']['hashtags'])):
                        hashtag=(dicti1['entities']['hashtags'][i]['text'].lower())
                        if is_ascii(hashtag)==False:
                            continue
                        else:
                            hasht.append(hashtag)
                return(hasht)

def HashtagVocab(dirs): #return list of  hashtag vocab in one time period 
        print("Inside HashtagVocab Function")
        vocab_of_a_folder=[]
        full_filename = "%s/%s" % ('D:\\DATASETS\\16_09_2020\\Step_0_preprocessed', dirs)   #FIRST TIME INTERVAL (FIRST JSON FILE)
        with open(full_filename,'r', encoding="utf-8") as fi:
                dicti = [json.loads(line) for line in fi]
                
                for insidei in range(0,len(dicti)):
##                    print(insidei)
                    hashtagsi=hashtagextraction(dicti[insidei])
#                    print(hashtagsi, "----hashtagsi")
                    if not hashtagsi:
                        continue
                    else:
##                            
                                 vocab_of_a_folder.extend(hashtagsi)
#        vocab_of_a_folder.append(alldictsi)
#        print(len(vocab_of_a_folder))
#        print((vocab_of_a_folder))
#        print("NEXT")
        return((vocab_of_a_folder))



#print(HashtagVocab(folder[2]))
#print(type(HashtagVocab(folder[3])))
 

authenticator = IAMAuthenticator('viFjPvn82FYhWTGh9sMHHCyl0D7GiDVF7Y89b0wjV3xV')
natural_language_understanding = NaturalLanguageUnderstandingV1(version='2021-02-18',authenticator=authenticator)
natural_language_understanding.set_service_url('https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/0b416a2c-d5c8-46be-ab67-ad41830b1fae')
      
def CategoryList(file):
    print("Inside CategoryList Function")
    category_of_a_folder=[]

    tweets_first_interval = []
    
#        print(len(dirs))
    CD_full_filename = "%s/%s" % ('D:\\DATASETS\\16_09_2020\\Step_0_preprocessed', file)   #FIRST TIME INTERVAL (FIRST JSON FILE)
    with open(CD_full_filename,'r', encoding="utf-8") as fi:
        dict_tweetsi = [json.loads(line) for line in fi]
            
        for insidei in range(0,len(dict_tweetsi)):
            tweeti=dict_tweetsi[insidei]['text']
            tweets_first_interval.append(tweeti)
               
    Sample_Interval1=sample(tweets_first_interval,700) 
    Sample_Interval1=('[{}]'.format(', '.join(Sample_Interval1)))
#    print(Sample_Interval1)
    
    response = natural_language_understanding.analyze(text= Sample_Interval1,features=Features(categories=CategoriesOptions())).get_result()
#    print(json.dumps(response, indent=2))
    category_dict_t1={}
    for r in response['categories']:
            
#            print (text)
            category= r['label']
#                print (word,"keyword")
            score=r['score']
            if score<0.7:
                continue
            else:
                category_dict_t1[category]= score
            
            
#            category_of_a_time_interval.append(category_dict_t1)
    category_of_a_folder.append(category_dict_t1)
#    print(category_dict_t1)
    return(category_dict_t1)        
##        
##
##
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def HashtagDiversity(list1,list2):
#    print("Inside HashtagDiversity Function")
#    print(list1, list2)
#    difference_length=len(list(set(list1) - set(list2)))
#    HD_value= (difference_length/ len(list2))
#    print(HD_value, "--HashtagDiversity")     
    HD_value=OverlapCofficient(list1, list2)
    return(HD_value)     
##    
####
def OverlapCofficient(dict1,dict2):
    
    try:
        dict_intersection= intersection(dict1, dict2)
        oc= (len(set(dict_intersection)))/(min(len(set(dict1)), len(set(dict2))))
        return oc
    except ZeroDivisionError:
        oc = 0.0
        return oc  
    
#import numpy as np

def Combined_KLOC_CD(dict1,dict2):
#    print(dict1, "first dictionary")
#    print(dict2, "second dictionary")
#    P=np.array(list(dict1.values()))
#    Q=np.array(list(dict2.values()))
   
#    dictionary_intersection=(dict1.keys()&dict2.keys()).values()
    
#    print(dictionary_intersection)
#    P=[]
#    Q=[]
    dict_intersection= list(dict1.keys()&dict2.keys())
#    for i in range(0, len(dict_intersection)):
#        p=(dict1[dict_intersection[i]])
#        P.append(p)
#        
#    for j in range(0, len(dict_intersection)):
#        q=(dict2[dict_intersection[j]])
#        Q.append(q)
#    First_DICT=np.array(P)
#    Second_DICT=np.array(Q)
#    divergence = np.sum((First_DICT-Second_DICT)*np.log(First_DICT/Second_DICT))
    def Average(lst):
        return sum(lst) / len(lst)
        
#    print((dict_intersection),"length of intersection")
    oc=  (len(dict_intersection)/min(len(list(dict1.keys())), len(list(dict2.keys()))))
    all_values=[]
    for items in dict_intersection:
#         print((items), "---items")
         first=((dict1[items]))
         second=((dict2[items]))
#         AVG=abs((first+second)/2)
         AVG=min(first, second)
         all_values.append(AVG)
#    print(all_values, "all_values")
    avg2=Average(all_values)
    overlap=oc*avg2
#         print(first, second)
#         
#         if (abs(first-second)<5):
#             print(first, "---", second)
#             average_num=abs((first+second)/2)
#             print(average_num)
#             overlap=oc*(average_num/100)
#             print(overlap, "overlP", oc, "---oc")
#         else:
#             overlap=oc
#        all_values.append(values)
#    print(all_values, "all values")
    
#        print(dict1[items], "dictionary1 values")
#        print((dict2[items]), "dictionary 2 values")
#    combined_value=divergence*oc
#    print(combined_value, "--Combined_KLOC_CD")
#    print(P, "first probability ditribution")
#    print(Q, "second probability ditribution")
#    print(overlap)
    return (overlap)
##
##
##
#folder_name = input('tester_folder')
folder1 =('D:\\DATASETS\\16_09_2020\\Step_1_New_intervals_with_extended_tweet')
def Combine_two_files(file1, file2):
     with open("D:\\DATASETS\\16_09_2020\\Step_0_preprocessed\\"+file1,'r',encoding="utf-8") as f1:
        dict_tweets1 = [json.loads(line) for line in f1]
     with open("D:\\DATASETS\\16_09_2020\\Step_0_preprocessed\\"+file2,'r', encoding="utf-8") as f2:
        dict_tweets2 = [json.loads(line) for line in f2]
     dict_tweets= dict_tweets1+dict_tweets2
     file_name = file1+file2+"combined.json"
     file = os.path.join(folder1, file_name)
     with open(file, 'w', encoding="utf-8") as f:
         for items1 in dict_tweets:
           f.write('%s\n' %items1)
##        
##        
###     first_file=[]
###     second_file=[]
###     full_filename1 = "%s/%s" % ('joined', file1)   #FIRST TIME INTERVAL (FIRST JSON FILE)
###     with open(full_filename1,'r') as f1:
###         dict1 = [json.loads(line) for line in f1]
###         first_file.extend(dict1)
###     full_filename2 = "%s/%s" % ('joined', file2)   #FIRST TIME INTERVAL (FIRST JSON FILE)
###     with open(full_filename2,'r') as f2:
###         dict2 = [json.loads(line) for line in f2]
###         second_file.extend(dict2)
##     
##    
##    
##    
##    
##
##
import shutil, os


from os.path import exists   
##       
def FinalCalculation(i):        
    for i in range(i, len(folder)-1):
        print(i, "value of i")
        j=i+1
        print(j, "value of j")
        print(len(folder))
        hashtags_FIRST= HashtagVocab(folder[i])
        hashtags_SECOND=HashtagVocab(folder[j])
        Category_FIRST=CategoryList(folder[i])
        Category_SECOND=CategoryList(folder[j])
        HD_VALUE=HashtagDiversity(hashtags_FIRST,hashtags_SECOND)
        
        CD_mid_value=Combined_KLOC_CD(Category_FIRST, Category_SECOND)
        print(HD_VALUE,CD_mid_value, "functions")
#        print(CD_mid_value, "CD_mid_value")
#        CD_VALUE= (0.5*(CD_mid_value[0])+0.5*(1.0-(CD_mid_value[1])))
#        print(CD_VALUE, "comid value")
##        print(CD_VALUE, "category value")
        linear_function= float(0.4*(HD_VALUE)+ 0.6*(CD_mid_value))
        print(linear_function, "Final Linear Function Calculation")
        
        if (linear_function)>0.5:
            
            print("yes both should be combined",folder[i], "and", folder[j])
#            print(Combine_two_files(folder[i],folder[j]))  # final combining will be done manually
        else:
#            shutil.copy("D:\\DATASETS\\16_09_2020\\Step_0_preprocessed\\"+folder[i], folder1)
            print("No they should not be combined")
#            Combine_two_files(folder[i], folder[i])
#            print("Combining Done")
#            i=j
#            FinalCalculation(i)
#        else:
#            print("entering into else")
#            i=j
        
    return()    
    
    
    
print(FinalCalculation(0))    
    
    
    
    
    
    
    
    
    
    
    
