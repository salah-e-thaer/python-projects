from collections import deque

graph = {}

graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def person_is_seller(name):
    return name[-1] == 'm'

def sreach(name):
    sreach_queue = deque()
    sreach_queue += graph[name]
    sreached = []
    while sreach_queue:
        person = sreach_queue.popleft()
        if not person in sreached:
            if person_is_seller(person):
                print(f"{person} is a mango seller")
            else:
                sreach_queue += graph[person]
                sreached.append(person)

sreach("you")