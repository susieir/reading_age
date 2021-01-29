""" 
    Basic features and EDA
    - Basic features
        - Number of words
        - Average length of words
        - Standard deviation of word length
        - Number of sentences
        - Average length of sentences
        - Standard deviation of sentence length
        - Number of paragraphs - no paragraphs in the dataset - may be how the data has been read?
        - Average length of paragraphs  - no paragraphs in the dataset - may be how the data has been read?
        - Standard deviation of paragraph length - no paragraphs in the dataset - may be how the data has been read?
        - Total number of unique words
        - Measure of word repetition"""

# Import packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

""" Basic Features """
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

# Average word length

def avg_word_len():
    """ A function that creates a list of average word lengths for each observation"""
    avg_word_len_list = []
    for obs in df_clean.excerpt:
        avg_word_len = sum([len(word) for word in obs.split(" ")]) / \
            len(obs.split(" "))
        avg_word_len_list.append(avg_word_len)
    return avg_word_len_list

df_clean['avg_word_len'] = avg_word_len()

# Standard deviation of word length

def std_word_len():
    """ A function that create a list of the standard deviation of word lengths for each observation"""
    std_word_len_list = []
    for obs in df_clean.excerpt:
        std_word_len = np.std([len(word) for word in obs.split(" ")])
        std_word_len_list.append(std_word_len)
    return std_word_len_list

df_clean['std_word_len'] = std_word_len()

""" EDA """
"""# Age profile
age_profile = df_clean.age.value_counts().sort_index()
age_profile_norm = df_clean.age.value_counts(normalize = True).sort_index()

# Graph - non normalised
#age_profile.plot()
#plt.xlabel("Age")
#plt.ylabel("Frequency")
#plt.show()

# Graph - normalised
#age_profile_norm.plot()
#plt.xlabel("Age")
#plt.ylabel("Percentage")
#plt.show()

# How is the distribution centred
print("The mean age is {:.1f}".format(df_clean.age.mean()))
print("The median age is {}".format(df_clean.age.median()))

# How many observations are there where age > 15
no_books_over_15 = df_clean.age[df_clean.age > 15].count()
print("There are {} books with a reading age of more than 15".format(no_books_over_15))
# What proportion of observations have age > 15
prop_books_over_15 = no_books_over_15 / len(df_clean.age)
print("{:.1%} of observations have a reading age over 15".format(prop_books_over_15))


# Number of words
words_profile = df_clean.no_words.value_counts().sort_index()
words_profile_norm = df_clean.no_words.value_counts(normalize = True).sort_index()

# Graph - non normalised
#words_profile.plot()
#plt.xlabel("Number of words")
#plt.ylabel("Frequency")
#plt.show()

# Graph - normalised
words_profile_norm.plot()
plt.xlabel("Number of words")
plt.ylabel("Percentage")
plt.show()


# How is the distribution centred
print("The mean number of words is {:.1f}".format(df_clean.no_words.mean()))
print("The median number of words is {}".format(df_clean.no_words.median()))


# How many observations are there where no_words > 100
no_words_over_100 = df_clean.no_words[df_clean.no_words > 100].count()
print("There are {} books with more than 100 words on a page".format(no_words_over_100))
# What proportion of observations have no_words > 100
prop_words_over_100 = no_words_over_100 / len(df_clean.no_words)
print("{:.1%} of observations have more than 100 words on a page".format(prop_words_over_100))"""