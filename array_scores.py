def main():
    n = int(input("Enter number of scores: "))
    scores = []

    for i in range(n):
        score = float(input(f"Enter score {i+1}: "))
        scores.append(score)

    total = sum(scores)
    average = total / n
    maximum = max(scores)
    minimum = min(scores)

    print("Scores:", scores)
    print("Sum of scores:", total)
    print("Average score:", average)
    print("Maximum score:", maximum)
    print("Minimum score:", minimum)


if __name__ == "__main__":
    main()

