"""
Start Date:05/06/2020
Last Modified Date: 08/06/2020
Code Outcome: The program here plots the graph of number of affected people per day and number of days the simulation
is run for.

Program outcome Explained: Not always but yes sometimes the resulting graph matches the stated result on the defined
input values. This happens because we are working on random probability keeping aspect of social distancing in
consideration. The graph for each scenario are attached in the file which supports the required analysis
"""

from health_calculation import run_simulation  # importing run_simulation from task 2
from matplotlib import pyplot as plt  # importing matplot library

"""
Function visual_curve is plotting the graph of the simulation
"""


def visual_curve(days, meeting_probability, patient_zero_health):
    if meeting_probability > 1:
        meeting_probability = meeting_probability/100
    no_of_affected_person = run_simulation(days, meeting_probability, patient_zero_health)  # calling runsimulation func
    no_of_days = [*range(1, (len(no_of_affected_person)) + 1)]  # calculating number of days and creating list
    plt.plot(no_of_days, no_of_affected_person)  # plotting graph
    plt.xlabel('Number of Days')  # labeling x axis
    plt.ylabel('Number of affected people')  # labeling y axis
    plt.show()


if __name__ == '__main__':  # main function to define the flow and run code
    visual_curve(int(input('Enter number of days for simulation: ')), float(input('Enter Meeting Probability: ')),
                 float(input('Enter patient zero health: ')))
    #  visual_curve(30, 0.6, 25)   Scenario_A
    #  visual_curve(60, 0.25, 49)  Scenario_B
    #  visual_curve(90, 0.18, 40)  Scenario_C
