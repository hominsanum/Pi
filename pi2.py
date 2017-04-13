# Program to calculate PI
from numpy import *

print "Calculating PI with Random Numbers"
print "How many Random Numbers shall we use ?"

# Get a value from the keyboard - The amount of Random Numbers to use
i=input()
if i > 10000000 :
	i = 10000000

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
	if c < 10 :
		print "Points so far =" , int(c), "     Estimate of PI =", piestimate
	elif c < 100 and c / 10 == int (c / 10) :
		print "Points so far =" , int(c), "     Estimate of PI =", piestimate
	elif c < 1000 and c / 100 == int (c / 100) :
		print "Points so far =" , int(c), "     Estimate of PI =", piestimate
	elif c < 10000 and c / 1000 == int (c / 1000) :
		print "Points so far =" , int(c), "     Estimate of PI =", piestimate
	elif c < 100000 and c / 10000 == int (c / 10000) :
		print "Points so far =" , int(c), "     Estimate of PI =", piestimate
	elif c < 1000000 and c / 100000 == int (c / 100000) :
		print "Points so far =" , int(c), "     Estimate of PI =", piestimate
	elif c / 1000000 == int (c / 1000000) :
		print "Points so far =" , int(c), "     Estimate of PI =", piestimate
		
# Print final value
print "My final estimate of PI is ", piestimate