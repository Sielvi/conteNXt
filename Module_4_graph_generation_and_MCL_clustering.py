# -*- coding: utf-8 -*-
"""

@author: Sielvie
"""


import re 
import os

with open("8_11_2020\\Step_5_Bursty_segments_new\\all_segments.txt", 'r', encoding="utf-8") as handle:
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
    

# =============================================================================
# when all needs to be accessed
# =============================================================================
phrases1=[]           
for seg in range(0, len(string_list)):
#    if seg==1329:
#        break
#    else:
        phrases1.append(string_list[seg])
phrases1=set(phrases1)
def convert1(set):
    return sorted(set)
phrases=(convert1(phrases1))
# =============================================================================
# 
# =============================================================================

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



def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
#def convert(lst):
#            strlist = ' '.join(lst)
#            return strlist

def OverlapCofficient(dict1,dict2):
    
    try:
        dict_intersection= intersection(dict1, dict2)
        oc= (len((dict_intersection)))/(min(len(set(dict1)), len(set(dict2))))
        return oc
    except ZeroDivisionError:
        oc = 0.0
        return oc
    
import os   
list_of_files=os.listdir(r"8_11_2020\\Step_1_New_intervals_with_extended_tweet")
import ast  
all_data=[]
for file in range(0, len(list_of_files)):
   with open("8_11_2020\\Step_1_New_intervals_with_extended_tweet\\"+list_of_files[file],'r', encoding='utf-8') as src:
#        tweet_count= sum(1 for line in open("0_features_forcombinedfiles\\"+list_of_files[file]))      
        dict_tweetsi = [json.loads(line) for line in src]
        all_data.extend(dict_tweetsi)
        print("next")
           
print(len(phrases))    


tweet_count=len(all_data)


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
def convert(lst):
            strlist = ' '.join(lst)
            return strlist


from nltk import word_tokenize
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))


def removestoword(example_sent):
   word_tokens = word_tokenize(example_sent)
   filtered_sentence = [w for w in word_tokens if not w.lower() in stop]
   filtered_sentence = []
   for w in word_tokens:
     if w not in stop:
       filtered_sentence.append(w)
##   print(filtered_sentence)
   return filtered_sentence
  
##print(word_tokens)
    
print("preperation for hashtag")

all_phrase={}        
all_hashtags={}        
for i in range(0, len(phrases)):
    
#     print(phrases[i])
     count_in_whole_dataset=[]
     phrases[i]=phrases[i].replace("'", "")
     tweet=[]
     
     count=0
     for j in range(0, tweet_count):
              
#                print(i, j,all_data[j]['text'])
                text=all_data[j]['text']
#                print(text)
                hashtags=hashtagextraction(all_data[j])
                if not hashtags:
                        hashtags=""
                else:
                        hashtags=((convert(hashtags)))

                mentions=mentionextraction(all_data[j])
                if not mentions:
                    mentions=""
                else:
                    mentions=((convert(mentions)))
#               mentions=str(mentions)
               
                final= text+ ' '+hashtags+' '+mentions
        
                final=final.strip()

                final=final.lower()

                
                if (final.find(phrases[i])!=-1):     

                     tweet.extend(removestoword(final))
##                     print(final, "--final after")
                     count+=1
     all_phrase[phrases[i]]=count
     print(i,phrases[i] ,"----for the phrase")
##     print(tweet, "---tweet")
     counts = Counter(tweet)
#     print(counts)
     top_5=counts.most_common(5)
     words=[i[0] for i in top_5]
     top_51=[]
     for m in range(0, len(phrases[i].split())):
#     print(phrases[26].split()[i])
         if phrases[i].split()[m] in words:
             top_5=counts.most_common(len(top_5)+1)
             top_51.extend(top_5)
#         top_5=counts.most_common(5)
##     print(top_5)
     new_top_5=set(top_51)
     new_top_5=list(new_top_5)
     words1=[i[0] for i in new_top_5]
     for k in range(0, len(phrases[i].split())):
         if phrases[i].split()[k] in words1:
           words1.remove(phrases[i].split()[k])
#     tweet=list(set(tweet))
     print(words1, "-------words")
     all_hashtags[i]=words1   

hashtag_sim_nes={}
for list1 in range(0, len(all_hashtags)):
#    print(list1, "first")
    hashtag_sim={}
    for list2 in range(0, len(all_hashtags)):
        overlap_coff=OverlapCofficient(all_hashtags[list1], all_hashtags[list2])
        hashtag_sim[list2]=overlap_coff
    hashtag_sim_nes[list1]=hashtag_sim

print("hashtags calculation done")   
#        
#    

seg_sim=hashtag_sim_nes

#
#
inut_to_word2vec=[]

tweet_count=len(all_data)
for j in range(0, tweet_count):
              
                 
                text=all_data[j]['text']

                hashtags=hashtagextraction(all_data[j])
                if not hashtags:

                        hashtags=''
                
                else:
                     hashtags=(' '.join(str(x) for x in hashtags))

                mentions=mentionextraction(all_data[j])
                if not mentions:

                        mentions=''
                
                else:
                     mentions=(' '.join(str(x) for x in mentions))

                final= text+ ' '+hashtags+' '+mentions
        
                final=final.strip()

                final=final.lower()

                for token in final.split():

                    inut_to_word2vec.append(((token)))
#from gensim.models import FastText
print("word2vec training")
word2vec_model = Word2Vec([inut_to_word2vec], size=50, window=3, min_count=1,sg=1)   
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
            embed=word2vec_model.wv[str(token)]
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

#          
          word2vec_list_maximum_value.append(np.pad(word2vec_list[p], (0, n), 'constant'))
    else:
        word2vec_list_maximum_value.append(word2vec_list[p])



 
    
word2vec_sim_nes={}
for m in range(0, len(word2vec_list_maximum_value)):
    word2vec_sim={}
    for n in range(0,len (word2vec_list_maximum_value)):
        sim=cosine(word2vec_list_maximum_value[m],word2vec_list_maximum_value[n])
        word2vec_sim[n]=sim
    word2vec_sim_nes[m]=word2vec_sim


print("Word2vec similarity calculation done")
#
    
seg_sim = {key:{key2:(((0.75)*val1)+((0.25)*word2vec_sim_nes[key][key2])) for key2,val1 in subdic.items()} for key,subdic in hashtag_sim_nes.items()}        


# seg_sim=    word2vec_sim_nes
        
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