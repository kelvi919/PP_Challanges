"""The aim of this challenge is, 
given a dictionary of people's online status, 
to count the number of people who are online.
"""


statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}


def online_count(statuses):
    number_of_online = 0
    states = statuses.values()
    
    for nr in states:
        if nr == "online":
            number_of_online += 1
        else :
            pass
    return(number_of_online)


online_count(statuses)
