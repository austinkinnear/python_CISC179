from collections import Counter
import matplotlib.pyplot as plt

def generate_histogram():
    with open("labs/lab6-Text-Parsing/textParsin.txt", "r", encoding="utf-8") as file:
        words_list = [line.strip() for line in file]

    word_freq = Counter(words_list)

    plt.figure(figsize=(10, 6))
    plt.bar(word_freq.keys(), word_freq.values())
    plt.xlabel("Word")
    plt.ylabel("Frequency")
    plt.xticks(rotation=90)
    plt.title("Word Frequency Histogram")
    plt.tight_layout()
    plt.savefig("labs/lab6-Text-Parsing/histogram.png")
    plt.close()

if __name__ == "__main__":
    generate_histogram()
