# -*- coding: utf-8 -*-
"""

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




authenticator = IAMAuthenticator('xxxxxxxxxxxxxxxxxxxx') #CREDIDENTIALS WILL BE ADDED AFTER CREATING ACCOUNT ON NLU
natural_language_understanding = NaturalLanguageUnderstandingV1(version='date',authenticator=authenticator)
natural_language_understanding.set_service_url('')
from spacy.lang.en import English

def keywords(file):
    print("Inside keywords Function")

    keywords=[]

    n=1000

    
    x = list(divide_chunks(file, n))

    for p in range(0, len(x)):
      data=[]

      for j in range(0, len(x[p])):

          data.append(x[p][j]['text'])
      p=p+1
      data=('[{}]'.format(', '.join(data))).lower()

      
      keywords_inside=[]
      try:  
            response = natural_language_understanding.analyze(text= data, features=Features(keywords=KeywordsOptions(limit=200), syntax=SyntaxOptions(tokens=SyntaxOptionsTokens(lemma=True, part_of_speech=True)))).get_result()

            for r in response['keywords']:
             
             word= r['text']

             keywords_inside.append(word)

            keywords.extend(keywords_inside)
            print(len(keywords_inside))
         
      except:
             print("ApiException")    
      print(len(keywords), "---length of keywords")  

                
    return(keywords)

        
import spacy
nlp = spacy.load("en_core_web_sm")
def NERTag(file):

        print("Inside NERTag Function")
        POS=[] 
    
           
                
        
           
        pos_inside_list=[]           
   
   
          
        count=0
      
        for insidei in range(0,len(file)):

            tweeti=file[insidei]['text']
            tweeti=tweeti.lower()

            
            doc = nlp(tweeti)
            count=0
            POS_inside=[]
            for ent in doc.ents:
                            
                count+=1

                POS_inside.append(ent.text)

            pos_inside_list.extend(POS_inside)   

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

                for insidei in range(0,len(dirs)):
                    hashtagsi=mentionextraction(dirs[insidei])
                    if not hashtagsi:
                        continue
                    else:

                        vocab_of_a_folder.extend(hashtagsi)

                print(vocab_of_a_folder)
                return((vocab_of_a_folder))







def Hashtags(dirs): #return list of  hashtag vocab in one time period 
           print("Inside Hashtags Function")
           vocab_of_a_folder=[]
               
           for insidei in range(0,len(dirs)):

                hashtagsi=hashtagextraction(dirs[insidei])
                if not hashtagsi:
                    continue
                else:

                    vocab_of_a_folder.extend(hashtagsi)

           print(vocab_of_a_folder)
           return((vocab_of_a_folder))


import ast
def Ouput_Module_2(filename):
    print("Inside output module 2")
    try:
        os.mkdir("\\Step_2_Features_new") 
    except FileExistsError:
        pass
    full_filename = "%s/%s" % ('\\Step_1_New_intervals_with_extended_tweet', filename)   #FIRST TIME INTERVAL (FIRST JSON FILE)

    with open(full_filename,'r', encoding="utf-8") as fi:
        dicti = [json.loads(line) for line in fi]

    hashtag_list= Hashtags(dicti)

    mention_list= Mentions(dicti)
    keyword=keywords(dicti)

    NERTag_result=NERTag(dicti)

    
    file = open("\\Step_2_Features_new\\"+filename+"all_tokens.txt",'w', encoding= 'utf-8')

    Time_win_list1=list(set().union(hashtag_list, mention_list, keyword, NERTag_result))
    Time_win_list=(sorted(hashtag_list+mention_list+keyword+NERTag_result))
   
    for items in Time_win_list:
        file.write('%s\n' %items.lower())
    file1 = open("\\Step_2_Features_new\\"+filename+"sorted_tokens.txt",'w', encoding= 'utf-8')    
    for items1 in Time_win_list1:
        file1.write('%s\n' %items1.lower())
    print(full_filename, "done for filename")

    
    return()    

#print(Ouput_Module_2(0))       









