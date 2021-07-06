"""
Start Date: 26/05/2020
Last Modified Date: 05/06/2020

Code Outcome: The Patient class inherits the Person class tto use the methods of Person class, then we run the required
simulation on the given values of days, meeting probability and patients zero health. The result of this task returns a
list of affected people per day which is used further in Task 2.
"""

from reading_population import Person  # importing Person class from task 1
import random  # importing random function

"""
Patient class with inherited Person class which returns Person's object list and with 7 methods defined to be 
used in run_simulation function.
"""


class Patient(Person):
    # initial function of the class Patient
    def __init__(self, first_name, last_name, health):
        super().__init__(first_name, last_name)
        self.person_health = health
        self.list_Friends = []

    # method overwriting of add_friend method from Task 1
    def add_friend(self, friend_person):
        list_friend_person = dict1[friend_person]
        self.list_Friends.append(list_friend_person)

    # method to get health of Person object
    def get_health(self):
        return self.person_health

    #  method to set new health on Person Object
    def set_health(self, new_health):
        self.person_health = new_health

    # method to check if Person object is contagious or not
    def is_contagious(self):
        if self.person_health < 50:
            return True
        else:
            return False

    # method to infect Person with viral load
    def infect(self, viral_load):
        if self.person_health >= 50:
            self.person_health = self.person_health - (2 * viral_load)  # health calculation after being affected
        elif 29 < self.person_health < 50:
            self.person_health = self.person_health - (1 * viral_load)  # health calculation after being affected
        elif self.person_health <= 29:
            self.person_health = self.person_health - (0.1 * viral_load)  # health calculation after being affected
        if self.person_health < 0:
            self.person_health = 0

    # method to add health points when sleeping at the end of the day
    def sleep(self):
        self.person_health = self.person_health + 5
        if self.person_health > 100:  # setting maximum health to 100
            self.person_health = 100
            return self.person_health
        else:
            return self.person_health


"""
run_simulation function for viral spread between people objects and friends object.
"""


def run_simulation(days, meeting_probability, patient_zero_health):
    people = load_patients(75)  # storing returned Person objects list in people variable and setting their health to 75
    people[0].set_health(patient_zero_health)  # setting health of patient zero
    no_of_affected = []
    for day in range(days):
        count = 0

        for person in people:  # for loop to fetch person from people list
            for friend in person.get_friends():  # for loop to get friends list for each person
                random_probability = random.random()  # random no. generation
                if random_probability <= meeting_probability:  # checking meeting probability

                    if person.is_contagious():  # checking for contagious in people
                        viral_load = 5 + ((person.get_health() - 25) ** 2) / 62  # calculating viral load by person
                        friend.infect(viral_load)
                    if friend.is_contagious():  # checking for contagious in friends
                        viral_load = 5 + ((friend.get_health() - 25) ** 2) / 62  # calculating viral load by friend
                        person.infect(viral_load)

        for person in people:
            if person.is_contagious():
                count += 1  # counting number of affected person
            person.sleep()  # making all person sleep at day end
        no_of_affected.append(count)  # list creation of no. Of affected people per day
    return no_of_affected  # returning list of no. of affected people per day


"""
# load_people function to create Person's object and return a list of Person's objects.
"""


# using similar code from task 1 to load patients
def load_patients(default_health):
    num_lines = sum(1 for line in open("a2_sample_set.txt"))  # calculating number of rows to iterate
    reading_file = open("a2_sample_set.txt", 'r')  # reading from source file

    # three empty list
    objects_list = []
    first_name_list = []
    list_of_lists = []

    for names in range(num_lines):
        readPerson = reading_file.readline()
        y = 1
        person_name = []
        for val in readPerson:  # for loop to fetch Person's name from the list
            if val != ':':
                person_name.append(val)
                y = y + 1
            else:
                break

        first_name = ''
        first_name = first_name.join(person_name)
        first_name_list.append(first_name)  # list of Person's names
        first_name0 = first_name.split()
        friends_name = ((readPerson[y + 1:-1]).split(', '))  # list of friends
        list_of_lists.append(friends_name)  # creation of list for Person’s in txt file
        first_name = Patient(first_name0[0], first_name0[1], default_health)  # listof Person and setting default health
        objects_list.append(first_name)
    reading_file.close()

    global dict1
    dict1 = dict(zip(first_name_list, objects_list))  # dictionary creation of Person’s name list and objects of person
    dict2 = dict(zip(objects_list, list_of_lists))  # dictionary creation of objects of person list and list of friends

    """
    1. Iterating on values in objects_list
    2. Iterating on each value of objects_list and fetching values of keys in dict2
    3. Iterating on fetched values of dict2 and using them on add.friend method 
    4. Converting the friends name into objects in add.friend method 
    """
    # for loop for maping values in the Person class method and returns Person’s object list
    for object_ in objects_list:
        for name in dict2.get(object_):
            object_.add_friend(name)
    return objects_list  # resulting Person's object list


if __name__ == '__main__':  # main function to define the flow and run code
    run_simulation(40, 1, 1)
    # sample output:
    # [19, 82, 146, 181, 196, 199, 200, 200, 200, 200, 200, 200, 200, 200,
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200,
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
