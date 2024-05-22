voted = {}


def check_voter(name):
    if name in voted:
        print("Kick them out!")
    else:
        voted[name] = True
        print("Let them vote")


check_voter("Tom")
check_voter("Mike")
check_voter("Mike")
