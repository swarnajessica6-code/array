def main():
    n = int(input("Enter number of scores: "))
    scores = []

    for i in range(n):
        score = float(input(f"Enter score {i+1}: "))
        scores.append(score)

    total = sum(scores)
    average = total / n

    print("Scores:", scores)
    print("Sum of scores:", total)
    print("Average score:", average)


if __name__ == "__main__":
    main()
