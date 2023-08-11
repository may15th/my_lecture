'''
()(((()())(())()))(())
'''

pipe_lazor = input()
pipe_lazor = list(pipe_lazor)
for i in range(len(pipe_lazor)):
    if pipe_lazor[i] == '(':
        if pipe_lazor[i+1] == ')':
            pipe_lazor[i] = 'L'
            pipe_lazor[i+1] = ''
print(pipe_lazor)