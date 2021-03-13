#!/usr/bin/env python
import sys

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

def tower(nrings, npegs):
    pegs = []
    for peg in range(0, npegs):
        pegs.append([])

    # push the nrings on
    for i in range(0, nrings):
        pegs[0].append(i + 1)

    for tries in range(0, 1 + nrings % 2):
        print_tower(pegs, nrings)
        move_peg_one_right = True
        for moves in range(0, (1 << nrings) - 1):
            if move_peg_one_right:
                for peg in range(0, npegs):
                    if len(pegs[peg]):
                        if pegs[peg][0] == 1:
                            next_peg = (peg + 1) % npegs
                            pegs[next_peg].insert(0, pegs[peg].pop(0))
                            print("Moving value 1 from peg {} to peg {}\n".format(peg + 1, next_peg + 1))
                            break
            else:
                done = False
                for peg in range(0, npegs):
                    if len(pegs[peg]):
                        value = pegs[peg][0]
                        if value != 1:
                            for next_peg in range(0, npegs):
                                next_peg = (peg + next_peg) % npegs
                                if next_peg == peg:
                                    continue

                                if not len(pegs[next_peg]):
                                    pegs[peg].pop(0)
                                    pegs[next_peg].insert(0, value)
                                    done = True
                                    print("Moving value {} from peg {} to empty peg {}\n".format(value, peg + 1, next_peg + 1))
                                    break
                                elif value < pegs[next_peg][0]:
                                    pegs[peg].pop(0)
                                    pegs[next_peg].insert(0, value)
                                    done = True
                                    print("Moving < value {} from peg {} to peg {} dest {}\n".format(value, peg + 1, next_peg + 1, pegs[next_peg][0]))
                                    break
                    if done:
                        break

                if not done:
                    print("Failed to move")
                    sys.exit(1)

            print_tower(pegs, nrings)
            move_peg_one_right = not move_peg_one_right
        print("Finished pass\n")

nrings = 3
npegs = 3
tower(nrings, npegs)
