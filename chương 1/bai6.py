class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return self.items == []

    def print(self):
        if self.is_empty():
            print("Ngăn xếp rỗng")
        else:
            print("Nội dung ngăn xếp:")
            for item in reversed(self.items):
                print(item)