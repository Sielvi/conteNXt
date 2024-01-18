# -*- coding: utf-8 -*-
"""


@author: sielvie
"""

# -*- coding: utf-8 -*-



import json
import os
import math
import csv
from collections import OrderedDict
import json
from textblob import TextBlob


class BurstySegmentExtractor():
    """
    Extract top k keyphrases based on burst weight of the keyphrase in a given bin
    for a keyphrase, BurstyWeight = BurstProbability x log(user_freq) x log(retweet_count) x log(follower_count)
    """
    def __init__(self, file, use_retweet_count=True, use_followers_count=True, default_seg_prob=0.000001):
        """
        seg_prob_file: file containing expected probability of a keyphrase to be used in a tweet
        use_retweet_count: whether to use retweet counts of tweet containing the keyphrase to calculate bursty weight (default=True)
        use_followers_count: whether to use followers count of user using the keyphrase to calculate bursty weight (deafult=True)
        seg_prob of a newly found keyphrase is assumed to default_seg_prob (deafult - 0.000001)
        """
        print('Initializing BurstySegmentExtractor')
        
        with open("\\Step_4_Probability_new\\"+file+"prob.json",'r') as f:  #you need to calculate his with the help of segment_prob_calc or segment_prob_calc_notepad program
            self.seg_prob = json.load(f)
        
        self.use_retweet_count = use_retweet_count
       
        self.use_followers_count = use_followers_count
        self.default_seg_prob = default_seg_prob
        
        print('BurstySegmentExtractor Ready')
    
    def bursty_keywords(self,file):
        import re
        import ast
        def is_ascii(s):
           try:
               s.encode(encoding='utf-8').decode('ascii')
           except UnicodeDecodeError:
              return False
           else:
                 return True

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

        CD_full_filename = "%s/%s" % ('\\Step_1_New_intervals_with_extended_tweet', file)

      
        final_phrases={}
        phrases=[]
        

        with open(CD_full_filename,'r', encoding="utf-8") as fi:
            dict_tweetsi = [json.loads(line) for line in fi]
            
        tweet_count=len(dict_tweetsi)
        k = int(math.sqrt(tweet_count))
        with open("\\Step_3_Preprocessed_Features_new\\"+file+"_counting_phrases_including_unigrams_new.txt",'r', encoding='utf-8') as src:
            phrases = [line.rstrip('\n') for line in src]
#        print(phrases)
        print("entering into for")   
        for i in range(0, len(phrases)):
            print(i, "--------------------------------------phrase", phrases[i])
            
#            tweet_freq=data.count(phrases[i].replace("'", ""))
            user_set = set()
            retweet_count = 0 
            followers_count = 0 
#            print((phrases[i] ), "---------phrase file upper")
            phrases[i]=phrases[i].replace("'", "")
            phrases[i]=phrases[i].lower()          
            user_id=[]
            tweet_freq=0
            found=[]

            for j in range(0, tweet_count):

                text=dict_tweetsi[j]['text']
                hashtags=hashtagextraction(dict_tweetsi[j])
                if not hashtags:
                        hashtags=""
                else:
                        hashtags=((convert(hashtags)))

                mentions=mentionextraction(dict_tweetsi[j])
                if not mentions:
                    mentions=""
                else:
                    mentions=((convert(mentions)))
                    

                   
                final= text+ ' '+hashtags+' '+mentions
                    
                final=final.strip()

                final=final.lower()
                if (final.find(phrases[i])!=-1):
                    
                    

                    tweet_freq+=1
                    found.append(j)

                    user_id.append(dict_tweetsi[j]['user']['id'])

                    retweet_count+=  dict_tweetsi[j]['retweet_count']

                    
                    followers_count+=dict_tweetsi[j]['user']['followers_count']
                

                else:
#                    print("continue")
                    continue
                    

            user_set = user_set.union(user_id)    

            user_count = len(user_set)

            prob = self.seg_prob.get(phrases[i],self.default_seg_prob) # new segment
            print(prob)
            seg_mean = tweet_count * prob

            seg_std_dev = math.sqrt(tweet_count * prob * (1 - prob))

            bursty_score = self.sigmoid(10 * (tweet_freq - seg_mean - seg_std_dev)/(seg_std_dev)) * math.log10(1+user_count)

            if retweet_count>0:
              
                bursty_score *= math.log10(1+retweet_count)

            if followers_count>0:
                bursty_score *= math.log10(1 + math.log10(1 + followers_count))

            final_phrases[phrases[i]]=bursty_score

        sort_orders = sorted(final_phrases.items(), key=lambda x: x[1], reverse=True)[:k]

        try:
          os.mkdir("\\Step_5_Bursty_segments_new")  #create new folder in current directory
        except FileExistsError:
            pass
        file1=open("\\Step_5_Bursty_segments_new\\"+file+"segments", "w", encoding="utf-8")
#        final_output=[]
        for item in sort_orders:
             file1.write(str(item[0])+' ')
             file1.write(str(item[1]))
             file1.write("\n")


    
    

    
    
    def sigmoid(self, x):
            try:
                return 1/(1+(math.exp(-x)))
            except:
                print('SIGMOID ERROR:', x)
                return 0
        
 

##print(bursty_keywords('09_hour.json'))
#file= '13_14_15_16_17_18_19.json_counting_phrases_including_unigrams_1'
#print(file)
#BurstySegmentExtractor().bursty_keywords(file)



































