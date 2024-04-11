def word_stats():
    file = "C:\\Users\\austi\\OneDrive\\Desktop\\python_CISC179\\labs\\quiz\\quizWords.txt"

    with open(file) as file:
        content = file.read()
        # Splits the content of quizWords.txt into words based on whitespace
        words = content.split()
        total_words = len(words)
        total_length = sum(len(word) for word in words)
        #Calculates the average by taking the total length and dividing by the total words
        average_length = total_length / total_words if total_words > 0 else 0
        # Printed exactly how suggested for question 1
        print(f"Total words = {total_words}")
        print(f"Average length = {average_length}")
word_stats()
