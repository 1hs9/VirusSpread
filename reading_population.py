"""
Name: Harshit Shamra
Student ID: 31272215
Start Date:20/05/2020
Last Modified Date:25/05/2020
Code Outcome: The main aim of this task is to generated objects for each person in the list and map them with their
friend's object. The result of this task returns a list of Persons's object which is further used in Task 2.
"""


"""
Person class with 4 methods defined to perform simulation in load_people function
"""


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.list_Friends = []

    # method to add friend 
    def add_friend(self, friend_person):
        list_friend_person = dict1[friend_person]
        self.list_Friends.append(list_friend_person)

    # method to get names of the objects
    def get_name(self):
        return self.first_name + ' ' + self.last_name

    # method to return the lists of friend made out of get_name function
    def get_friends(self):
        return self.list_Friends


"""
# load_people function to create Person's object and return a list of Person's objects.
"""


def load_people():

    # reading from txt file
    num_lines = sum(1 for line in open("a2_sample_set.txt"))
    reading_file = open("a2_sample_set.txt", 'r')
    objects_list = []
    first_name_list = []
    list_of_lists = []
    # for loop to get names of the Persons
    for names in range(num_lines):
        readPerson = reading_file.readline()
        y = 1
        person_name = []
        for val in readPerson:
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
        first_name = Person(first_name0[0], first_name0[1])  # creation of objects for each Person
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
    # for loop for mapping values in the Person class method and returns Person’s object list
    for object_ in objects_list:
        for name in dict2.get(object_):
            object_.add_friend(name)
    return objects_list  # resulting Person's object list


if __name__ == '__main__':  # main function to define the flow and run code
    load_people()
