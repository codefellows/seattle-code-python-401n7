import nltk
import re

nltk.download("words", quiet=True)
nltk.download("names", quiet=True)

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()
# print(len(word_list))  # 236,736 words!
# print(name_list)

candidates = [
    "a Dark and Stormy Night",  # 100% English
    "n qnex naq fgbezl avtug",  # 0% English
    "j mjat jwm bcxavh wrpqc",
    "call me Ishmael",
    "Billy Pilgrim has become unstuck in time",
    "All happy families are alike; each unhappy family is unhappy in its own way.",
    '"Where\'s Papa going with that ax?" said Fern to her mother as they were setting the table for breakfast.',
    "Off the hizzle fo shizzle",
]


# For each string, I want to determine the *percentage* of words that are English words
def count_words(text):
    """
    Returns the number of valid (per corpus) English words in a string.
    :param text: String, representing a sentence of candidate words.
    :return: String, representing the percentage of English words
    """
    list_of_candidate_words = text.split()

    word_counter = 0

    for word in list_of_candidate_words:
        word = re.sub(r"[^A-Za-z]+", "", word)
        if word.lower() in word_list or word in name_list:
            word_counter += 1

    return f"There are {word_counter/len(list_of_candidate_words)*100}% English words in \"{text}\""


if __name__ == "__main__":
    for candidate in candidates:
        print(count_words(candidate))

