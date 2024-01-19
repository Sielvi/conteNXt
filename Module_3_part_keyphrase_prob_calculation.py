# -*- coding: utf-8 -*-
"""
@author: Sielvie
"""

import json
import os
import sys
sys.path.append('../')
import csv
# =============================================================================
# This program alculates the frequency of the keyphrases in the file.
# total_phrases counts all number of phrases
# scenario where above both become equal when count of all the segments is 1.
# =============================================================================


def Prob (file1):

    ph_freq = {}
    total_phrases = 0
    

    file=[]
    #        print('\t', fname)
    with open("\\Step_2_Features_new\\"+file1+"all_tokens.txt",'r', encoding='utf-8') as src:
                file = [line.rstrip('\n') for line in src]
    #        print(lines)
    for i in range(0, len(file)):
   
                phrase=[file[i]]
    #            print(phrase)
                total_phrases += len(phrase)
                for ph in phrase:
    #                    print(ph_freq, "ph_freq")
                        ph_freq[ph] = ph_freq.get(ph,0) + 1
                        
                        
    print('Total phrases:',total_phrases)
    print('Total Unique phrases:',len(ph_freq))
    ph_prob = {k: v/total_phrases for k,v in ph_freq.items()}
                   

    try:
         os.mkdir("\\Step_4_Probability_new")  #create new folder in current directory
    except FileExistsError:
         pass
    with open("\\Step_4_Probability_new\\"+file1+"prob.json",'w') as f:
        json.dump(dict(sorted(ph_prob.items())), f, indent=4)
    return()
