# Suppose I show you a call stack like this.

# greet2(name)
# greet(name)

# What information can you give me, just based on this call stack?
# Now let’s see the call stack in action with a recursive function.

# The greet function is called first
# Then the greet function calls the greet2 function
# At this point, the greet function is in an incomplete, suspended state.
# The current function call is the greet2 function.
# After this function call completes, the greet function will resume.

def greet2(name):
    print("How are you, " + name + "?")


def greet(name):
    print("Hello, " + name + "!")
    greet2(name)


greet("Maggie")
