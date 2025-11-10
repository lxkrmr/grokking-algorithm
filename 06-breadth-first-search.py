from collections import deque


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if person in searched:
            continue

        if person_is_seller(person):
            print(person + " is a mango seller!")
            return True

        search_queue += graph[person]
        searched.add(person)

    return False


def person_is_seller(name):
    return name[-1] == 'm'


graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}


if __name__ == '__main__':
    print(search("you"))
