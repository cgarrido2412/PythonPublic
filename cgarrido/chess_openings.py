#!/usr/bin/env python3

if __name__ == "__main__":
    beginner = """
    Evans Gambit
    London System
    Advanced French
    Caro Kann
    Danish Gambit 
    Kings Indian
    Vienna Gambit 
    Scandi
    Sicilian Defense
    """

    beginner = beginner.split('\n')
    beginner_openings = []
    for x in range(len(beginner)):
        beginner[x] = beginner[x].lower().strip()
        beginner_openings.append(beginner[x])

    intermediate = """
	Queens Gambit
	Evans Gambit
	Caro Kann
	Grand Prix
	Closed Sicilian
	Kings Indian
	Ruy Lopez
	Sicilian Defense 
	Vienna Gambit
	 Alapin Sicilian
    """

    intermediate = intermediate.split('\n')
    intermediate_openings = []
    for x in range(len(intermediate)):
        intermediate[x] = intermediate[x].lower().strip()
        intermediate_openings.append(intermediate[x])

    commonList = set();
    [commonList.add(x) for x in beginner_openings for y in intermediate_openings if x == y]

    for x in commonList:
        print(x)
