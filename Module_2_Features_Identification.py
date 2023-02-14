# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 19:19:24 2022

@author: Sielvie
"""

import os 
import json
#import spacy
from random import sample
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, CategoriesOptions, KeywordsOptions, SyntaxOptions, SyntaxOptionsTokens
#from Module_1_Temporal_Binning import FinalCalculation


def divide_chunks(l, n):
      
    # looping till length l
    for i in range(0, len(l), n): 
        yield l[i:i + n]




def is_ascii(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True




authenticator = IAMAuthenticator('viFjPvn82FYhWTGh9sMHHCyl0D7GiDVF7Y89b0wjV3xV')
natural_language_understanding = NaturalLanguageUnderstandingV1(version='2021-08-01',authenticator=authenticator)
natural_language_understanding.set_service_url('https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/0b416a2c-d5c8-46be-ab67-ad41830b1fae')
from spacy.lang.en import English
#folder = os.listdir( '0_features_forcombinedfiles' ) #FOLDER IN THE DIRECTORY WITH MULTIPLE JSON FILES
#print(len(folder))
#nlp = English()
#nlp = spacy.load('en_core_web_sm')
def keywords(file):
    print("Inside keywords Function")
#    tweets_first_interval = []
#    CD_full_filename = "%s/%s" % ('4_timewindows', file)   #FIRST TIME INTERVAL (FIRST JSON FILE)
    keywords=[]
#    file = open("keywords_feature1.txt",'w', encoding= 'utf-8')   
#    with open(CD_full_filename,'r') as fi:
#        dict_tweetsi = [json.loads(line) for line in fi]
#        print(type(dict_tweetsi))
    n=1000
#        count=0
    
    x = list(divide_chunks(file, n))
#        print(x)
    for p in range(0, len(x)):
      data=[]
#          keywords=[]
      for j in range(0, len(x[p])):
#              print(x[p][j]['Tweet Text'])
          data.append(x[p][j]['text'])
      p=p+1
      data=('[{}]'.format(', '.join(data))).lower()
#          print(len(data))
#          print(data)
      
      keywords_inside=[]
      try:  
            response = natural_language_understanding.analyze(text= data, features=Features(keywords=KeywordsOptions(limit=200), syntax=SyntaxOptions(tokens=SyntaxOptionsTokens(lemma=True, part_of_speech=True)))).get_result()
#                print(json.dumps(response, indent=2))
            for r in response['keywords']:
             
             word= r['text']
#                 print (word,"keyword")
#                 score=r['relevance']
#                 print (score,"score")
             keywords_inside.append(word)
#             print(word, "keyword")
            keywords.extend(keywords_inside)
            print(len(keywords_inside))
         
#                 print(json.dumps(response, indent=2))}
#                valid_keywords=['NOUN', 'PRON' ,'ADJ']
#                for r in response ["syntax"]['tokens']:
#                    
#                    word1= r['text']
##                    print (word1,"word")
#                    pos=r['part_of_speech']
##                    print (pos,"part_of_speech")
#                    if pos in valid_keywords:
#                        POS_inside.append(word1)
#                    else:
#                        print("next")
##                print(POS_inside)
#                POS.extend(POS_inside)
#                print("ApiException")
      except:
             print("ApiException")    
      print(len(keywords), "---length of keywords")  
#          file.write(str(keywords))#line to uncomment
#          file.write("\n") #line to uncomment
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
#    file.write
#    file.write(str(keywords))
#    file.write("\n")
        
#            print(json.dumps(response, indent=2))
#            
#            print("next")
#        count=count+1
#        print("count----", count)
#    print(len(keywords))
    return(keywords)
#            tweets_first_interval.append(tweeti)
#    tweets_first_interval=('[{}]'.format(', '.join(tweets_first_interval[:100]))) #to remove single quotes from strings in a list
#    print(tweets_first_interval)
#    response = natural_language_understanding.analyze(text= tweets_first_interval, features=Features(keywords=KeywordsOptions()), language='en').get_result()
#    for r in response['keywords']:
#             word= r['text']
#             print (word,"keyword")
#             score=r['relevance']
#             print (score,"score")
#    return()

#keywords_POSTag("2012_Costa_Rica_earthquake-tweets_labeled.json")


#
#def POSTag(file):
##    tweets_first_interval = []
#        print("Inside POSTag Function")
#        POS=[] 
#    
#    # creating a csv writer object 
##            
#                
#        
#           
#        pos_inside_list=[]           
#   
##    file = open("NERrtag.txt",'w', encoding= 'utf-8')       
##    with open(CD_full_filename,'r') as fi:
##        dict_tweetsi = [json.loads(line) for line in fi]
#        
#          
#        count=0
#      
#        for insidei in range(0,len(file)):
##            pos_inside_list=[]     
##            print(insidei)
#           tweeti=file[insidei]['text']
#           tweeti=tweeti.lower()
##            print(tweeti, "---tweet")
#            
#           
##            valid_keywords=['NN', 'NNP', 'NNS', 'NNPS']
##            print(type(tweeti))
##            tokens=nlp(tweeti) 
##            print(tokens)
##            print(tokens, "tokens")
##            tokens=tokens.lower()
#           POS_inside=[] 
#           valid_keywords=['NN', 'NNP', 'NNS', 'NNPS']
##            print(type(tweeti))
#           tokens=nlp(tweeti) 
##            print(tokens)
##            print(tokens, "tokens")
##            tokens=tokens.lower()
#           for token in tokens:
##                print (token,"token")
#                count+=1
#                if token.tag_ in valid_keywords :
##                    print ((token.text),"VALID", token.tag_)
#                    POS_inside.append(token.text) #stemword(noun and adjective)
#                else:
#                        print("next")
#           pos_inside_list.extend(POS_inside)   
#           print(count, "---count")    
#            
##            print(insidei, "outer side")
##            file.write(str(pos_inside_list))
##            file.write("\n")
##            print(pos_inside_list)
###            POS_inside =(" ".join(POS_inside))
###            for token in tokens:
####                print (token,"token")
###                if token.tag_ in valid_keywords :
###                    print ((token.text),"VALID", token.tag_)
###                    POS_inside.append(token.text) #stemword(noun and adjective)
###                else:
###                        print("next")
###            
###            POS_inside =(" ".join(POS_inside))
###            print([POS_inside], "----POSINSIDE")
###        print(POS_inside)
###            POS.extend(POS_inside)
###        print(pos_inside_list)
###            
##    print(pos_inside_list) 
##    print(len(pos_inside_list))
#        return(pos_inside_list)
#        
        
        
import spacy
nlp = spacy.load("en_core_web_sm")
def NERTag(file):
#    tweets_first_interval = []
        print("Inside NERTag Function")
    #    CD_full_filename = "%s/%s" % ('4_timewindows', file)   #FIRST TIME INTERVAL (FIRST JSON FILE)
        POS=[] 
    
    # creating a csv writer object 
#            
                
        
           
        pos_inside_list=[]           
   
#    file = open("NERrtag.txt",'w', encoding= 'utf-8')       
#    with open(CD_full_filename,'r') as fi:
#        dict_tweetsi = [json.loads(line) for line in fi]
        
          
        count=0
      
        for insidei in range(0,len(file)):
#            pos_inside_list=[]     
#            print(insidei, "inside NERTag")
            tweeti=file[insidei]['text']
            tweeti=tweeti.lower()
#            print(tweeti, "---tweet")
            
           
#            valid_keywords=['NN', 'NNP', 'NNS', 'NNPS']
#            print(type(tweeti))
#            tokens=nlp(tweeti) 
#            print(tokens)
#            print(tokens, "tokens")
#            tokens=tokens.lower()
            
            doc = nlp(tweeti)
            count=0
            POS_inside=[]
            for ent in doc.ents:
                            
                count+=1
#                print(ent.text)
                POS_inside.append(ent.text)
#                POS_inside[ent.text]= ent.label_
#                print(POS_inside, "ner tagging")
            pos_inside_list.extend(POS_inside)   
#            print(count, "---count")    
            
#            print(insidei, "outer side")
#            file.write(str(pos_inside_list))
#            file.write("\n")
#            print(pos_inside_list)
##            POS_inside =(" ".join(POS_inside))
##            for token in tokens:
###                print (token,"token")
##                if token.tag_ in valid_keywords :
##                    print ((token.text),"VALID", token.tag_)
##                    POS_inside.append(token.text) #stemword(noun and adjective)
##                else:
##                        print("next")
##            
##            POS_inside =(" ".join(POS_inside))
##            print([POS_inside], "----POSINSIDE")
##        print(POS_inside)
##            POS.extend(POS_inside)
##        print(pos_inside_list)
##            
#    print(pos_inside_list) 
#    print(len(pos_inside_list))
        return(pos_inside_list)




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
                hasht=[]
                for i in range(0, len(dicti1['extended_tweet']['entities']['user_mentions'])):
                        hashtag=(dicti1['extended_tweet']['entities']['user_mentions'][i]['name'].lower())
                        if is_ascii(hashtag)==False:
                            continue
                        else:
                            hasht.append(hashtag)
                return(hasht)       
        except:
                hasht=[]
                for i in range(0, len(dicti1['entities']['user_mentions'])):
                        hashtag=(dicti1['entities']['user_mentions'][i]['name'].lower())
                        if is_ascii(hashtag)==False:
                            continue
                        else:
                            hasht.append(hashtag)
                return(hasht)


import emoji

def remove_emoji(text): #removing graphical emojis
    return (emoji.get_emoji_regexp().sub(u'', text).lstrip())
def Mentions(dirs): #return list of  hashtag vocab in one time period 
                print("Inside Mentions Function")
                vocab_of_a_folder=[]
#        full_filename = "%s/%s" % ('4_timewindows', dirs)   #FIRST TIME INTERVAL (FIRST JSON FILE)
#        with open(full_filename,'r') as fi:
#                dicti = [json.loads(line) for line in fi]
                
                for insidei in range(0,len(dirs)):
                    hashtagsi=mentionextraction(dirs[insidei])
                    if not hashtagsi:
                        continue
                    else:
#                        mentions=remove_emoji(str(hashtagsi['user_mentions']))
#                        print(mentions, "mentions")
                        vocab_of_a_folder.extend(hashtagsi)
#        vocab_of_a_folder.append(alldictsi)
#        print(len(vocab_of_a_folder))
#        print(type(vocab_of_a_folder))
#        print("NEXT")
                print(vocab_of_a_folder)
                return((vocab_of_a_folder))


#Mentions("09_hour.json")




def Hashtags(dirs): #return list of  hashtag vocab in one time period 
           print("Inside Hashtags Function")
           vocab_of_a_folder=[]
#        full_filename = "%s/%s" % ('4_timewindows', dirs)   #FIRST TIME INTERVAL (FIRST JSON FILE)
#        with open(full_filename,'r') as fi:
#                dicti = [json.loads(line) for line in fi]
                
           for insidei in range(0,len(dirs)):
#                print(insidei, "Inside Hashtags Function")
                hashtagsi=hashtagextraction(dirs[insidei])
                if not hashtagsi:
                    continue
                else:
#                    print(hashtagsi['hashtags'], "hashtags")
                    vocab_of_a_folder.extend(hashtagsi)
#                        print(vocab_of_a_folder)
#                        for i in (hashtagsi['hashtags']):
#                            print(i.lower())
#        vocab_of_a_folder.append(alldictsi)
#        print(len(vocab_of_a_folder))
#        print(type(vocab_of_a_folder))
#        print("NEXT")
           print(vocab_of_a_folder)
           return((vocab_of_a_folder))


import ast
def Ouput_Module_2(filename):
    print("yayyyyyyyyyyyyyyyyyy")
    try:
        os.mkdir("D:\\DATASETS\\16_09_2020\\Step_2_Features_new") 
    except FileExistsError:
        pass
    full_filename = "%s/%s" % ('D:\\DATASETS\\16_09_2020\\Step_1_New_intervals_with_extended_tweet', filename)   #FIRST TIME INTERVAL (FIRST JSON FILE)
#    tweet_count= sum(1 for line in open(full_filename))
#    print("okay")
    with open(full_filename,'r', encoding="utf-8") as fi:
        dicti = [json.loads(line) for line in fi]
#    for i in range(i_value, len(folder)):
#    print("not okay")
    hashtag_list= Hashtags(dicti)
#        print(hashtag_list)
    mention_list= Mentions(dicti)
    keyword=keywords(dicti)
#        print(keyword)
#        POSTag1=POSTag(folder[i])
    NERTag_result=NERTag(dicti)
#    with open(full_filename,'r') as fi:
#            dict_tweetsi = [json.loads(line) for line in fi]
#    CD_full_filename = "%s/%s" % ('4_timewindows', file)
    
    file = open("D:\\DATASETS\\16_09_2020\\Step_2_Features_new\\"+filename+"all_tokens.txt",'w', encoding= 'utf-8')
#        filename = "posttag_keywords.csv"
#        with open(filename, 'w', encoding="utf-8") as csvfile: 
#            csvwriter = csv.writer(csvfile)
#        
#            csvwriter.writerow(NERTag_result)
#            csvwriter.writerow(keyword)
    Time_win_list1=list(set().union(hashtag_list, mention_list, keyword, NERTag_result))
    Time_win_list=(sorted(hashtag_list+mention_list+keyword+NERTag_result))
   
    for items in Time_win_list:
        file.write('%s\n' %items.lower())
    file1 = open("D:\\DATASETS\\16_09_2020\\Step_2_Features_new\\"+filename+"sorted_tokens.txt",'w', encoding= 'utf-8')    
    for items1 in Time_win_list1:
        file1.write('%s\n' %items1.lower())
    print(full_filename, "done for filename")
#        print(items)
#        tweet_freq=0
#        for j in range(0, tweet_count):
#             if items in dict_tweetsi[j]:
#    #                    print(j, "jj")
#    #                    print((phrases[i] ), "---------phrase file")
#                        tweet_freq+=1
#                        file.write('%s\n' %items)
#                        file.write(str(tweet_freq))
#            file.write("\n")
#        file.write(str(Time_win_list))
#        file.write("\n")
#        file.write(str(Posttag))
#        file.write("\n")
#        file.write(str(hashtag_list))
#        file.write("\n")
##        file.write(str(mention_list))
#        file.write("\n")
#        file.write(str(Time_win_list))
#        file.close()
#    print(keyword_postlist)
#    i+=1
#        print(i, "down")
    
    return()    

#print(Ouput_Module_2(0))       









