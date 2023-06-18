if __name__ == '__main__':
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        score_list.append([name, score])

    # Sort the score list based on the second element (score)
    score_list.sort(key=lambda x: x[1])

    # Find the second lowest score
    second_lowest_score = sorted(set(score for _, score in score_list))[1]

    # Collect the names with the second lowest score
    second_lowest_names = sorted(
        [name for name, score in score_list if score == second_lowest_score])

    # Print the names in alphabetical order
    for name in second_lowest_names:
        print(name)
