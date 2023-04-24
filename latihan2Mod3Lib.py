from collections import deque

class SecondExercise:
    def queueExample(self):
        baris = deque()
        baris.append("Java")
        baris.append("DotNet")
        baris.append("PHP")
        baris.append("HTML")
        print("popleft : ", baris.popleft())
        print("leftmost element : ", baris[0])
        print("pop : ", baris.pop())
        print("leftmost element : ", baris[0])

if __name__ == '__main__':
    s = SecondExercise()
    s.queueExample()