#Aaron, Sam, Jake

import random

class GroupBuilder:
    def __init__(self, peopleList, groupSize):
        self.peopleList = peopleList
        self.groupSize = groupSize

    def divider(self, peopleList, groupSize):

        length = len(peopleList)
        shuffledPeople = random.shuffle(peopleList)

        extras = length % groupSize

