class MinStack:

    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        cur_min: int
        if not self.s:
            cur_min = val
        else:
            cur_min = min(val, self.s[-1][1])

        self.s.append((val, cur_min))

    def pop(self) -> None:
        trash = self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]

        
