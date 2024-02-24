class Decipher:
    def __init__(self, text, cypher):
        self.text = text.split(" ")
        self.cypher = cypher
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= len(self.cypher):
            raise StopIteration
        # # Check if a raise is also required here
        # if self.cypher[self.current_index] in range(len(self.text)):
        temp = self.cypher[self.current_index]
        self.current_index += 1
        return self.text[temp - 1][0]


def start():
    str = input("type your text\n")
    # https://stackoverflow.com/questions/4663306/get-a-list-of-numbers-as-input-from-the-user
    cypher = [int(x) for x in input().split()]
    for i in Decipher(str, cypher):
        print(i)


start()
# message : cudotwbWtifghpallpntttltetdltcatsatossposseila
