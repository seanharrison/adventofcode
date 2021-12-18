"""
As the submarine drops below the surface of the ocean, it automatically performs a sonar
sweep of the nearby sea floor. On a small screen, the sonar sweep report (your puzzle
input) appears: each line is a measurement of the sea floor depth as the sweep looks
further and further away from the submarine.

For example, suppose you had the following report:
```
199
200
208
210
200
207
240
269
260
263
```
This report indicates that, scanning outward from the submarine, the sonar sweep found
depths of 199, 200, 208, 210, and so on.

The first order of business is to figure out how quickly the depth increases, just so
you know what you're dealing with - you never know if the keys will get carried into
deeper water by an ocean current or a fish or something.

To do this, count the number of times a depth measurement increases from the previous
measurement. (There is no measurement before the first measurement.) In the example
above, the changes are as follows:
```
199 (N/A - no previous measurement) 
200 (increased) 
208 (increased) 
210 (increased) 
200 (decreased) 
207 (increased) 
240 (increased) 
269 (increased) 
260 (decreased) 
263 (increased)
```
In this example, there are 7 measurements that are larger than the previous measurement.

How many measurements are larger than the previous measurement?
"""

# Count the number of increases in the input file.
# - Open input file as a stream
# - Read it one line at a time.
# - Even if the file is 3TB, this method will still work.

import sys

filepath = sys.argv[1] if len(sys.argv) > 1 else "input"
increases = 0
previous = None
with open(filepath) as f:
    for line in f:
        value = int(line)
        if previous and value > previous:
            increases += 1
        previous = value

print('increases =', increases)
