class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.list_of_friend = []

    def add_friend(self, friends_of_person, oo):
        ll = oo[friends_of_person]
        self.list_of_friend.append(ll)

    def get_name(self):
        return self.first_name + " " + self.last_name

    def get_friends(self):
        return self.list_of_friend


def load_people():
    # initiating an empty list to import data from text file
    data = []

    # open given file in read mode
    with open('a2_sample_set1.txt', 'r') as file:
        # store each line in the file into the list created above - data[]
        for record in file:
            t = record.strip()
            t = t.replace(":",",")
            t = t.split(", ")
            data.append(t)

    import pandas as pd
    df = pd.DataFrame(data)
    # data[] contains 200 records with the person's name and a list of their friends
    # extract the names and friends-list onto two separate lists
    list_of_people = []
    list2_of_friends = []
    for record in data:
        list_of_people.append(record[0].split())
        # need first and last name separately for the class constructor
        list2_of_friends.append(record[1:])

    # creating an object for each name in list_of_people and storing objects in a new list
    objects_of_personlist = []
    for per_person in list_of_people:
        t  = Person(per_person[0],per_person[1])
        objects_of_personlist.append(t)

    # call get_name() on every object
    allnames_list = df[0]

    # combine objects and their respective names in a dictionary
    objects_name=dict(zip(allnames_list, objects_of_personlist))
    objects_name_1 = dict(zip(objects_of_personlist, list2_of_friends))
    for ob1 in objects_of_personlist:
        for ob2 in objects_name_1.get(ob1):
            ob1.add_friend(ob2, objects_name)
        print(ob1.get_friends())


    return objects_of_personlist

if __name__ == '__main__':
    load_people()

# do not add code here (outside the main block).

