"""
Replace the contents of this module docstring with your own details
Name:
Date started:
GitHub URL:
"""
import random

NAMEINDEX = 0
COUNTRYINDEX = 1
PRIORITYINDEX = 2
VISITORNOTINDEX = 3


def displayMenu():
    """
    display a menu
    """
    print('Menu:')
    print('L - List places')
    print('R - Recommend random place')
    print('A - Add new place')
    print('M - Mark a place as visited')
    print('Q - Quit')


def sortPlace(placeList):
    """
    sort the placeList
    The list will be sorted by visited status then by priority (decreasing number)
    :param placeList: place list
    :return: sorted place list
    """
    visitList = []
    noVisitList = []
    # traverse the placeList
    for place in placeList:
        # has visit
        if place[VISITORNOTINDEX] == 'v':
            # add place to visitList
            visitList.append(place)
        # not has visit
        if place[VISITORNOTINDEX] == 'n':
            # add place to noVisitList
            noVisitList.append(place)
    # sort the visitList
    visitList.sort(key=lambda x: x[PRIORITYINDEX])
    # sort the noVisitList
    noVisitList.sort(key=lambda x: x[PRIORITYINDEX])
    # merge the visitList and noVisitList
    noVisitList.extend(visitList)
    return noVisitList


def displayPlaceList(placeList):
    """
    display the place list
    :param placeList:  place list
    """
    countNoVisit = 0
    # traverse the placeList
    for i in range(len(placeList)):
        place = placeList[i]
        name = place[NAMEINDEX]
        country = place[COUNTRYINDEX]
        priority = place[PRIORITYINDEX]
        visitOrNot = place[VISITORNOTINDEX]
        # display the visit place information with no *
        if place[VISITORNOTINDEX] == 'v':
            print(' {}. {:<10}in {:<13}{:>3}'.format(i + 1, name, country, priority, visitOrNot))
        # display the unvisited places information with *
        if place[VISITORNOTINDEX] == 'n':
            print('*{}. {:<10}in {:<13}{:>3}'.format(i + 1, name, country, priority, visitOrNot))
            countNoVisit += 1
    if countNoVisit == 0:
        print('{} places. No places left to visit. Why not add a new place?'.format(len(placeList)))
    else:
        print('{} places. You still want to visit {} places.'.format(len(placeList), countNoVisit))


def recommendPlace(placeList):
    """

    :param placeList:  place list
    :return: random recommend place
    """
    print('Not sure where to visit next?')
    recommendList = [place for place in placeList if place[VISITORNOTINDEX] == 'n']
    # random choose an unvisited place from recommendList
    randomPlace = random.choice(recommendList)
    print('How about... {} in {}?'.format(randomPlace[NAMEINDEX], randomPlace[COUNTRYINDEX]))


def getGenericInput(inputHint):
    """
    You should be able to use generic, customisable functions to perform input with error checking
    (e.g., getting the place name and country can reuse the same function).
    :param inputHint:
    :return:
    """
    blankHint = 'Input can not be blank'
    while (True):
        inputStr = input(inputHint + ': ')
        # error input
        if (inputStr == ''):
            print(blankHint)
        else:
            return inputStr


def countNoVisit(placeList):
    """

    :param placeList: place list
    :return: count the
    """
    result = [1 if place[VISITORNOTINDEX] == 'n' else 0 for place in placeList]
    return sum(result)


def readFile(FILENAME):
    """
    read places from file name
    :param FILENAME: file name
    :return: placeList
    """
    placeList = []
    # load the places.csv to placeList
    with open(FILENAME) as f:
        line = f.readline().strip()
        # read line
        while (line):
            name = line.split(',')[NAMEINDEX]
            country = line.split(',')[COUNTRYINDEX]
            # str -> int
            priority = int(line.split(',')[PRIORITYINDEX])
            visitOrNot = line.split(',')[VISITORNOTINDEX]
            # add to placeList
            placeList.append([name, country, priority, visitOrNot])
            # read line
            line = f.readline().strip()
    return placeList


def writeToFile(FILENAME, placeList):
    """
    write placeList information to FILENAME
    :param FILENAME: file name
    :param placeList: place list
    :return:
    """
    with open(FILENAME, mode='w') as f:
        for place in placeList:
            name = place[NAMEINDEX]
            country = place[COUNTRYINDEX]
            # int -> str
            priority = str(place[PRIORITYINDEX])
            visitOrNot = place[VISITORNOTINDEX]
            f.write(','.join([name, country, priority, visitOrNot]) + '\n')
    print('{} places saved to places.csv'.format(len(placeList)))
    print('Have a nice day :)')


def markPlaceVisit(placeList):
    """

    :param placeList:
    :return:
    """
    print('Enter the number of a place to mark as visited')
    while True:
        try:
            index = int(input('>>> '))
            # error checking
            if index <= 0:
                print('Number must be > 0')
            elif index > len(placeList):
                print('Invalid place number')
            # already visited
            elif (placeList[index - 1][VISITORNOTINDEX] == 'v'):
                print('You have already visited {}'.format(placeList[index - 1][NAMEINDEX]))
                break
            else:
                # mark as visited
                placeList[index - 1][VISITORNOTINDEX] = 'v'
                print('{} in {} visited!'.format(placeList[index - 1][NAMEINDEX],
                                                 placeList[index - 1][COUNTRYINDEX]))
                break
        # ValueError: the input string is not a number
        except ValueError as e:
            print('Invalid input;', end='')
            print(' enter a valid number')
    return placeList


# You should be able to use generic, customisable functions to perform input with
# error checking (e.g., getting the place name and country can reuse the same function).
def main():
    # display a welcome message with my name
    print("Travel Tracker 1.0 - by yeyanjun")
    FILENAME = 'places.csv'
    # initial the place list to empty list
    placeList = readFile(FILENAME)
    placeList = sortPlace(placeList)

    # print the hint when load csv file successfully
    print('{} places loaded from places.csv'.format(len(placeList)))

    while True:
        displayMenu()
        userInputMenuChoice = input('>>> ').lower()
        validInput = ['l', 'r', 'a', 'm', 'q']
        # error-check user inputs as demonstrated in the sample output
        # not valid menu choice
        if userInputMenuChoice not in validInput:
            print('Invalid menu choice')
        else:
            # valid menu choice
            # quit the system and save placeList to places.csv file
            if userInputMenuChoice == 'q':
                writeToFile(FILENAME, placeList)
                break
            # recommend place from the placeList
            elif (userInputMenuChoice == 'r'):
                if countNoVisit(placeList) == 0:
                    print('No places left to visit!')
                else:
                    recommendPlace(placeList)
                    # list the place
            elif (userInputMenuChoice == 'l'):
                displayPlaceList(placeList)
            # add new place to placeList
            elif (userInputMenuChoice == 'a'):
                name = getGenericInput('Name')
                country = getGenericInput('Country')
                priority = int(input('Priority: '))
                print('{} in {} (priority {}) added to Travel Tracker'.format(name, country, priority))
                placeList.append([name, country, priority, 'n'])
                placeList = sortPlace(placeList)
            # mark the place
            elif (userInputMenuChoice == 'm'):
                # count unVisit num
                countNoVisitNum = countNoVisit(placeList)
                # No unvisited places left
                if countNoVisitNum == 0:
                    print('No unvisited places')
                else:
                    # display the place list
                    displayPlaceList(placeList)
                if countNoVisitNum != 0:
                    # mark the place as visited
                    placeList = markPlaceVisit(placeList)
                    placeList = sortPlace(placeList)


if __name__ == '__main__':
    main()
