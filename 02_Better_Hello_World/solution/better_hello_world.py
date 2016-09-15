#!/usr/bin/env python3

# OK, now we're going to do a slightly more complicated Hello World

# First, declare two variables.

# Here, declare one called print1 with the value "Hello, world!"

print1 = "Hello, world!"

# Now here, declare another one called print2 with the value "Nice to see you!"

print2 = "Nice to see you!"

# This bit here is called a loop. It executes a block of code multiple times
for i in range(10): #Notice how a line that begins a block ends with a colon.
    if (i % 2) == 0:
        print(print1)
    else:
        print(print2)

# You had to line up the function calls because python uses spaces to group
# code into blocks. This is different from how Arduino uses curly braces to
# delimit blocks.
