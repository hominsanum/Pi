# Program to calculate PI
from numpy import *

print "Calculating PI with Random Numbers"
print "How many Random Numbers shall we use ?"

# Get a value from the keyboard - The amount of Random Numbers to use
i=input()

# Set up counters for the total number of points, and number of points inside circle 
inside = 0.0
c = 0.0

# Start a loop to generate the random number and calculate PI
while c < i :
	
	# Create a random point using two randome co-ordinates called 'x' and 'y'
	x = random.rand()
	y = random.rand()
	
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
	
	# Print the data from this current loop
	print c,",", x,",", y,",", z,",", piestimate

# Print final value
print "My final estimate of PI is ", piestimate