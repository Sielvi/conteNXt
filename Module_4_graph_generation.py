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
#notepad_file=open("15_aug_2021_again\\Step_5_Bursty_segments_new\\\distinct_segments1.txt", "w")        
#for item in phrases:
#  notepad_file.write(str(item))
#  notepad_file.write("\n")
#notepad_file.close()        
##phrases=[]
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
##import networkx as nx
##from node2vec import Node2Vec

# Create a graph
##import networkx as nx
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

#seg_sim=word2vec_sim_nes

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
#               mentions=str(mentions)
               
                final= text+ ' '+hashtags+' '+mentions
        
                final=final.strip()

                final=final.lower()
#                print(final, "final")
#                print(hashtags, "---hashtags", mentions, "---mentions")
#                final=final.split(" ")
#                print(final, "splitted one")
#                print(final, "final")
#                final=removestoword(final)
#                if j== 2134:
                
                if (final.find(phrases[i])!=-1):     
#                     tweet.extend(all_data[j]['entities']['hashtags'])
#                     print(final, "----------final")
                     
##                     print(final, "--final before")  
#                     print("------found")
#                     print(final)
#                     print(mentions, "mentions")
#                     print(hashtags, "hashtags")
#                     print(phrases[i], "----------phrases")
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
#for file in range(0, len(list_of_files)):
##    with open("0_features_forcombinedfiles\\"+list_of_files[file],'r', encoding='utf-8') as src:
##        tweet_count= sum(1 for line in open("0_features_forcombinedfiles\\"+list_of_files[file]))
##      
##        dict_tweetsi = [json.loads(line) for line in src]
tweet_count=len(all_data)
for j in range(0, tweet_count):
              
                 
                text=all_data[j]['text']
#                print(text)
                hashtags=hashtagextraction(all_data[j])
                if not hashtags:
##                        print("next")
                        hashtags=''
                
                else:
                     hashtags=(' '.join(str(x) for x in hashtags))
#                print(hashtags, "hashtags")
                mentions=mentionextraction(all_data[j])
                if not mentions:
##                        print("next")
                        mentions=''
                
                else:
                     mentions=(' '.join(str(x) for x in mentions))
#                mentions=str(mentions)
#                print(mentions, "mentions")
                final= text+ ' '+hashtags+' '+mentions
        
                final=final.strip()

                final=final.lower()
##                print(final)
                for token in final.split():
##                    print(token,"token")
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
    
seg_sim = {key:{key2:(((0.75)*val1)+((0.25)*word2vec_sim_nes[key][key2])) for key2,val1 in subdic.items()} for key,subdic in hashtag_sim_nes.items()}        
#seg_sim=word2vec_sim_nes        
##        
##import networkx as nx
###for ph in range(0, len(phrases)):
###    phrases_dict[phrases[ph]]=ph
##
##def get_events(phrases, seg_sim ,n_neighbors=3, max_cluster_segments=20, threshold=4):
##    """
##    return event clusters from bursty_segment_scores(dict from seg_name to bursty_wt)
##    using a variation of Jarvis Patrick Clustering Algo
##    """    
###    print(seg_sim, "-----------------------------------------------------------------------------------------------seg_sim")
##    bursty_segments = list(phrases)
###    print(bursty_segments,"--bursty segments")
##    n = len(bursty_segments)
###    print(n,"----------------------------bursty segments")
##    G = nx.Graph()
##    G.add_nodes_from(range(n))
##    #print(G.nodes,"nodes of graph")
##    
##    k_neighbors = {}
##    for i in range(n):
##        
##        k_neighbors[i] = get_k_neighbors(n_neighbors, i, seg_sim)
##        if i==674 :
##            print( k_neighbors[i],  k_neighbors[i])
##    # add edge between a,b if both in k_neighbors of other
##    for i in range(n):
##        for j in range(i+1,n):
##            if i in k_neighbors[j] and j in k_neighbors[i]:
##                G.add_edge(i,j)
##    #print(nx.draw(G))
###    print("done")
###    print(list(nx.connected_components(G)),"graph connected components ")
##    # for sg in nx.connected_components(G):
##    #     h=(nx.subgraph(G, sg))
##    #     print(h.nodes,"nodes")
##    #     print (h.edges,"edges")
###    clusters = [] # each cluster is a tuple of list(segments) and event_newsworthiness
###    max_event_worthiness = 0
###    file= open("Datasets\\2012-10-12_output_new\\\RESULTS\\Result_after_entity_filteration__without_repetition_word2vec_win_3_and_nei_3__top_5_similarity_0.75_0.25_1n_nei.txt", "w")
##    for sg in nx.connected_components(G):
##        h=(nx.subgraph(G, sg))
###        print(list(h),"graph connected components ")
##        n = len(h.nodes)
###        print(n,"--------------lenth of nodes")
###        print(n_neighbors,"---")
###        print(1.5*n_neighbors,"-------------")
##        
###        print()
##        if(n < 1.*n_neighbors): continue # remove clusters with size < 1.5*n_neighbors
##       # print("trueeeeeeeeeeeeeee")
###        print (h.edges,"---after")
###        print (h.nodes,"after")
##        cluster_segments = [bursty_segments[i] for i in h.nodes]
##        
##        
###        print(cluster_segments,"cluster segments")
##    
##
###        event_newsworthiness = sum([segment_newsworthiness[s] for s in cluster_segments])/n
###        print(event_newsworthiness,"previous")
###        event_newsworthiness *= sum([seg_sim[i][j] for i,j in h.edges])/n
###        print(event_newsworthiness,"nextt")
###        max_event_worthiness = max(max_event_worthiness,event_newsworthiness)
##        
##        # keep top k=max_cluster_segments segments as per bursty_score
##        cluster_segments1 = sorted(cluster_segments)[:max_cluster_segments]
###        file.write('%s\n' %cluster_segments1)
##    return cluster_segments1
###        print(max_event_worthiness,"maxxxxxxx")
###        print (cluster_segments,"cluster____________Segments")
###        clusters.append((cluster_segments, event_newsworthiness))
###        
###    clusters = sorted(clusters, key = lambda x:x[1], reverse=True)
###    print(clusters,"---------------------clusters")
###    threshold_worthiness = max_event_worthiness/threshold
###    print(threshold_worthiness,"-----threshold_worthiness")
##
##
##def get_k_neighbors(p, seg, seg_sim): #intially make all neigbors but then extract top p in ascending order of their similarity
##    """
##    return set of k nearest neighbors of 'seg'
##    """
##    # print(seg_sim,"segment similarity")
##    neighbor_list = []
##    sim_list = [] # sim_list[i] = similarity of seg with neighbor[i]
##    for i in seg_sim:
##        # print(seg_sim,"segment similarity")
##        # print(i,"i")
###        print (i,"--i")
##        # print("next")
###        print (seg,"segment")
##        if i == seg: continue
##        else:
###            print(i, "i")
###            if i>0.2:
##            neighbor_list.append(i)
###        print(neighbor_list,"neighbor list" )
##       
##        sim_list.append(seg_sim[seg][i])
###        print(seg_sim[seg][i],"seg[i]")
##        # print("next")
##        # print(sim_list,"sim_list")
###    print(set([x for _,x in sorted(zip(sim_list,neighbor_list), reverse=True)][:p]))
##    return set([x for _,x in sorted(zip(sim_list,neighbor_list), reverse=True)][:p])
##
##
##
##
##
##
##print(get_events(phrases, seg_sim))
##        
        
