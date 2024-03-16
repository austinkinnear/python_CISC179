import matplotlib.pyplot as plt

# Sample word frequencies dictionary for demonstration
# Replace this with your actual word frequency dictionary
word_freq_dict = {'the': 10, 'on': 5, 'and': 8}

# Generating the histogram
plt.figure(figsize=(10, 6))
plt.bar(word_freq_dict.keys(), word_freq_dict.values())
plt.xlabel('Word')
plt.ylabel('Frequency')
plt.title('Word Frequency Histogram')
plt.xticks(rotation=45)  # Rotate labels for better readability

# Show the histogram
plt.show()
