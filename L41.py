#Mandy and Emme
import turtle
jack=turtle.Turtle()
jack.color("yellow")
for side in range(4):
    if side == 2:
        jack.color("blue")
    jack.forward(100)
    jack.right(90)


#The if statement makes it so that when it gets to 3 in the range the color of the line changes from yellow to blue. 
#This makes the whole square yellow and Jack turns blue once it has completed its range(4).
#I think putting the if after forward and right didn't do what the first block of code did because the code ran the range and then looked for the if instead of looking for the if while going through the range.
#In this case, the if statement told the code that if the range is at 2 then it is true and the if statement is run.
    
        
