from stack import Stack


balls = list(map(int, input().split()))
stack = Stack()
i = 0
while i < len(balls):
    stack.push(balls[i])
    if stack.size() >= 3 and stack.peek(-1) == stack.peek(-2) == stack.peek(-3):
        color = stack.peek()
        for _ in range(3):
            stack.pop()
        while i < len(balls) and balls[i] == color:
            i += 1
    else:
        i += 1

print(len(balls) - stack.size())
