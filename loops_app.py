
def main():
    # for i in range(5):
    #     print("#" * i)

    avengers = ["hulk", "groot", "thor", "dr strange", "captain marvel",
                "black Widow", "captain America", "wanda", "vision", "winter soldier",
                "black panther", "ant man", "spider-man", "the wasp", "gamora", "hawkeye",
                "iron man", "war machine"]

    # for hero in avengers:
    #     print(hero)
    avengers.sort(key=len)  # sort based on length method

    print("===== Total Avengers: {} ======".format(len(avengers)))
    for index, hero in enumerate(avengers):   # index starts from 0
        print("{:2}) {} - {} characters".format(index+1, hero.title(), len(hero)))


main()