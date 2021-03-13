#!/usr/bin/env python
#
# The way to solve this is quite simple but does differ slightly for N = odd or even numbers of rings.
# 
# At each move you do either a) or b):
# 
# a) move the "1" value to the peg to the right, wrapping around to the first peg if needed
# 
# b) make the only other legal move
# 
# And then repeat either a) or b) for (2 ^ numrings) - 1.
# 
# So for N=3, you would do the above steps 7 times.
# 
# The catch that I alluded to earlier is that for N == odd (3,5,...), you will need to repeat this
# entire algorithm one more time as the above will only move the rings one peg to the right. 
#
import sys

#
# Print the tower so we can check our progress
#
def print_tower(pegs, nrings):
    npegs = len(pegs)
    for y in range(0, nrings):
        h = nrings - y
        for x in range(0, npegs):
            if len(pegs[x]) >= h:
                sys.stdout.write(str(pegs[x][len(pegs[x]) - h]) + " ")
            else:
                sys.stdout.write("| ")
        print("")
    print("-----")

def solve_tower(nrings, npegs):
    pegs = []

    #
    # Create empty lists for the pegs
    #
    for peg in range(0, npegs):
        pegs.append([])

    #
    # push the rings on
    #
    for i in range(0, nrings):
        pegs[0].append(i + 1)

    #
    # For N == odd numbers we will need to repeat this twice
    #
    for tries in range(0, 1 + nrings % 2):
        print_tower(pegs, nrings)
        move_peg_one_right = True

        #
        # Repeat the steps a) or b) for 2^N-1 times
        #
        for moves in range(0, (1 << nrings) - 1):
            #
            # step a)
            #
            if move_peg_one_right:
                for peg in range(0, npegs):
                    if len(pegs[peg]):
                        if pegs[peg][0] == 1:
                            next_peg = (peg + 1) % npegs
                            pegs[next_peg].insert(0, pegs[peg].pop(0))
                            print("Moving value 1 from peg {} to peg {}\n".format(peg + 1, next_peg + 1))
                            break
            else:
                #
                # step b)
                #
                moved_a_ring = False
                for peg in range(0, npegs):
                    #
                    # Look for a ring on a peg to move
                    #
                    if len(pegs[peg]):
                        value = pegs[peg][0]
                        #
                        # Don't move the ring value "1" as we move that in a)
                        #
                        if value != 1:
                            for n in range(0, npegs):
                                #
                                # The next peg is the one to the right of this peg. If we reach the last peg then we
                                # need to move to the first peg.
                                #
                                next_peg = (peg + n) % npegs

                                #
                                # Don't move to the same peg; that would be silly
                                #
                                if next_peg == peg:
                                    continue

                                #
                                # If the destination peg is empty, move there
                                #
                                if not len(pegs[next_peg]):
                                    pegs[peg].pop(0)
                                    pegs[next_peg].insert(0, value)
                                    moved_a_ring = True
                                    print("Moving value {} from peg {} to empty peg {}\n".format(value, peg + 1, next_peg + 1))
                                    break
                                elif value < pegs[next_peg][0]:
                                    #
                                    # Else if the destination peg has a lower value, move there
                                    #
                                    pegs[peg].pop(0)
                                    pegs[next_peg].insert(0, value)
                                    moved_a_ring = True
                                    print("Moving < value {} from peg {} to peg {} dest {}\n".format(value, peg + 1, next_peg + 1, pegs[next_peg][0]))
                                    break
                    if moved_a_ring:
                        break

                if not moved_a_ring:
                    print("Error, failed to move")
                    sys.exit(1)

            print_tower(pegs, nrings)

            #
            # Alternate between a) and b)
            #
            move_peg_one_right = not move_peg_one_right

        print("Finished pass\n")

nrings = 3
npegs = 3
solve_tower(nrings, npegs)
