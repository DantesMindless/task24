#task1
def stack(sentence):
    stack = []
    reverse = ""
    for i in range(len(sentence)):
        reverse = reverse + sentence[i]
    stack.append(reverse)
    while len(stack) != 0:
        reverse = stack[len(stack) - 1]
        print(reverse[::-1], end=' ')
        stack.pop()



sentence = "Was it a car or a cat I saw"
stack(sentence)

#task2
open= ["{", "[", "("]
close = ["}", "]", ")"]
def balance(str):
    stack = []
    for i in str:
        if i in open:
            stack.append(i)
        elif i in close:
            place = close.index(i)
            if (open[place] == stack[len(stack) - 1]):
                print(stack)

                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"



str = "{{{[s]s{(s)}}}}"
print(balance(str))

#task3

stack1 = []
stack2 = []
def remove(data):
 stack1.append('a')
 stack1.append('b')
 stack1.append('c')
 stack1.append('d')
 stack1.append('e')
 print(stack1)
 while len(stack1)>=1:
    pop = stack1.pop()
    try:
        if data == pop:
           print(pop)
        elif data !=pop:
            stack2.append(pop)

    except ValueError:
        print('Element not found')
 return(stack2[::-1])

print(remove('a'))

