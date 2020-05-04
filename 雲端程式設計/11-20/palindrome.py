class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
 
s = Stack()
text = input('請輸入')
for character in text:
    s.push(character)
reversed_text = ''
text.replace(" ", "")
text=text.lower()

while not s.is_empty():
    reversed_text.replace(" ", "")    
    reversed_text = reversed_text + s.pop()
    reversed_text=reversed_text.lower()
if text == reversed_text:
    print('palindrome.')
else:
    print('not a palindrome.')
