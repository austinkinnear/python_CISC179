import re

# Using file path to open and read the story
file_path = "C:/Users/austi/OneDrive/Desktop/python_CISC179/labs/lab6-Text-Parsing/Story-1.txt"
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Counts both words and characters
words_list = text.split()
word_count_list = len(words_list)
char_count_list = len(''.join(words_list))
print(f"List: {word_count_list} words, {char_count_list} characters")

# Uses a dictionary to count each word
word_freq_dict = {word: words_list.count(word) for word in set(words_list)}
char_count_dict = sum([len(word) for word in word_freq_dict])
print(f"Dictionary: {len(word_freq_dict)} unique words, {char_count_dict} characters from unique words")

# Regex is used for formats for phone numbers and emails 
phone_regex = re.compile(r'\b\d{3}-\d{3}-\d{4}\b')
email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
phones = phone_regex.findall(text)
emails = email_regex.findall(text)
print(f"Phones: {phones}")
print(f"Emails: {emails}")

# Email modification to be the @hotmail
modified_emails = [email.split('@')[0] + '@hotmail.com' for email in emails]
print(f"Modified Emails: {modified_emails}")
