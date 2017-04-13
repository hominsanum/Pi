# coding: utf-8

# Program to calculate PI
from numpy import *
import matplotlib.pyplot as plt

print "Calculating PI with Random Numbers"
print "How many numbers shall we use ?"

# Get a value from the keyboard - The amount of Random Numbers to use
i=input()
if i > 100000 :
   i = 100000

# Set up counters for the total number of points, and number of points inside circle 
inside = 0.0
c = 0.0
x_coord = []
y_coord = []
pi_evolution = []

# Start a loop to generate the random number and calculate PI
while c < i :
   
   # Create a random point using two randome co-ordinates called 'x' and 'y'
   x = random.rand()
   y = random.rand()
   x_coord.append(x)
   y_coord.append(y)
   
   # Find how far the random point is from the origin using Pythagorus
   z = math.sqrt( (x * x)  + (y * y) )
   
   # Check to see if the random point is inside or outside of circle
   if z < 1 :
       
       # And add one to the count if it is
       inside = inside + 1
   
   # Add one to the count of random points checked so far
   c = c + 1
   
   # Make a new estimate of PI with all the data so far
   piestimate = inside / ( c / 4 )
   pi_evolution.append(piestimate)
   
   # Print the data from this current loop
   if c < 10 :
       print int (c), "points, PI =", round(piestimate,4)
   elif c < 100 and c / 10 == int (c / 10) :
       print int (c), "points, PI =", round(piestimate,4)
   elif c < 1000 and c / 100 == int (c / 100) :
       print int (c), "points, PI =", round(piestimate,4)
   elif c < 10000 and c / 1000 == int (c / 1000) :
       print int (c), "points, PI =", piestimate
   elif c < 100000 and c / 10000 == int (c / 10000) :
       print int (c), "points, PI =", piestimate
   elif c < 1000000 and c / 100000 == int (c / 100000) :
       print int (c), "points, PI =", piestimate
   elif c / 1000000 == int (c / 1000000) :
       print int (c), "points, PI =", piestimate

arc_x = []
arc_y = []
for arc in range(0, 90):
	arc_x.append(sin(arc*pi/180))
	arc_y.append(cos(arc*pi/180))
       
# Print final value
plt.scatter(x_coord, y_coord)
plt.axis([0,1,0,1])
plt.plot(arc_x, arc_y, '-r')
plt.show()
print "After ", i, " points my final estimate of PI is ", round(piestimate,4)