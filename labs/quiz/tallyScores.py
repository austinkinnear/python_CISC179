def tally_scores():
    file = "C:\\Users\\austi\\OneDrive\\Desktop\\python_CISC179\\labs\\quiz\\studentRecords.txt"

    with open(file) as file:
        for line in file:
            # Split the line into name and scores
            parts = line.strip().split()
            name = parts[0]
            # Convert score strings to integers
            scores = list(map(int, parts[1:]))
            #Same calculation logic as question 1 of the quiz
            average = sum(scores) / len(scores)
            print(f"{name}: {' '.join(map(str, scores))}")
            print(f"average = {average}")
tally_scores()
