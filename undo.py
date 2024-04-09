from turtle import*

pensize(3)
pencolor("blue")
for i in range(50): 
    forward(20+5*i) 
    right(90)

while undobufferentries(): 
    undo()
done()