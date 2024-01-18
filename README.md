**Event Detection in Online Social Networks**

The automated process of gleaning insights about the existence of perceptible happenings in colossal online social networking content is known as event detection. This repository contains source code files in python which are used in proposed approach for consolidation of content and context for event detection in OSN. Due to the restriction of Twitter only samll snippet of dataset is shared. A small description of source code files is mentioned below:

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Pre-requisite:**

Python 3.7+

spaCy

NLTK

Gensim 

NetworkX 

NLU (Natural Language Understanding)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Module_1_Temporal_Binning.py**

Temporal binning takes two consecutive one-hour interval tweets as input and outputs contextually similar consecutive bins. This source file will process a folder containing JSON files for each hour of the day.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Module_2_Features_Identification.py**

This module accepts tweets as input from a json file obtained from module 1 and outputs features extracted using NLU and spaCy. To obtain credentials in natural language understanding, one must first create an account.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Module_3_bursty_keyphrase_extraction.py** and **Module_3_part_keyphrase_prob_calculation.py**

Bursty keyphrases will be extracted with the help of seg prob file which contains the probability of every keyphrase with respect to the bin and seg prob file will be created with source file 'Module 3 part keyphrase prob calculation' which takes keyphrases from the previous module 'Feature identification'.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Module_4_graph_generation_and_MCL_clustering.py**

The previous module's bursty keyphrases will be transformed into a multi-attributed graph, and MCL clustering will be applied to the graph.
It uses all of the bursty keyphrases, as well as the folder containing all of the bins obtained in module 1, to train Word2Vec. As an output, event keys will be extracted.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Preprocessing.py**

Process of filtration of keyphrases collected from feature extraction section. Unigrams are removed during preprocessing because they do not contribute in essential information and and on top of that add to noise. Multi-gram phrases are more purposeful than single-gram phrases, which are often difficult to understand.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Event_keyphrases.py**

Finally, the top ten keyphrases for each event will be extracted using the bursty keyphrase score computed in module 3. It takes all keyphrases with the bursty score as input and returns the top ten keyphrases for each detected event.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
