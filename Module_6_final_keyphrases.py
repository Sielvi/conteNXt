# -*- coding: utf-8 -*-
"""
Created on Thu May 19 13:03:21 2022

@author: Sielvie
"""

import re 
import os

with open("Dataset_3\\18_JUNE_DATA\\Step_5_Bursty_segments_new\\all_segments.txt", 'r', encoding="utf-8") as handle:
         phrases = [line.rstrip('\n') for line in handle]
         
#dictionary_both={}         
import re
full_part_all=[]
phrases_1=[]
for i in range(0, len(phrases)):
    decimal_part=re.findall("\d+\.\d+", phrases[i])
    
    string_part=re.sub("\d+\.\d+",'', phrases[i])
    string_part=[string_part.strip()]
#    if phrases[i]=='jessica veronica ':
#        print("yes")
#        print(i)
    phrases_1.extend(string_part)
    full_part=string_part+decimal_part
    full_part_all.append(full_part)
    
         
dec1={}
for j in phrases_1:
    dec=[]
    for i in range(0, len(full_part_all)):
        if j == full_part_all[i][0]:
            
          dec.append(full_part_all[i][1])
        
#          print(full_part_all[i][0], "----")
    dec1[j]=dec
    
    
dictionary_seg={}   
for key, val in dec1.items():
    value1=max(val,key=lambda x:float(x))
    dictionary_seg[key]=value1
    
files=os.listdir("Dataset_3\\18_JUNE_DATA\\RESULTS\\only_semantics")    
for h in range(0, len(files)):
    
    with open("Dataset_3\\18_JUNE_DATA\\RESULTS\\only_semantics\\"+files[h], 'r', encoding="utf-8") as handle:
         RESULT = [line.rstrip('\n') for line in handle]
         
         
    res = [i.strip("[""]").split(",") for i in RESULT]
    seg=[]
    for item in range (0, len(res)):
       VERSIONS_F = []
       for j in range(0, len(res[item])):
          temp = res[item][j].replace("'",'')
          VERSIONS_F.append(temp)
       seg.append(VERSIONS_F)
#print (seg)

    sc_clu_sorted_upper=[]
    for i in range(0, len(seg)):
      sc_clu={}
      for j in range(0, len(seg[i])):
        se=seg[i][j].strip()
#        print(se, "se")
        sc_clu[se]=(dictionary_seg[se])
      sc_clu_sorted=sorted(sc_clu.items(), key = lambda x: x[1], reverse=True)[:10]
      sc_clu_sorted_1=[(i[0]) for i in sc_clu_sorted] 
      sc_clu_sorted_upper.append(sc_clu_sorted_1)
      file1=open("Dataset_3\\18_JUNE_DATA\\RESULT1\\SORTED\\"+files[h], "w")    
      for i in range(0, len(sc_clu_sorted_upper)):
         file1.write(str(sc_clu_sorted_upper[i]))
         file1.write("\n")
#file1.close()



#import math       
#import os  
#import json 
#list_of_files=os.listdir(r"Datasets\\2012-10-14_output_new\\STEP_1")    
#all_data=[]
#for file in range(0, len(list_of_files)):
#   with open("Datasets\\2012-10-14_output_new\\STEP_1\\"+list_of_files[file],'r', encoding='utf-8') as src:
##        tweet_count= sum(1 for line in open("0_features_forcombinedfiles\\"+list_of_files[file]))      
#        dict_tweetsi = [json.loads(line) for line in src]
#        all_data.extend(dict_tweetsi)
#        print("next")
#def convert(lst):
#            strlist = ' '.join(lst)
#            return strlist              
#tweet_count=len(all_data)
#outer=[]
#for i in range(0, len(sc_clu_sorted_upper)):
#  innrlist=[]
#  for second in range(0, len(sc_clu_sorted_upper[i]))  :
#      firstThree = sc_clu_sorted_upper[i][second][0:3]
#      innrlist.append(firstThree)
#  outer.append(innrlist)
#
#
#scoring={}
#for i in range(0, len(outer)):
#  for second in range(0, len(outer[i]))  :
##    print(sc_clu_sorted_upper[i][second], "---cluster")
#    tweet_freq=0
#    found=[]
#
#    for j in range(0, tweet_count):
#
#        text=all_data[j]['text']
#    #        print(type(text))
#    #        text=nlp(text)
#        hashtags=((all_data[j]['entities']['hashtags']))
#            
#        hashtags=((convert(hashtags)))
#    #        print(hashtags, "hashtags")
#        mentions=((all_data[j]['entities']['user_mentions']))
#        mentions=((convert(mentions)))
#           
#        final= text+ ' '+hashtags+' '+mentions
#            
#        final=final.strip()
#    #        if j==80:
#    #            print(final)
#        final=final.lower()
#        if (final.find(outer[i][second])!=-1):
#            
#            
##               
#  
#            tweet_freq+=1  
#  print("done for--", outer[i])         
#  score=(math.log(tweet_freq))
#  scoring[i]=score