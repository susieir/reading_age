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
import seaborn as sns

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

##############################################################################################################################
#### EDA - Univariate
##############################################################################################################################

#### Age 
# Age profile
age_profile = df_clean.age.value_counts().sort_index()
age_profile_norm = df_clean.age.value_counts(normalize = True).sort_index()

age_range = age_profile.index.to_list()
print("There are {} unique ages included within the dataset".format(len(age_range)))
print("The age variable ranges from {min} to {max}".format(min = min(age_range), max = max(age_range)))

# Graph - non normalised
#age_profile.plot()
#plt.xlabel("Age")
#plt.ylabel("No observations")
#plt.title("Age by no observations")
#plt.show()

# Graph - normalised
#age_profile_norm.plot()
#plt.xlabel("Age")
#plt.ylabel("Percentage")
#plt.title("Normalised distribution of ages")
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



#### Number of words
words_profile = df_clean.no_words.value_counts().sort_index()
words_profile_norm = df_clean.no_words.value_counts(normalize = True).sort_index()

# Graph - non normalised
#words_profile.plot()
#plt.xlabel("Number of words")
#plt.ylabel("Frequency")
#plt.title("Number of words by number of observations")
#plt.show()

# Graph - normalised
#words_profile_norm.plot()
#plt.xlabel("Number of words")
#plt.ylabel("Percentage")
#plt.title("Frequency of number of words")
#plt.show()

# How is the distribution centred
print("The mean number of words is {:.1f}".format(df_clean.no_words.mean()))
print("The median number of words is {}".format(df_clean.no_words.median()))

# How many observations are there where no_words > 100
no_words_over_100 = df_clean.no_words[df_clean.no_words > 100].count()
print("There are {} books with more than 100 words on a page".format(no_words_over_100))
# What proportion of observations have no_words > 100
prop_words_over_100 = no_words_over_100 / len(df_clean.no_words)
print("{:.1%} of observations have more than 100 words on a page".format(prop_words_over_100))



#### Number of sentences
sentences_profile = df_clean.no_sentences.value_counts().sort_index()
sentences_profile_norm = df_clean.no_sentences.value_counts(normalize = True).sort_index()

# Graph - non normalised
#sentences_profile.plot()
#plt.xlabel("Number of sentences")
#plt.ylabel("Number of occurrences")
#plt.title("Number of sentences by number of observations")
#plt.show()

# Graph - normalised
#sentences_profile_norm.plot()
#plt.xlabel("Number of sentences")
#plt.ylabel("Percentage")
#plt.title("Frequency of number of sentences")
#plt.show()

# How is the distribution centred
print("The mean number of sentences is {:.1f}".format(df_clean.no_sentences.mean()))
print("The median number of sentences is {}".format(df_clean.no_sentences.median()))

# How many observations are there where no_sentences > 10
no_sentences_over_10 = df_clean.no_sentences[df_clean.no_sentences > 10].count()
print("There are {} books with more than 10 sentences on a page".format(no_sentences_over_10))
# What proportion of observations have no_sentences > 10
prop_sentences_over_10 = no_sentences_over_10 / len(df_clean.no_sentences)
print("{:.1%} of observations have more than 10 sentences on a page".format(prop_sentences_over_10))



#### Average word length
word_len_profile = df_clean.avg_word_len.value_counts().sort_index()
word_len_profile_norm = df_clean.avg_word_len.value_counts(normalize = True).sort_index()

# Graph - non normalised
#word_len_profile.plot()
#plt.xlabel("Average word length")
#plt.ylabel("Number of occurrences")
#plt.title("Frequency of average word length")
#plt.show()

# Graph - normalised
#word_len_profile_norm.plot()
#plt.xlabel("Average word length")
#plt.ylabel("Percentage")
#plt.title("Distribution of average word length")
#plt.show()

# How is the distribution centred
print("The mean of the distribution of average word length is {:.1f}".format(df_clean.avg_word_len.mean()))
print("The median of the distribution of average word length is {:.2f}".format(df_clean.avg_word_len.median()))

# How many observations are there where average word length > 6
avg_word_len_over_6 = df_clean.avg_word_len[df_clean.avg_word_len > 6].count()
print("There are {} books with average word length of more than 6".format(avg_word_len_over_6))
# What proportion of observations where average word length > 6
prop_word_len_over_6 = avg_word_len_over_6 / len(df_clean.avg_word_len)
print("{:.1%} of observations have an average word length of more than 6".format(prop_word_len_over_6))




#### Standard deviation of word length
std_word_len_profile = df_clean.std_word_len.value_counts().sort_index()
std_word_len_profile_norm = df_clean.std_word_len.value_counts(normalize = True).sort_index()

# Graph - non normalised
#std_word_len_profile.plot()
#plt.xlabel("Standard deviation of word length")
#plt.ylabel("Number of occurrences")
#plt.title("Frequency of standard deviation of word length")
#plt.show()

# Graph - normalised
#std_word_len_profile_norm.plot()
#plt.xlabel("Standard deviation of word length")
#plt.ylabel("Percentage")
#plt.title("Distribution of standard deviation of word length")
#plt.show()

# How is the distribution centred
print("The mean of the distribution of standard deviation of word length is {:.1f}".format(df_clean.std_word_len.mean()))
print("The median of the distribution of standard deviation of word length is {:.2f}".format(df_clean.std_word_len.median()))

##############################################################################################################################
#### EDA - Multivariate
##############################################################################################################################

#### Age vs. number of words
#sns.relplot(x = 'no_words', y = 'age', data = df_clean, alpha = 0.4)
#plt.xscale('log')
#plt.show()

#### Age vs. number of sentences
#sns.relplot(x = 'no_sentences', y = 'age', data = df_clean, alpha = 0.2)
#plt.xscale('log')
#plt.show()

#### Age vs. average word length
#sns.relplot(x = 'avg_word_len', y = 'age', data = df_clean, alpha = 0.2)
#plt.title("Age vs. average word length")
#plt.show()

#### Age vs. std of word length
#sns.relplot(x = 'std_word_len', y = 'age', data = df_clean, alpha = 0.2)
#plt.xscale('log')
#plt.title("Age vs. std of word length")
#plt.show()

