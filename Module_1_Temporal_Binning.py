# -*- coding: utf-8 -*-
"""
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
        
folder = os.listdir( '' ) #FOLDER IN THE DIRECTORY WITH MULTIPLE JSON FILES OF THE DAY
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
        full_filename = "%s/%s" % ('', dirs)   #FIRST TIME INTERVAL (FIRST JSON FILE)
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

        return((vocab_of_a_folder))



 

authenticator = IAMAuthenticator('XXXXXXXXXXXXXXXXXXXXXXXX') #to be added after making an account
natural_language_understanding = NaturalLanguageUnderstandingV1(version='date',authenticator=authenticator)
natural_language_understanding.set_service_url('') #Url to be added
      
def CategoryList(file):
    print("Inside CategoryList Function")
    category_of_a_folder=[]

    tweets_first_interval = []
    
#        print(len(dirs))
    CD_full_filename = "%s/%s" % ('', file)   #FIRST TIME INTERVAL (FIRST JSON FILE)
    with open(CD_full_filename,'r', encoding="utf-8") as fi:
        dict_tweetsi = [json.loads(line) for line in fi]
            
        for insidei in range(0,len(dict_tweetsi)):
            tweeti=dict_tweetsi[insidei]['text']  #tweet from json file with the header "text"
            tweets_first_interval.append(tweeti)
               
    Sample_Interval1=sample(tweets_first_interval,1000) 
    Sample_Interval1=('[{}]'.format(', '.join(Sample_Interval1)))
#    print(Sample_Interval1)
    
    response = natural_language_understanding.analyze(text= Sample_Interval1,features=Features(categories=CategoriesOptions())).get_result()

    category_dict_t1={}
    for r in response['categories']:
            

            category= r['label']

            score=r['score']
            if score<0.7:
                continue
            else:
                category_dict_t1[category]= score
            
            

    category_of_a_folder.append(category_dict_t1)

    return(category_dict_t1)        
##        
##
##
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def HashtagOverlapScore(list1,list2):
  
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
#
    dict_intersection= list(dict1.keys()&dict2.keys())

    def Average(lst):
        return sum(lst) / len(lst)
        
#    print((dict_intersection),"length of intersection")
    oc=  (len(dict_intersection)/min(len(list(dict1.keys())), len(list(dict2.keys()))))
    all_values=[]
    for items in dict_intersection:

         first=((dict1[items]))
         second=((dict2[items]))

         AVG=min(first, second)
         all_values.append(AVG)
#    print(all_values, "all_values")
    avg2=Average(all_values)
    overlap=oc*avg2

    return (overlap)

folder1 =('') #New folder will be created with the output of temporal binning
def Combine_two_files(file1, file2):
     with open("\\Step_0_preprocessed\\"+file1,'r',encoding="utf-8") as f1:
        dict_tweets1 = [json.loads(line) for line in f1]
     with open("\\Step_0_preprocessed\\"+file2,'r', encoding="utf-8") as f2:
        dict_tweets2 = [json.loads(line) for line in f2]
     dict_tweets= dict_tweets1+dict_tweets2
     file_name = file1+file2+"combined.json"
     file = os.path.join(folder1, file_name)
     with open(file, 'w', encoding="utf-8") as f:
         for items1 in dict_tweets:
           f.write('%s\n' %items1)

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
        HD_VALUE=HashtagOverlapScore(hashtags_FIRST,hashtags_SECOND)
        
        CD_mid_value=Combined_KLOC_CD(Category_FIRST, Category_SECOND)
        print(HD_VALUE,CD_mid_value, "functions")

        linear_function= float(0.4*(HD_VALUE)+ 0.6*(CD_mid_value))
        print(linear_function, "Final Linear Function Calculation")
        
        if (linear_function)>0.5:
            
            print("yes both should be combined",folder[i], "and", folder[j])

        else:
            shutil.copy("\\Step_0_preprocessed\\"+folder[i], folder1)
            print("No they should not be combined")
#          
        
    return()    
    
    
    
print(FinalCalculation(0))    
    
    
    
    
    
    
    
    
    
    
    
