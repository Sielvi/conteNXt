# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 12:03:28 2022

@author: Sielvie
"""

import json
import os
import sys
sys.path.append('../')
import csv
# =============================================================================
# This program alculates the frequency of the phrases or segments in the file.
#ph_freq will calculate the frequency of the word, and finally count the unique words.
# total_phrases counts all number of phrases
#scenario where above both become equal when count of all the segments is 1.
# =============================================================================
#from TweetSegmenter import SEDTWikSegmenter

def Prob (file1):
#    tweet_dir = 'C:\\Users\\Sielvie\\.spyder-py3\\Dec21\\Experiment\\Modules\\Fresh\\Step_3/' # end with '/'
#    ph_prob_file = 'C:\\Users\\Sielvie\\.spyder-py3\\Dec21\\Experiment\\Modules\\Fresh\\1_AFTER_TEMPORAL_BINNG\\Step_prob\\ph_prob_after_preprocessing_file.json'
    #tw_seg = SEDTWikSegmenter(wiki_titles_file='C:\\Users\\Sielvie\\.spyder-py3\\SEDTWik-Event-Detection-from-Tweets-master\\data\\enwiki-titles-unstemmed.txt', hashtag_wt=1, entities_only=False)
#   print
    ph_freq = {}
    total_phrases = 0
    
#    for dir_path, sub_dir_list, file_list in os.walk(tweet_dir):
#        print("inside directory")
#        dir_path = dir_path.replace('\\','/') # make windows-like path to unix-like path which can be used for both
#        dir_name = dir_path.replace(tweet_dir,'') 
#        print('Found directory: %s' % dir_name)
#        print(file_list, "-------file_list")
#        for fname in file_list:
    file=[]
    #        print('\t', fname)
    with open("D:\\DATASETS\\16_09_2020\\Step_2_Features_new\\"+file1+"all_tokens.txt",'r', encoding='utf-8') as src:
                file = [line.rstrip('\n') for line in src]
    #        print(lines)
    for i in range(0, len(file)):
    #            print(file[i], "---filei")
    #            file[i]=file[i].strip('"') 
    #            print(file[i], "---new file ii")
                phrase=[file[i]]
    #            print(phrase)
                total_phrases += len(phrase)
                for ph in phrase:
    #                    print(ph_freq, "ph_freq")
                        ph_freq[ph] = ph_freq.get(ph,0) + 1
                        
                        
    print('Total phrases:',total_phrases)
    print('Total Unique phrases:',len(ph_freq))
    ph_prob = {k: v/total_phrases for k,v in ph_freq.items()}
                   
    #       print((row[0].split(","))[1])      
    #                line = line.replace('\n','')
    #                segmentation =
    #                print(segmentation, "--segmentation")
    #                total_segs += len(segmentation)
    ##                print(total_segs, "total segments")erick today looking see teelin star action beginners chase', 'rt rt wants s good looks longing sexual contact']
    #                for seg in segmentation:
    ##                    print(seg,"----seg ")
    #                    seg_freq[seg] = seg_freq.get(seg,0) + 1
    ##            print ("next file", len(seg_freq), (total_segs))    
    ##    print ("next folder", len(seg_freq), (total_segs))        # print(seg_freq, "frequency")
    #
    #Time_win_list=list(set().union(hashtag_list, mention_list, keyword, NERTag_result))
    #
    #print('Done')
    #print('Total Segments:',total_segs)
    #print('Total Unique Segments:',len(seg_freq))
    #seg_prob = {k: v/total_segs for k,v in seg_freq.items()}
    ##print(seg_prob)
    try:
         os.mkdir("D:\\DATASETS\\16_09_2020\\Step_4_Probability_new")  #create new folder in current directory
    except FileExistsError:
         pass
    with open("D:\\DATASETS\\16_09_2020\\Step_4_Probability_new\\"+file1+"prob.json",'w') as f:
        json.dump(dict(sorted(ph_prob.items())), f, indent=4)
    return()
