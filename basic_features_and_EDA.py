""" 
    Basic features and EDA
    - Basic features
        - Number of words
        - Average length of words
        - Standard deviation of word length
        - Number of sentences
        - Average length of sentences
        - Standard deviation of sentence length
        - Number of paragraphs
        - Average length of paragraphs
        - Standard deviation of paragraph length
        - Total number of unique words
        - Measure of word repetition"""

# Import packages
import pandas as pd
import nltk

# Copied from data_load_explore [TODO - Find a way to call the function from data_load_explore]
def load_and_clean():
    """ Function that loads the data and removes observations where data has been incorrectly split across rows"""
    # File path
    file_path = 'ocr_data.xlsx'

    # Read excel file, add column names
    df = pd.read_excel(file_path, names=['excerpt','book_and_page','age'], usecols=[0, 1, 2], skiprows=[0])

    # Filters rows with non-integer values within the age row
    f_list = []
    for i, x in df['age'].iteritems():
        if isinstance(x, int) == True:
            f_list.append(i)

    # Filter for observations where age is an integer
    df_clean = df.loc[f_list]
    return df_clean

# Import data
df_clean = load_and_clean()

# Basic features

# Number of words - split on " "
df_clean['no_words'] = [len(item.split(" ")) for item in df_clean.excerpt]
#print(df_clean.no_words[0:20])

# Number of sentences - split on ".", 
def sentence_count(col):
    """ A function that iterates through a list, splits each element into sentences and counts the number of sentences in each row"""
    sentence_count_list = []
    # Iterates through each observation
    for obs in col:
        # Initialises a sentence count for each observation
        sentence_count = 0
        # Iterates through each sentence and adds to count
        for item in obs.split("."):
            if len(item) > 0:
                sentence_count += 1
        # Appends the sentence count to the sentence_count_list
        sentence_count_list.append(sentence_count)
    return sentence_count_list

df_clean['no_sentences'] = sentence_count(df_clean['excerpt'])
#print(df_clean['no_sentences'][0:20])

# Number of paragraphcs - split on "\n"

print(df_clean.excerpt[1000].split("\n"))

def para_count(col):
    """ A function that iterates through a list, splits each element into paragraphs and counts the number of paragraphs in each row"""
    para_count_list = []
    # Iterates through each observation
    for obs in col:
        # Initialises a paragraph count for each observation
        para_count = 0
        # Iterates through each paragraph and adds to count
        for item in obs.split("\n"):
            if len(item) > 0:
                para_count += 1
        # Appends the sentence count to the para_count_list
        para_count_list.append(para_count)
    return para_count_list

print(para_count(df_clean['excerpt']))