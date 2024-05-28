import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns
from collections import Counter

import unicodedata

def meaningful_word(word):
    for c in word:
        if not ('\u4e00' <= c <= '\u9fff'):
            return False

    return True

def plot_keyword_frequency(segmented_results):
    words = [word for result in segmented_results for word in result]
    words = filter(meaningful_word, words)
    keyword_counts = Counter(words)
    most_common_keywords = keyword_counts.most_common()

    most_common_keywords = most_common_keywords[:30]
    print(most_common_keywords)
    keywords, frequencies = zip(*most_common_keywords)
    plt.figure(figsize=(10, 6))
    sns.set_style("whitegrid",{"font.sans-serif":['Taipei Sans TC Beta']})
    sns.barplot(x=list(frequencies), y=list(keywords), palette="viridis")
    plt.xlabel("Frequency")
    plt.ylabel("Keywords")
    plt.title("Top Keywords Frequency")
    plt.savefig('keyword_frequency.png')