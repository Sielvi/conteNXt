# -*- coding: utf-8 -*-
"""


@author: Sielvie
"""

# -*- coding: utf-8 -*-

import csv
import pandas as pd
import numpy as np
from twython import Twython
import tweepy
import json
from collections import Counter
#from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re, string, unicodedata

import re
#from nltk.tokenize import TweetTokenizer
import spacy
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English
import en_core_web_sm
nlp = en_core_web_sm.load()

import string



# =============================================================================
#Remove puncuations
#Keep all hashtags
#Remove unigrams
# =============================================================================





stop=["0o", "0s", "3a", "3b", "3d", "6b", "6o", "a", "a1", "a2", "a3", "a4", "ab", "able", "about", "above", "abst", "ac", "accordance", "according", "accordingly", "across", "act", "actually", "ad", "added", "adj", "ae", "af", "affected", "affecting", "affects", "after", "afterwards", "ag", "again", "against", "ah", "ain", "ain't", "aj", "al", "all", "allow", "allows", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "amoungst", "amount", "an", "and", "announce", "another", "any", "anybody", "anyhow", "anymore", "anyone", "anything", "anyway", "anyways", "anywhere", "ao", "ap", "apart", "apparently", "appear", "appreciate", "appropriate", "approximately", "ar", "are", "aren", "arent", "aren't", "arise", "around", "as", "a's", "aside", "ask", "asking", "associated", "at", "au", "auth", "av", "available", "aw", "away", "awfully", "ax", "ay", "az", "b", "b1", "b2", "b3", "ba", "back", "bc", "bd", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "begin", "beginning", "beginnings", "begins", "behind", "being", "believe", "below", "beside", "besides", "best", "better", "between", "beyond", "bi", "bill", "biol", "bj", "bk", "bl", "bn", "both", "bottom", "bp", "br", "brief", "briefly", "bs", "bt", "bu", "but", "bx", "by", "c", "c1", "c2", "c3", "ca", "call", "came", "can", "cannot", "cant", "can't", "cause", "causes", "cc", "cd", "ce", "certain", "certainly", "cf", "cg", "ch", "changes", "ci", "cit", "cj", "cl", "clearly", "cm", "c'mon", "cn", "co", "com", "come", "comes", "con", "concerning", "consequently", "consider", "considering", "contain", "containing", "contains", "corresponding", "could", "couldn", "couldnt", "couldn't", "course", "cp", "cq", "cr", "cry", "cs", "c's", "ct", "cu", "currently", "cv", "cx", "cy", "cz", "d", "d2", "da", "date", "dc", "dd", "de", "definitely", "describe", "described", "despite", "detail", "df", "di", "did", "didn", "didn't", "different", "dj", "dk", "dl", "do", "does", "doesn", "doesn't", "doing", "don", "done", "don't", "down", "downwards", "dp", "dr", "ds", "dt", "du", "due", "during", "dx", "dy", "e", "e2", "e3", "ea", "each", "ec", "ed", "edu", "ee", "ef", "effect", "eg", "ei", "eight", "eighty", "either", "ej", "el", "eleven", "else", "elsewhere", "em", "empty", "en", "end", "ending", "enough", "entirely", "eo", "ep", "eq", "er", "es", "especially", "est", "et", "et-al", "etc", "eu", "ev", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "ey", "f", "f2", "fa", "far", "fc", "few", "ff", "fi", "fifteen", "fifth", "fify", "fill", "find", "fire", "first", "five", "fix", "fj", "fl", "fn", "fo", "followed", "following", "follows", "for", "former", "formerly", "forth", "forty", "found", "four", "fr", "from", "front", "fs", "ft", "fu", "full", "further", "furthermore", "fy", "g", "ga", "gave", "ge", "get", "gets", "getting", "gi", "give", "given", "gives", "giving", "gj", "gl", "go", "goes", "going", "gone", "got", "gotten", "gr", "greetings", "gs", "gy", "h", "h2", "h3", "had", "hadn", "hadn't", "happens", "hardly", "has", "hasn", "hasnt", "hasn't", "have", "haven", "haven't", "having", "he", "hed", "he'd", "he'll", "hello", "help", "hence", "her", "here", "hereafter", "hereby", "herein", "heres", "here's", "hereupon", "hers", "herself", "hes", "he's", "hh", "hi", "hid", "him", "himself", "his", "hither", "hj", "ho", "home", "hopefully", "how", "howbeit", "however", "how's", "hr", "hs", "http", "hu", "hundred", "hy", "i", "i2", "i3", "i4", "i6", "i7", "i8", "ia", "ib", "ibid", "ic", "id", "i'd", "ie", "if", "ig", "ignored", "ih", "ii", "ij", "il", "i'll", "im", "i'm", "immediate", "immediately", "importance", "important", "in", "inasmuch", "inc", "indeed", "index", "indicate", "indicated", "indicates", "information", "inner", "insofar", "instead", "interest", "into", "invention", "inward", "io", "ip", "iq", "ir", "is", "isn", "isn't", "it", "itd", "it'd", "it'll", "its", "it's", "itself", "iv", "i've", "ix", "iy", "iz", "j", "jj", "jr", "js", "jt", "ju", "just", "k", "ke", "keep", "keeps", "kept", "kg", "kj", "km", "know", "known", "knows", "ko", "l", "l2", "la", "largely", "last", "lately", "later", "latter", "latterly", "lb", "lc", "le", "least", "les", "less", "lest", "let", "lets", "let's", "lf", "like", "liked", "likely", "line", "little", "lj", "ll", "ll", "ln", "lo", "look", "looking", "looks", "los", "lr", "ls", "lt", "ltd", "m", "m2", "ma", "made", "mainly", "make", "makes", "many", "may", "maybe", "me", "mean", "means", "meantime", "meanwhile", "merely", "mg", "might", "mightn", "mightn't", "mill", "million", "mine", "miss", "ml", "mn", "mo", "more", "moreover", "most", "mostly", "move", "mr", "mrs", "ms", "mt", "mu", "much", "mug", "must", "mustn", "mustn't", "my", "myself", "n", "n2", "na", "name", "namely", "nay", "nc", "nd", "ne", "near", "nearly", "necessarily", "necessary", "need", "needn", "needn't", "needs", "neither", "never", "nevertheless", "new", "next", "ng", "ni", "nine", "ninety", "nj", "nl", "nn", "no", "nobody", "non", "none", "nonetheless", "noone", "nor", "normally", "nos", "not", "noted", "nothing", "novel", "now", "nowhere", "nr", "ns", "nt", "ny", "o", "oa", "ob", "obtain", "obtained", "obviously", "oc", "od", "of", "off", "often", "og", "oh", "oi", "oj", "ok", "okay", "ol", "old", "om", "omitted", "on", "once", "one", "ones", "only", "onto", "oo", "op", "oq", "or", "ord", "os", "ot", "other", "others", "otherwise", "ou", "ought", "our", "ours", "ourselves", "out", "outside", "over", "overall", "ow", "owing", "own", "ox", "oz", "p", "p1", "p2", "p3", "page", "pagecount", "pages", "par", "part", "particular", "particularly", "pas", "past", "pc", "pd", "pe", "per", "perhaps", "pf", "ph", "pi", "pj", "pk", "pl", "placed", "please", "plus", "pm", "pn", "po", "poorly", "possible", "possibly", "potentially", "pp", "pq", "pr", "predominantly", "present", "presumably", "previously", "primarily", "probably", "promptly", "proud", "provides", "ps", "pt", "pu", "put", "py", "q", "qj", "qu", "que", "quickly", "quite", "qv", "r", "r2", "ra", "ran", "rather", "rc", "rd", "re", "readily", "really", "reasonably", "recent", "recently", "ref", "refs", "regarding", "regardless", "regards", "related", "relatively", "research", "research-articl", "respectively", "resulted", "resulting", "results", "rf", "rh", "ri", "right", "rj", "rl", "rm", "rn", "ro", "rq", "rr", "rs", "rt", "ru", "run", "rv", "ry", "s", "s2", "sa", "said", "same", "saw", "say", "saying", "says", "sc", "sd", "se", "sec", "second", "secondly", "section", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sensible", "sent", "serious", "seriously", "seven", "several", "sf", "shall", "shan", "shan't", "she", "shed", "she'd", "she'll", "shes", "she's", "should", "shouldn", "shouldn't", "should've", "show", "showed", "shown", "showns", "shows", "si", "side", "significant", "significantly", "similar", "similarly", "since", "sincere", "six", "sixty", "sj", "sl", "slightly", "sm", "sn", "so", "some", "somebody", "somehow", "someone", "somethan", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "sp", "specifically", "specified", "specify", "specifying", "sq", "sr", "ss", "st", "still", "stop", "strongly", "sub", "substantially", "successfully", "such", "sufficiently", "suggest", "sup", "sure", "sy", "system", "sz", "t", "t1", "t2", "t3", "take", "taken", "taking", "tb", "tc", "td", "te", "tell", "ten", "tends", "tf", "th", "than", "thank", "thanks", "thanx", "that", "that'll", "thats", "that's", "that've", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "thered", "therefore", "therein", "there'll", "thereof", "therere", "theres", "there's", "thereto", "thereupon", "there've", "these", "they", "theyd", "they'd", "they'll", "theyre", "they're", "they've", "thickv", "thin", "think", "third", "this", "thorough", "thoroughly", "those", "thou", "though", "thoughh", "thousand", "three", "throug", "through", "throughout", "thru", "thus", "ti", "til", "tip", "tj", "tl", "tm", "tn", "to", "together", "too", "took", "top", "toward", "towards", "tp", "tq", "tr", "tried", "tries", "truly", "try", "trying", "ts", "t's", "tt", "tv", "twelve", "twenty", "twice", "two", "tx", "u", "u201d", "ue", "ui", "uj", "uk", "um", "un", "under", "unfortunately", "unless", "unlike", "unlikely", "until", "unto", "uo", "up", "upon", "ups", "ur", "us", "use", "used", "useful", "usefully", "usefulness", "uses", "using", "usually", "ut", "v", "va", "value", "various", "vd", "ve", "ve", "very", "via", "viz", "vj", "vo", "vol", "vols", "volumtype", "vq", "vs", "vt", "vu", "w", "wa", "want", "wants", "was", "wasn", "wasnt", "wasn't", "way", "we", "wed", "we'd", "welcome", "well", "we'll", "well-b", "went", "were", "we're", "weren", "werent", "weren't", "we've", "what", "whatever", "what'll", "whats", "what's", "when", "whence", "whenever", "when's", "where", "whereafter", "whereas", "whereby", "wherein", "wheres", "where's", "whereupon", "wherever", "whether", "which", "while", "whim", "whither", "who", "whod", "whoever", "whole", "who'll", "whom", "whomever", "whos", "who's", "whose", "why", "why's", "wi", "widely", "will", "willing", "wish", "with", "within", "without", "wo", "won", "wonder", "wont", "won't", "words", "world", "would", "wouldn", "wouldnt", "wouldn't", "www", "x", "x1", "x2", "x3", "xf", "xi", "xj", "xk", "xl", "xn", "xo", "xs", "xt", "xv", "xx", "y", "y2", "yes", "yet", "yj", "yl", "you", "youd", "you'd", "you'll", "your", "youre", "you're", "yours", "yourself", "yourselves", "you've", "yr", "ys", "yt", "z", "zero", "zi", "zz","dont"]






def Expand_Contractions(text):
    text = text.replace(" can't ", ' cannot ').replace("can't've ", ' cannot have ').replace("'cause ", ' because ').replace("ain't ", ' am not ')\
        .replace("could've ", ' could have ').replace("couldn't ", ' could not ').replace("couldn't've ", ' could not have ')\
        .replace("doesn't ", ' does not ').replace("don't ", ' do not ').replace("hadn't ", ' had not ').replace("hadn't've ", ' had not have ') \
        .replace("hasn't ", ' has not ').replace("haven't ", ' have not ').replace("he'd ", ' he would ').replace("he'd've ", ' he would have ') \
        .replace("he'll ", ' he will ').replace("he'll've ", ' he will have ').replace("he's ", ' he is ').replace("how'd ", ' how did ') \
        .replace("how'd'y ", ' how do you ').replace("how'll ", ' how will ').replace("how's ", ' how is ').replace("I'd ", ' I would ') \
        .replace("I'd've ", ' I would have ').replace("I'll ", ' I will ').replace("I'll've ", ' I will have ').replace("I'm ", ' I am ') \
        .replace("I've ", ' I have ').replace("isn't ", ' is not ').replace("it'd ", ' it had ').replace("it'd've ", ' it would have ') \
        .replace("it'll ", ' it will ').replace("it'll've ", ' it will have ').replace("it's ", ' it is ').replace("let's ", ' let us ') \
        .replace("ma'am ", ' madam ').replace("mayn't ", ' may not ').replace("might've ", ' might have ').replace("mightn't ", ' might not ') \
        .replace("mightn't've ", ' might not have ').replace("must've ", ' must have ').replace("might've ", ' might have ') \
        .replace("mustn't've ", ' must not have ').replace("needn't ", ' need not ').replace("needn't've ", ' need not have ') \
        .replace("oughtn't", ' ought not ').replace("oughtn't've ", ' ought not have').replace("shan't ", ' shall not ')\
        .replace("shan't've", ' shall not have ').replace("sha'n't've ", ' shall not have').replace("she'd ", ' she would ')\
        .replace("mustn't ", ' must not ').replace("aren't ", ' are not ').replace("o'clock ", ' of the clock ').replace("sha'n't ", ' shall not ') \
        .replace("she'd've ", ' she would have ').replace("she'd've ", ' she would have ').replace("o'clock ", ' of the clock ') \
        .replace("sha'n't ", ' shall not ').replace("she'll ", ' she will ').replace("she'll've ", ' she will have ').replace("she's ", ' she is ')\
        .replace("should've ", ' should have ').replace("shouldn't ", ' should not ').replace("shouldn't've ", ' should not have ')\
        .replace("so've ", ' so have ').replace("didn't ", ' did not ').replace("so's ", ' so is ').replace("that'd ", ' that would ')\
        .replace("that'd've ", ' that would have ').replace("that's ", ' that is ').replace("there'd ", ' there had ').replace("there's ", ' there is ')\
        .replace("there'd've ", ' there would have ').replace("they'd ", ' they would ').replace("they'd've ", ' they would have ')\
        .replace("they'll ", ' they will ').replace("they'll've ", ' they will have ').replace("they're ", ' they are ').replace("they've ", ' they have ')\
        .replace("to've ", ' to have ').replace("wasn't ", ' was not ').replace("we'd ", ' we had ').replace("we'd've ", ' we would have ')\
        .replace("we'll ", ' we will ').replace("we'll've ", ' we will have ').replace("we're ", ' we are ').replace("we've ", ' we have ')\
        .replace("weren't ", ' were not ').replace("what'll ", ' what will ').replace("what'll've ", ' what will have').replace("what're ", ' what are ')\
        .replace("what's ", ' what is ').replace("what've ", ' what have ').replace("when's ", ' when is').replace("when've ", ' when have ')\
        .replace("where'd ", ' where did ').replace("where's ", ' where is ').replace("where've ", ' where have').replace("who'll ", ' who will ')\
        .replace("who'll've ", ' who will have ').replace("who's ", ' who is ').replace("who've ", ' who have').replace("why's ", ' why is ')\
        .replace("why've ", ' why have ').replace("will've ", ' will have ').replace("won't ", ' will not ').replace("won't've ", ' will not have ')\
        .replace("would've ", ' would have ').replace("wouldn't ", ' would not ').replace("wouldn't've ", ' would not have').replace("'s ",' is ')\
        .replace("y'all ", ' you all ').replace("y'alls ", ' you alls ').replace("y'all'd ", ' you all would').replace("y'all'd've ", ' you all would have ')\
        .replace("y'all're ", ' you all are ').replace("y'all've ", ' you all have ').replace("you'd ", ' you had').replace("you'd've ", ' you would have ')\
        .replace("you'll ", ' you will ').replace("you'll've ", ' you will have ').replace("you're ", ' you are').replace("you've ", ' you have')\
    
    return text;


def Remove_Numbers(tweet):
    tweet = re.sub(r'[0-9]+', '', tweet)
    return tweet
# This function is to remove hex care
def Remove_Hexchar(preprocessed_tweet):
    return preprocessed_tweet.encode('ascii', errors='ignore')

def Remove_Extra_Whitespace(review):
    #return re.sub( '\s+', ' ', input).strip()
    #return Whitespace.sub(" ", input).strip()
    s=' '.join(review.split())
    return s

def Remove_Emojis(tweet):
    # Smile -- :), : ), :-), (:, ( :, (-:, :')
    tweet = re.sub(r'(:\s?\)|:-\)|\(\s?:|\(-:|:\'\))', ' ', tweet)
    # Laugh -- :D, : D, :-D, xD, x-D, XD, X-D
    tweet = re.sub(r'(:\s?D|:-D|x-?D|X-?D)', ' ', tweet)
    # Love -- <3, :*
    tweet = re.sub(r'(<3|:\*)', ' ', tweet)
    # Wink -- ;-), ;), ;-D, ;D, (;,  (-;
    tweet = re.sub(r'(;-?\)|;-?D|\(-?;)', ' ', tweet)
    # Sad -- :-(, : (, :(, ):, )-:
    tweet = re.sub(r'(:\s?\(|:-\(|\)\s?:|\)-:)', ' ', tweet)
    # Cry -- :,(, :'(, :"(
    tweet = re.sub(r'(:,\(|:\'\(|:"\()', ' ', tweet)
    return tweet

def Remove_All_Dots(tweet):
    tweet = re.sub(r'(?<!\d)\.(?!\d)', ' ', tweet)
    tweet = Remove_Extra_Whitespace(tweet)
    return tweet


#def Remove_wordlength_retweetnumber(tweet):
#    tweet=re.findall('\w+' , tweet)
#    if len(tweet)<4:
        
        
def Remove_exclamation_other_marks(tweet):
    tweet=tweet.replace('!', '')
    tweet=tweet.replace('?', '')
    tweet=tweet.replace('"', '')
    tweet=tweet.replace('_', '')
    tweet=tweet.replace('[', '')
    tweet=tweet.replace(']', '')
    tweet=tweet.replace('~', '')
    tweet=tweet.replace('\ ', '')
    tweet=tweet.replace('^', '')
    tweet=tweet.replace('|', '')
    tweet=tweet.replace('+', '')
    tweet=tweet.replace('{', '')
    tweet=tweet.replace('}', '')
    tweet=tweet.replace(' \ ', '')
    return tweet




def Remove_Ampersand(text):
    text = text.replace("&amp;", "&")
    text = text.replace("amp;", "&")
#    text = html.parser.unescape(text)
    return text

def ReplaceTwoOrMore(s):
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    #preprocessed_tweet = ''.join(''.join(s)[:2] for _, s in itertools.groupby(preprocessed_tweet))
    return  pattern.sub(r"\1\1", s)

#def Remove_Hexchar(preprocessed_tweet):
#    return preprocessed_tweet.decode('utf8').encode('ascii', errors='ignore')

def Remove_charaters(tweet):
    #Convert @username with space
    tweet=re.sub('\ |\,|\`|\\|\/|\&|\*|\'|\;|\(|\)|\:|\/|\=|\-|\%|\$', ' ', tweet)    
##    tweet = re.sub(r'[a-zA-Z0-9]*', '', tweet)
    return tweet 

import time
import preprocessor as p1
filtered_sentence_final=[]


count=0

import os
def preprocessing(file): 
    try:
         os.mkdir("\\Step_3_Preprocessed_Features_new")  #create new folder in current directory
    except FileExistsError:
         pass
    with open("\\Step_2_Features_new\\"+file+"sorted_tokens.txt", 'r', encoding="utf-8") as handle:
         phrases = [line.rstrip('\n') for line in handle]
    print(len(phrases), "--length of phrases")

    print("----file", file)
    count=0
    final_phrases=[]  
    for line in phrases:
              count+=1

              tweet= line
 
              url_1 = re.findall(r'(https?://\S+)', tweet)
              url = ",".join(str(x) for x in url_1)
              tweet= re.sub(r'(https?://\S+)',"",tweet)
              tweet = Expand_Contractions(tweet)
              tweet = Remove_Numbers(tweet)
              tweet = Remove_Hexchar(tweet)
              tweet=tweet.decode()
              tweet = Remove_Extra_Whitespace(tweet)
              tweet = Remove_Emojis(tweet)
              tweet = Remove_All_Dots(tweet)
              tweet = Remove_Ampersand(tweet)
              tweet = ReplaceTwoOrMore(tweet)
              tweet = Remove_charaters(tweet)
              tweet = Remove_exclamation_other_marks(tweet)
              tweet=p1.clean(tweet)
              
             
             
              
              if (len(tweet.split())==2):
                   length=list(map(len, tweet.split()))
                   if (any(x < 4 for x in length)):
                      continue
                   if (any(word in tweet.split() for word in stop)):
                       continue
                      
                  
              map(len, tweet.split())  
              length=list(map(len, tweet.split()))
              if (all(x < 5 for x in length)):
                      continue
                  
                  
              tweet= tweet.split()  
              middle_phrase=[]
              for j in range(0, len(tweet)):
    #            print(j, "j", phrase[j])
                
                
                if tweet[j].startswith('#'):
                       middle_phrase.append(tweet[j])
               
                else:
                       
                        middle_phrase.append(tweet[j])
            
        
              
                  
    
            
              middle_phrase=' '.join(middle_phrase)
              if (len(middle_phrase)<6 ):
                       continue 
              if ((len(middle_phrase.split()))==1):
                  continue
                
                    
              final_phrases.append(middle_phrase)
#              count+=1
#              print(len(final_phrases))
              
              
             
    print("first preprocesing done")
    phrases_list=[]
#    print(final_phrases)
    for items in final_phrases:
     
         phrases_list.append(p1.clean(items)) 
    print("second preprocesing done")
    phrases_add={}  
    for item in phrases_list:
         phrases_count = phrases_list.count(item)
         phrases_add[item]=phrases_count
    print("third preprocesing done")
    phrases_count=[]
#    for key, value in phrases_add.items():
#       
#             phrases_count.append(key)
#        
    print("final preprocesing done")   
    
#    cwd = os.getcwd()
   
    file1 = open("\\Step_2_Features_new\\"+file+"_counting_phrases_including_unigrams_new.txt",'w', encoding= 'utf-8')    
    for items1 in phrases_add:
        if items1!= "":
            file1.write('%s\n' %items1)  
        else:
            continue           
              
    file1.close() 
    return()
