# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 23:52:28 2022

@author: sielv
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 17:48:15 2022

@author: Sielvie
"""

#import json
#import os
#import math
#import csv
#folder = os.listdir( '4_timewindows' )
#
#def bursty_keywords(file):
#    CD_full_filename = "%s/%s" % ('4_timewindows', file)
#    tweet_count= sum(1 for line in open(CD_full_filename))
#    phrases=[]
#    with open(CD_full_filename, "r") as f:
#         data = f.read()
##    print("opening csv")
#    with open(CD_full_filename,'r') as fi:
#        dict_tweetsi = [json.loads(line) for line in fi]
#    with open('4_timewindows\\09_hour.csv','r') as src:
#           reader = csv.reader(src)
#           for row in reader:
#               phrases.extend(row[0].split(","))
##    print(phrases)
#    print("entering into for")   
#    for i in range(0, len(phrases)):
#        print(phrases[i].replace("'", ""), "---phrase")
#        
#        tweet_freq=data.count(phrases[i])
#        user_set = set()
#        retweet_count = 0 
#        followers_count = 0 
#        print(tweet_freq)
#        phrases[i]=phrases[i].replace("'", "")
#        for j in range(0, tweet_count):
#            for word in range(0, len(phrases[i]. split())):
#                all_words=[]
#                print((phrases[i].split()), type(phrases[i]))
#                print((phrases[i].split()[word]), "-----yes it is there")
#                print(dict_tweetsi[j]['text'], "dictionary")
#                if phrases[i].split()[word] in dict_tweetsi[j]['text']:
#                   
#                    all_words.append(phrases[i].split()[word])
#                print( all_words, "all_words")
##                print(dict_tweetsi[j]['text'], "dictionary of file")
##                if (len(all_words))== (len(dict_tweetsi[j]['text'])):
##
##                    print("yes")
##                    
##                    retweet_count+=  dict_tweetsi[j]['retweet_count']
##                    print(retweet_count, "retweet_count")
##                    followers_count+=dict_tweetsi[j]['user']['followers_count']
##                    print(followers_count, "followers_count")
#                
#            
##                user_set=user_set.union(dict_tweetsi[j]['user']['id'])
##        user_count = len(user_set)
#    print(i)     
#    return(tweet_count)
#    
#    
#bursty_keywords('09_hour.json')


import json
import os
import math
import csv
from collections import OrderedDict
#folder = os.listdir( '0_features_forcombinedfiles' )
#from pytrends.request import TrendReq
import json
#pytrends = TrendReq(hl='en-US', tz=360, timeout=(5,10))
from textblob import TextBlob


class BurstySegmentExtractor():
    """
    Extract top k segments based on burst weight of the segment in a given TimeWindow class object 
    for a segment, BurstyWeight = BurstProbability x log(user_freq) x log(retweet_count) x log(follower_count)
    """
    def __init__(self, file, use_retweet_count=True, use_followers_count=True, default_seg_prob=0.000001):
        """
        seg_prob_file: file containing expected probability of a segment to be used in a tweet
        use_retweet_count: whether to use retweet counts of tweet containing the segment to calculate bursty weight (default=True)
        use_followers_count: whether to use followers count of user using the segment to calculate bursty weight (deafult=True)
        seg_prob of a newly found segment is assumed to default_seg_prob (deafult - 0.000001)
        """
        print('Initializing BurstySegmentExtractor')
        
        with open("D:\\DATASETS\\16_09_2020\\Step_4_Probability_new\\"+file+"prob.json",'r') as f:  #you need to calculate his with the help of segment_prob_calc or segment_prob_calc_notepad program
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
#        f=open("features_2\\segment_after_ner.txt", 'w', encoding='utf-8 ')
#        print(file)
        CD_full_filename = "%s/%s" % ('D:\\DATASETS\\16_09_2020\\Step_1_New_intervals_with_extended_tweet', file)
#        tweet_count= sum(1 for line in open(CD_full_filename))
      
        final_phrases={}
        phrases=[]
        
#        with open(CD_full_filename, "r") as f:
#             data = f.read()
    #    print("opening csv")
        with open(CD_full_filename,'r', encoding="utf-8") as fi:
            dict_tweetsi = [json.loads(line) for line in fi]
            
        tweet_count=len(dict_tweetsi)
        k = int(math.sqrt(tweet_count))
        with open("D:\\DATASETS\\16_09_2020\\Step_3_Preprocessed_Features_new\\"+file+"_counting_phrases_including_unigrams_new.txt",'r', encoding='utf-8') as src:
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
#            a_string_lowercase =  phrases[i].lower()
#            contains_letters = a_string_lowercase.islower()
#            if contains_letters== True:
#            print( phrases[i], "--phrase list")
#            print(tweet_freq, "--tweet frequency")
            user_id=[]
            tweet_freq=0
            found=[]
#            print(i, "iii")
#            print(phrases[i], "-------outside j --------------phrase")
#            print( tweet_freq, "tweet frequency before")
            for j in range(0, tweet_count):
    #            print( phrases[i].split(), "--phrase list")
    #            print(dict_tweetsi[j]['text'].split(),"dictionary" )
    #            print( dict_tweetsi[j]['text'].split(), "dict")
#                check = all(item in  (dict_tweetsi[j]['text'].split()) for item in (phrases[i].split() ))
##                
#                    print(j, "j")
                text=dict_tweetsi[j]['text']
                hashtags=hashtagextraction(dict_tweetsi[j])
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
                mentions=mentionextraction(dict_tweetsi[j])
                if not mentions:
                    mentions=""
                else:
                    mentions=((convert(mentions)))
                    
                # if (not dict_tweetsi[j]['entities']['user_mentions']):
                #         mentions=''
                # else:
                #      mentions=((dict_tweetsi[j]['entities']['user_mentions'][0]['name']))
                
                
                   
                final= text+ ' '+hashtags+' '+mentions
                    
                final=final.strip()
            #        if j==80:
##                print(final, "---final")
##                print(hashtags, "---hashtags", mentions, "---mentions")
                final=final.lower()
                if (final.find(phrases[i])!=-1):
                    
                    
##                    print(phrase, "phrase")
                    tweet_freq+=1
                    found.append(j)
#                    print((tweet_freq), "tweet_freq inside")
                    user_id.append(dict_tweetsi[j]['user']['id'])
#                    print(len(user_id), "count of users inside")
                    retweet_count+=  dict_tweetsi[j]['retweet_count']
#                    print(dict_tweetsi[j]['retweet_count'], "retweet_count inside")
                    
                    followers_count+=dict_tweetsi[j]['user']['followers_count']
                
#                    print(followers_count, "followers_count inside")
                else:
#                    print("continue")
                    continue
                    
#                print(retweet_count, "retweet count")
#                print(followers_count, "follower count")
    #                    print(j, "jj")
        #                break
    #            print("out of loop")
#            print(phrases[i], "phrases[i]")
#            print((tweet_freq), "tweet_freq")
#           
#            print((retweet_count), "  retweet_count")
#            print((followers_count), "  followers_count")
#            print(i, "i", len(phrases), "--total num of phrases")
            
#            print(found, "--found in these")
#                print((phrases[i] ), "---------phrase file")
#            print(tweet_freq, "tweet_freq outside")
            user_set = user_set.union(user_id)    
#            print((user_set), "  user_set")
            user_count = len(user_set)
#            print(phrases[i], "after solving j")
            prob = self.seg_prob.get(phrases[i],self.default_seg_prob) # new segment
            print(prob)
            seg_mean = tweet_count * prob
#            print(seg_mean, "---seg mean")
            seg_std_dev = math.sqrt(tweet_count * prob * (1 - prob))
#            print(seg_std_dev, "----seg deviation")
            bursty_score = self.sigmoid(10 * (tweet_freq - seg_mean - seg_std_dev)/(seg_std_dev)) * math.log10(1+user_count)
#            print(bursty_score, "bursty_score1")
            if retweet_count>0:
               # print(use_retweet_count, "selfff")
                bursty_score *= math.log10(1+retweet_count)
#                print(bursty_score, "bursty_score2")
            if followers_count>0:
                bursty_score *= math.log10(1 + math.log10(1 + followers_count))
#                print(bursty_score, "bursty_score3")
#            print(bursty_score, "final bursty score")
#            print(phrases[i], "phrases[i]")
            final_phrases[phrases[i]]=bursty_score
#            print(bursty_score, "bursty score")
#            final_phrases.append((phrases[i], bursty_score))    
#            print((final_phrases), "type of final phrases")
            
#            print('Total Segments:',len(phrases))
#            print('final phrase:',final_phrases)
#        for it in range(0, len( final_phrases)):
#            if it>183:
#                continue
#            else:
#                print(((final_phrases[it].key()), "----final phrases"))
        sort_orders = sorted(final_phrases.items(), key=lambda x: x[1], reverse=True)[:k]
#        print(sort_orders, type(sort_orders))
#        print("next", i)
        try:
          os.mkdir("D:\\DATASETS\\16_09_2020\\Step_5_Bursty_segments_new")  #create new folder in current directory
        except FileExistsError:
            pass
        file1=open("D:\\DATASETS\\16_09_2020\\Step_5_Bursty_segments_new\\"+file+"segments", "w", encoding="utf-8")
#        final_output=[]
        for item in sort_orders:
             file1.write(str(item[0])+' ')
             file1.write(str(item[1]))
             file1.write("\n")
#            final_output.append(item[0])
#            final_output.append(item[1])
            
#        for items1 in final_output:
#           file1.write('%s\n' %items1)
#            print(item)
#            print(item[0])
##            p=item[0]
#            q=item[1]
#            file1.write(str(p))
#            file1.write("\t")
#            file1.write((q))
#            file1.write("\n")
#                print(item[0], item[1])
#                file1.write(str(item[0]).lower())
#                file1.write("\t")
#                file1.write(str(item[1]))
#                file1.write(str("\n"))

    
    

    
    
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


# =============================================================================
# 
#for combining notepad files



# import os
# 
# filename_list=os.listdir(r"C:\\Users\\Sielvie\\.spyder-py3\\Dec21\\Experiment\\Modules\\all_day_tokens_with_repeatition")
# print (filename_list)
# 
# 
# with open("12-10-2012_all_segments_with_repeatition.txt", "w", encoding="utf-8") as outfile:
#     for filename in filename_list:
#         with open("all_day_tokens_with_repeatition"+"\\"+filename, encoding="utf-8") as infile:
#             contents = infile.read()
#             outfile.write(contents)
# 
# 
# =============================================================================





# =============================================================================
# for combining json files







# import os
# import json
# filename_list=os.listdir(r"C:\\Users\\Sielvie\\.spyder-py3\\Dec21\\Experiment\\Modules\\4_timewindows")
# print (filename_list)
# 
# result = list()
# for f1 in filename_list:
#     print(f1, "f1")
#     with open("4_timewindows"+"\\"+f1, 'r') as infile:
#         result.extend([json.loads(line) for line in infile])
# 
#     
# with open('Json_file_12_10_2012.json', 'w', encoding="utf-8") as f:
#  for i in range(0, len(result)):
#     f.write(str(result[i]))
#     f.write('\n')
# 
# 
# =============================================================================



































