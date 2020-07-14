# Define four Python functions named run, swing, slide, and hide_and_seek. Each function should take varying number of children's names as the argument.
def run(*kids):
    # Loop through all the kids and print that the child performed the activity.
    for kid in kids:
        print(f'{kid} ran like a girl.')
def swing(*kids):
    # Loop through all the kids and print that the child performed the activity.
    for kid in kids:
        print(f'{kid} swang like a monkey.')
def slide(*kids):
    # Loop through all the kids and print that the child performed the activity.
    for kid in kids:
        print(f'{kid} was sliding in mud.')
def hide_and_seek(*kids):
    # Loop through all the kids and print that the child performed the activity.
    for kid in kids:
        print(f'{kid} hid from themselves.')

run("Joe", "Jenna", "Pam", "Sam", "Andrea", "Will")
swing("Marybeth", "Ariel", "Kevin", "Courtney")
slide("Mike", "Jack", "Jennifer", "Earl")
hide_and_seek("Henry", "Heather", "Hayley", "Hugh")
# Output: 
# "Joe ran like a fool!"
# "Jenna ran like a fool!"