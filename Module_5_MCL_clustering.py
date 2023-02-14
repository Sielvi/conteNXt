# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 14:11:18 2022

@author: Sielvie
"""

#with open("Datasets\\2012-10-12_output\\Step_4_Bursty_segments\\all_segments.txt",'r', encoding='utf-8') as src:
#    phrases1 = [line.rstrip('\n') for line in src]
#
#
#       
#import re       
#decimal_list=[]   
#string_list=[]      
#for i in range(0, len(phrases1)):
#    decimal_part_list=re.findall("\d+\.\d+",phrases1[i]) # regex to extract decimal part
#    decimal_list.extend(decimal_part_list)
#    decimal_part = ''.join(decimal_part_list)
##    print(decimal_part)
#    string_part=re.sub("\d+\.\d+",'', phrases1[i])
#    string_list.append(string_part)
#    
##    dictionary_both[string_part]=decimal_part
#    
#new_phrases1={}
#for i in range(0, len(string_list)):
#    count_no_of_phrases= string_list.count(string_list[i])
#    new_phrases1[string_list[i]]=count_no_of_phrases
#
#new_phrases={}
#for key, value in new_phrases1.items():
#    if value>1:
#        continue
#    else:
#        new_phrases[key]=value
#    
#phrases=[]   
#for key, value in new_phrases.items():
##    if value>5:
#        print(key, "---key")
#        phrases.append(key)
#        
#print(len(phrases)) 

import re 
import os

with open("D:\\DATASETS\16_09_2020\\Step_5_Bursty_segments_new\\all_segments.txt", 'r', encoding="utf-8") as handle:
         phrases = [line.rstrip('\n') for line in handle]
         
#dictionary_both={}         
decimal_list=[]   
string_list=[]      
for i in range(0, len(phrases)):
    decimal_part_list=re.findall("\d+\.\d+",phrases[i]) # regex to extract decimal part
    decimal_list.extend(decimal_part_list)
    decimal_part = ''.join(decimal_part_list)
#    print(decimal_part)
    string_part=re.sub("\d+\.\d+",'', phrases[i])
    string_list.append(string_part)
    
#    dictionary_both[string_part]=decimal_part
# =============================================================================
# when top 1329 segments needs to be accessed    
# =============================================================================
#def merge(list1, list2):
#
#    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
#    return merged_list
#both_list=((merge(string_list, decimal_list)))
#
#segments_all=(sorted(both_list,key=lambda x: x[1], reverse=True)[:2007])
#list_of_phrases=[]
#for l in segments_all:
#    list_of_phrases.append(l[0])
#list_of_phrases=set(list_of_phrases)
#def convert(set):
#    return sorted(set)
#
#phrases=(convert(list_of_phrases))
# =============================================================================
# 
# =============================================================================
#list_of_phrases_1=list(list_of_phrases)
#segment_all_set= set(segments_all)
#segment_all_list=list(segment_all_set)
#phrases=[]           
#for seg in range(0, len(segments_all)):
#    if phrases.count(segments_all[seg][0])>1
#    if seg==1329:
#        break
#    else:
#        phrases.append(segments_all[seg][0])
#top_segments=[]
#for j in range(0, len(segments_all)):
#    for key,value in dictionary_both.items():
#        if sorted_list[j]==value:
##            if sorted_list[j] < '0.0':
##                continue
#            top_segments.append(key)

#for key,value in dictionary_both.items():
##        if sorted_list[j]==value:
#            if float(value) < 1.67 :
#                continue
#            else:
#              top_segments.append(key)
#top_segments = sorted(dictionary_both.items(), key=lambda x: x[1], reverse=True)[:1329]
# =============================================================================
# when all needs to be accessed
# =============================================================================
phrases=[]           
for seg in range(0, len(string_list)):
#    if seg==1329:
#        break
#    else:
        phrases.append(string_list[seg])
#phrases1=set(phrases1)
#def convert(set):
#    return sorted(set)
#phrases=(convert(phrases1))
# =============================================================================
# 
# =============================================================================
#notepad_file=open("Datasets\\2012-10-12_output_new\\Step_4_Bursty_segments_without_further_filter\\phrases__all_a", "w")        
#for item in phrases:
#  notepad_file.write(str(item))
#  notepad_file.write("\n")
#notepad_file.close()        
#phrases=[]
#from nltk import ngrams
#for strings in top_segments:
#    print(strings, "-strings1")
#    occurence=top_segments.count(strings)
#    if occurence > 1:
##        print("yes")
#        top_segments.append(strings)
#    else:
#        if occurence<2 and len(strings.split())>2:
##            print(strings, "---strings2")
#            n = 2
#            two_grams = ngrams(strings.split(), n)
#            grams_list=[]
#           
#    #        print()
#            for grams in two_grams:
##                 print(grams, "----before joining")
#    #             print(count)
#    #             if count==2871:
#    #                 print(grams)
#                 grams=' '.join(grams)
##                 print(grams, "-----after joining")
#                 grams_list.append(grams)
##            print(grams_list, "----list")
##            print(string_list, "-----string list")
##            answer=list(set(grams_list).intersection(set(final_phrases))) 
##            print(answer)
#            if  any(e in grams_list for e in top_segments) :le
##                 print("yes")
#                 phrases.append(strings)
#            else:
#                continue
#        else:
#                continue       
#        
import networkx as nx
from node2vec import Node2Vec

# Create a graph
import networkx as nx
from collections import Counter
import re
import gc
import numpy as np
import math
from scipy import sparse
import json
from gensim.models import Word2Vec
## ============================================================================
# graph intializing
# =============================================================================
#import spacy
#from spacy.lang.en import English
#nlp = English()
#nlp = spacy.load('en_core_web_sm')
def is_ascii(s):
           try:
               s.encode(encoding='utf-8').decode('ascii')
           except UnicodeDecodeError:
              return False
           else:
                 return True


def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
def convert(lst):
            strlist = ' '.join(lst)
            return strlist

def OverlapCofficient(dict1,dict2):
    
    try:
        dict_intersection= intersection(dict1, dict2)
        oc= (len((set(dict_intersection))))/(min(len(set(dict1)), len(set(dict2))))
        return oc
    except ZeroDivisionError:
        oc = 0.0
        return oc
    
import os   
list_of_files=os.listdir(r"Dataset_3\\18_JUNE_DATA\\Step_1_New_intervals_with_extended_tweet")
   
all_data=[]
for file in range(0, len(list_of_files)):
   with open("Dataset_3\\18_JUNE_DATA\\Step_1_New_intervals_with_extended_tweet\\"+list_of_files[file],'r', encoding='utf-8') as src:
#        tweet_count= sum(1 for line in open("0_features_forcombinedfiles\\"+list_of_files[file]))      
        dict_tweetsi = [json.loads(line) for line in src]
        all_data.extend(dict_tweetsi)
        print("next")
           
print(len(phrases))    

#
#
#inut_to_word2vec=[]
##for file in range(0, len(list_of_files)):
###    with open("0_features_forcombinedfiles\\"+list_of_files[file],'r', encoding='utf-8') as src:
###        tweet_count= sum(1 for line in open("0_features_forcombinedfiles\\"+list_of_files[file]))
###      
###        dict_tweetsi = [json.loads(line) for line in src]
tweet_count=len(all_data)
#for j in range(0, tweet_count):
#
#    text=all_data[j]['text']
#
#    hashtags=((all_data[j]['entities']['hashtags']))
#
#    hashtags=((convert(hashtags)))
#
#    mentions=((all_data[j]['entities']['user_mentions']))
#    mentions=((convert(mentions)))
#   
#    final= text+ ' '+hashtags+' '+mentions
#
#    final=final.strip()
#
#    final=final.lower()
#    final=final.split(" ")
# 
#    for token in final:
#        inut_to_word2vec.append(((token)))
        
#print("word2vec training")
#word2vec_model = Word2Vec([inut_to_word2vec], size=50, window=5, min_count=1, workers=1, sg=1)   
#word2vec_list=[]
#for val in phrases:
#    word2vec_inside_list=[]
##    print(len(val.split()))
#    if len(val.split())>1:
##        val=nlp(val)
#        val=val.split()
#        count=0
#        for token in val:
#            embed=word2vec_model[str(token)]
##             print(token, "---token")
#            word2vec_inside_list.extend(embed)
#            count+=1
#    
#        word2vec_list.append(word2vec_inside_list)
#        print(count, "count")
#    else:
##         print (word2vec_model[val], val, "---word")
#         word2vec_list.append(word2vec_model[val])
#
#print("word2vec done")
#print("Word2vec similarity calculation started")
#list1=[]
#for l in range(0, len(word2vec_list)):
#    list1.append(len(word2vec_list[l]))
#maximum_value=max(list1)
#def cosine(u, v):
#    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
#
#
#word2vec_list_maximum_value=[]
#for p in range(0, len(word2vec_list)):
#    if len (word2vec_list[p])<maximum_value:
#          n=maximum_value-(len(word2vec_list[p]))
##          print(maximum_value, "maximum_value")
##          print((len(word2vec_list[p])), "(len(word2vec_list))")
##          print(n, "--n")
##          
#          word2vec_list_maximum_value.append(np.pad(word2vec_list[p], (0, n), 'constant'))
#    else:
#        word2vec_list_maximum_value.append(word2vec_list[p])
##          print(word2vec_list_maximum_value[i-1], "word2vec_list_maximum_value")
#
#
#
#word2vec_sim_nes={}
#for m in range(0, len(word2vec_list_maximum_value)):
#    word2vec_sim={}
#    for n in range(0,len (word2vec_list_maximum_value)):
#        sim=cosine(word2vec_list_maximum_value[m],word2vec_list_maximum_value[n])
#        word2vec_sim[n]=sim
#    word2vec_sim_nes[m]=word2vec_sim
#
#
#print("Word2vec similarity calculation done")
##






#seg_sim=word2vec_sim_nes

       
        
        
#print("preperation for hashtag")       
#all_phrase={}        
#all_hashtags={}        
#for i in range(0, len(phrases)):
#    
#   
#     count_in_whole_dataset=[]
#     phrases[i]=phrases[i].replace("'", "")
#     tweet=[]
#     
#     count=0
#     for j in range(0, tweet_count):
#              
#                 
#                text=all_data[j]['text']
##                print(text)
#                hashtags=((all_data[j]['entities']['hashtags']))
#        
#                hashtags=((convert(hashtags)))
#
#                mentions=((all_data[j]['entities']['user_mentions']))
#                mentions=((convert(mentions)))
#       
#                final= text+ ' '+hashtags+' '+mentions
#        
#                final=final.strip()
#
#                final=final.lower()
##                final=final.split(" ")
#                if (final.find(phrases[i])!=-1):     
#                     tweet.extend(all_data[j]['entities']['hashtags'])
#                     count+=1
#     all_phrase[phrases[i]]=count
#     print(i, "----for the phrase")
#     all_hashtags[i]=tweet
#
#hashtag_sim_nes={}
#for list1 in range(0, len(all_hashtags)):
#    hashtag_sim={}
#    for list2 in range(0, len(all_hashtags)):
#        overlap_coff=OverlapCofficient(all_hashtags[list1], all_hashtags[list2])
#        hashtag_sim[list2]=overlap_coff
#    hashtag_sim_nes[list1]=hashtag_sim
#
#print("hashtags calculation done")   
##        
##    
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


def mentionextraction(dicti1):
##        print(dicti1)
            try:
                men=[]
                for i in range(0, len(dicti1['extended_tweet']['entities']['user_mentions'])):
                        ment=(dicti1['extended_tweet']['entities']['user_mentions'][i]['name'].lower())
                        if is_ascii(ment)==False:
                            continue
                        else:
                            men.append(ment)
                return(men)       
            except:
                men=[]
                for i in range(0, len(dicti1['entities']['user_mentions'])):
                        ment=(dicti1['entities']['user_mentions'][i]['name'].lower())
                        if is_ascii(ment)==False:
                            continue
                        else:
                            men.append(ment)
                return(men)
#



inut_to_word2vec=[]
#for file in range(0, len(list_of_files)):
##    with open("0_features_forcombinedfiles\\"+list_of_files[file],'r', encoding='utf-8') as src:
##        tweet_count= sum(1 for line in open("0_features_forcombinedfiles\\"+list_of_files[file]))
##      
##        dict_tweetsi = [json.loads(line) for line in src]
tweet_count=len(all_data)
for j in range(0, tweet_count):
#    print(j, "----j")
    text=all_data[j]['text']
#    print(text, "texttt")
    hashtags=((all_data[j]['entities']['hashtags']))
#    print(hashtags, "---hashtags")
#    if not hashtags:
#        hashtags=""
#    else:
#        hashtags=((convert(hashtags)))
#    hashtags=((convert(hashtags)))
#
#    mentions=([(all_data[j]['entities']['user_mentions']['name'])])
##    print(mentions, "---mentions")
##    if not mentions:
##        mentions=""
##    else:
##        mentions=((convert(mentions)))
#    mentions=((convert(mentions)))
    hashtags=hashtagextraction(all_data[j])
    if not hashtags:
                        hashtags=""
    else:
                        hashtags=((convert(hashtags)))
                            #        print(type(text))
            #        text=nlp(text)
#                print((dict_tweetsi[j]['entities']['hashtags']))
#                 if (not dict_tweetsi[j]['entities']['hashtags']):
# ##                        print("if")
#                     hashtags=''

#                 else:
#                     hashtags=((dict_tweetsi[j]['entities']['hashtags'][0]['text']))
                    
                
##                print(hashtags, "hashtags")
    mentions=mentionextraction(all_data[j])
    if not mentions:
                    mentions=""
    else:
                    mentions=((convert(mentions)))
    final= text+ ' '+hashtags+' '+mentions

    final=final.strip()

    final=final.lower()
    final=final.split(" ")
 
    for token in final:
        inut_to_word2vec.append(((token)))
from gensim.models import FastText
print("word2vec training")
word2vec_model = Word2Vec([inut_to_word2vec], size=50, window=5, min_count=1,sg=1)   
word2vec_list=[]
count1=0
for val in phrases:
    print(val)
    count1+=1
    word2vec_inside_list=[]
#    print(len(val.split()))
    if len(val.split())>1:
#        val=nlp(val)
        val=val.split()
        count=0
        for token in val:
#            print(token)
            embed=word2vec_model[str(token)]
#             print(token, "---token")
            word2vec_inside_list.extend(embed)
            count+=1
    
        word2vec_list.append(word2vec_inside_list)
        print(count, "count")
    else:
#         print (word2vec_model[val], val, "---word")
         word2vec_list.append(word2vec_model[val])
    print(count1)
print("word2vec done")
print("Word2vec similarity calculation started")
list1=[]
for l in range(0, len(word2vec_list)):
    list1.append(len(word2vec_list[l]))
maximum_value=max(list1)
def cosine(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))


word2vec_list_maximum_value=[]
for p in range(0, len(word2vec_list)):
    if len (word2vec_list[p])<maximum_value:
          n=maximum_value-(len(word2vec_list[p]))
#          print(maximum_value, "maximum_value")
#          print((len(word2vec_list[p])), "(len(word2vec_list))")
#          print(n, "--n")
#          
          word2vec_list_maximum_value.append(np.pad(word2vec_list[p], (0, n), 'constant'))
    else:
        word2vec_list_maximum_value.append(word2vec_list[p])
#          print(word2vec_list_maximum_value[i-1], "word2vec_list_maximum_value")



word2vec_sim_nes={}
for m in range(0, len(word2vec_list_maximum_value)):
    word2vec_sim={}
    for n in range(0,len (word2vec_list_maximum_value)):
        sim=cosine(word2vec_list_maximum_value[m],word2vec_list_maximum_value[n])
        word2vec_sim[n]=sim
    word2vec_sim_nes[m]=word2vec_sim


print("Word2vec similarity calculation done")
#
    
#seg_sim = {key:{key2:(((0.75)*val1)+((0.25)*word2vec_sim_nes[key][key2])) for key2,val1 in subdic.items()} for key,subdic in hashtag_sim_nes.items()}        
        
seg_sim=    word2vec_sim_nes
        
import networkx as nx
import markov_clustering as mc
import networkx as nx
import random


bursty_segments = list(phrases)
#    print(bursty_segments,"--bursty segments")
n = (bursty_segments)
list_of_dict = []
list_of_dicts=[]
for key, values in seg_sim.items():
   for keys,val in values.items():
    list_of_dict.append(val)
list_of_dicts.append(list_of_dict)
#    print(n,"----------------------------bursty segments")
g=nx.Graph()
counter1=0
for i in n:
  for j in n:
        
       
        g.add_edge(str(i),str(j), weight = list_of_dict[counter1])
#        print(counter1, "counter1",i, "--i", j, "---j")
#        print(list_of_dict[counter1])
        counter1+=1
#print(g.edges())
matrix = nx.to_numpy_matrix(g)
print("matrix done")
result = mc.run_mcl(matrix, inflation=2)    
print("going for clusters")       # run MCL with default parameters
clusters = mc.get_clusters(result) 
print(clusters)
#file_clusters=open("Datasets\\2012-10-12_output_new\\RESULTS\\events_r=5_equal_weight_after_entity_filteration_after_word_sim.txt","w")
#for k in range(0, len(clusters)):
#    file_clusters.write(str(clusters[k]))
#    file_clusters.write("\n")
#file_clusters.close()
res = [list(ele) for ele in clusters]
overall_clu=[]
for one in range(0, len(res)):
    clu=[]
    for two in range(0, len(res[one])):
        for three in range(0,len(phrases)):
            if (res[one][two])==three:
                clu.append(phrases[three])
    overall_clu.append(clu)    
    
file_clusters1=open("Dataset_3\\18_JUNE_DATA\RESULTS\\only_semantics\\W=5_r=2.txt","w")
for p in range(0, len(overall_clu)):
    if len((overall_clu[p]))==1 or  len((overall_clu[p]))<3: continue
    file_clusters1.write(str(overall_clu[p]))
    file_clusters1.write("\n")
file_clusters1.close()