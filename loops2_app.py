

def main():
    # count = 0                - prime loop
    # while count < 5:         - while condition
    #     print(count)               do your statements
    #     count = count + 1          statement to update condition

    scores_list = []     # empty list

    score_text = input("Enter score (-ve to exit): ")
    score = int(score_text)    # convert to integer
    

    while score >= 0:       # as long as score is +ve
        scores_list.append(score)        # add the score to the list
        print("  -- Number of scores entered: {}".format(len(scores_list)))  # inform user
        score_text = input("Enter score (-ve to exit): ")
        score = int(score_text)    # convert to integer

    if len(scores_list) > 0:
        total = sum(scores_list)
        maximum = max(scores_list)
        minimum = min(scores_list)
        average = total / len(scores_list)
        print("Total score: {}".format(total))
        print("Max: {}, Min: {}".format(maximum, minimum))
        print("Average: {}".format(average))
    else:
        print("You did not enter any scores!")




main()