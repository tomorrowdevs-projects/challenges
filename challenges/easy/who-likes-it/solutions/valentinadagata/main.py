def likes(people):
    peopleLength = len(people)
    # initialize the final sentence
    sentence = ""

    # if there are 0 or 1 people the verb will be at the third person with final s
    third_person = ""
    if peopleLength <= 1:
        third_person = "s"

    # starting the sentence
    if peopleLength == 0:
        sentence += "no one"
    else:
        sentence += people[0]

    # second part of the sentence
    if peopleLength > 2:
        sentence += ", "
        sentence += people[1]

    # if there are 2 or more people add "and"
    if peopleLength >= 2:
        sentence += " and "
        # add the last people or counting how many others
        if peopleLength > 3:
            sentence += str(peopleLength - 2) + " others"
        else:
            sentence += people[peopleLength - 1]

    # final part of the sentence, with or without s
    sentence += " like" + third_person + " this"

    return sentence

if __name__ == '__main__':
    print(likes(["Alex", "Max", "Jacob", "Mark", "Peter"]))
    """
    likes [] -- must be "no one likes this"
    likes ["Peter"] -- must be "Peter likes this"
    likes ["Jacob", "Alex"] -- must be "Jacob and Alex like this"
    likes ["Max", "John", "Mark"] -- must be "Max, John and Mark like this"
    likes ["Alex", "Jacob", "Mark", "Max"] -- must be "Alex, Jacob and 2 others like this"
    """