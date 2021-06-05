
def main():
    # 0. initialize variables
    my_grade = "unknown"

    # 1. input - get user input or from file or from web
    score_text = input("Enter score: ")   # get input as string
    score = int(score_text)   # convert to integer

    # 2. processing - massage the data / selection / repetition
    my_grade = calculate_grade(score)  # HD, C, D, P, F

    # 3. output - print your desired results
    print("Your grade is {}".format(my_grade))


def calculate_grade(score):
    if 80 <= score <= 100:
        grade = "HD"
    elif 70 <= score < 80:
        grade = "D"
    elif 60 <= score < 70:
        grade = "C"
    elif 50 <= score < 60:
        grade = "P"
    elif 0 <= score < 50:
        grade = "F"
    else:
        grade = "Invalid"
    return grade


main()  # run the main method