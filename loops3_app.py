
def main():
    scores_list = []
    is_exit = False

    while not is_exit:
        score_text = input("Enter score: ")
        score = int(score_text)
        if 0 <= score <= 100:
            scores_list.append(score)
        print("  -- Number of scores entered: {}".format(len(scores_list)))
        choice = input("Continue (Y/N)? ").lower()
        if choice == "n":
            is_exit = True
        else:
            print("Invalid choice!")

    if len(scores_list) > 0:
        print("Total: {}".format(sum(scores_list)))
    else:
        print("No scores entered!")

main()