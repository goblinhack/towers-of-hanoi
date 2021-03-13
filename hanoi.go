//
// The way to solve this is quite simple but does differ slightly for N = odd or even numbers of rings.
//
// At each move you do either a) or b):
//
// a) move the "1" value to the peg to the right, wrapping around to the first peg if needed
//
// b) make the only other legal move
//
// And then repeat either a) or b) for (2 ^ numrings) - 1.
//
// So for N=3, you would do the above steps 7 times.
//
// The catch that I alluded to earlier is that for N == odd (3,5,...), you will need to repeat this
// entire algorithm one more time as the above will only move the rings one peg to the right.
//
package main

import (
    "fmt"
)

//
// Print the tower so we can check our progress
//
func print_tower(pegs [][]int, nrings int) {
    npegs := len(pegs)
    for y := 0; y < nrings; y++ {
        h := nrings - y
        for x := 0; x < npegs; x++ {
            if len(pegs[x]) >= h {
                fmt.Printf("%d ", pegs[x][len(pegs[x]) - h])
            } else {
                fmt.Printf("| ")
            }
        }
        fmt.Println("")
    }
    fmt.Println("-----")
}

func solve_tower(nrings int, npegs int) {
    pegs := make([][]int, npegs)

    //
    // Create empty slices for the pegs
    //
    for i := 0; i < nrings; i++ {
        pegs[0] = make([]int, 0)
    }

    //
    // push the rings on
    //
    for i := 0; i < nrings; i++ {
        pegs[0] = append(pegs[0], i + 1)
    }

    //
    // For N == odd numbers we will need to repeat this twice
    //
    for tries := 0; tries < 1 + nrings % 2; tries++ {
        print_tower(pegs, nrings)
        move_peg_one_right := true

        //
        // Repeat the steps a) or b) for 2^N-1 times
        //
        for moves := 0; moves < (1 << nrings) - 1; moves++ {
            //
            // step a)
            //
            if move_peg_one_right {
                for peg := 0; peg < npegs; peg++ {
                    if len(pegs[peg]) > 0 {
                        if (pegs[peg][0] == 1) {
                            next_peg := (peg + 1) % npegs

                            popped := pegs[peg][0]
                            pegs[peg] = pegs[peg][1:]
                            pegs[next_peg] = append([]int{popped}, pegs[next_peg]...)

                            fmt.Printf("Moving value 1 from peg %d to peg %d\n\n", peg + 1, next_peg + 1)
                            break
                        }
                    }
                }
            } else {
                //
                // step b)
                //
                moved_a_ring := false
                for peg := 0; peg < npegs; peg++ {
                    //
                    // Look for a ring on a peg to move
                    //
                    if len(pegs[peg]) > 0 {
                        value := pegs[peg][0]
                        //
                        // Don't move the ring value "1" as we move that in a)
                        //
                        if (value != 1) {
                            for n := 0; n < npegs; n++ {
                                //
                                // The next peg is the one to the right of this peg. If we reach the last peg then we
                                // need to move to the first peg.
                                //
                                next_peg := (peg + n) % npegs

                                //
                                // Don't move to the same peg; that would be silly
                                //
                                if (next_peg == peg) {
                                    continue
                                }

                                //
                                // If the destination peg is empty, move there
                                //
                                if len(pegs[next_peg]) == 0 {
                                    pegs[peg] = pegs[peg][1:]
                                    pegs[next_peg] = append([]int{value}, pegs[next_peg]...)
                                    moved_a_ring = true
                                    fmt.Printf("Moving value %d from peg %d to empty peg %d\n\n", value, peg + 1, next_peg + 1)
                                    break
                                } else if (value < pegs[next_peg][0]) {
                                    //
                                    // Else if the destination peg has a lower value, move there
                                    //
                                    pegs[peg] = pegs[peg][1:]
                                    pegs[next_peg] = append([]int{value}, pegs[next_peg]...)
                                    moved_a_ring = true
                                    fmt.Printf("Moving < value %d from peg %d to peg %d dest %d\n\n", value, peg + 1, next_peg + 1, pegs[next_peg][0])
                                    break
                                }
                            }
                        }
                    }

                    if (moved_a_ring) {
                        break
                    }
                }

                if ! moved_a_ring {
                    panic("Error, failed to move")
                }
            }

            print_tower(pegs, nrings)

            //
            // Alternate between a) and b)
            //
            move_peg_one_right = ! move_peg_one_right
        }
        fmt.Printf("Finished pass\n\n")
    }
}

func main() {
    nrings := 3
    npegs := 3
    solve_tower(nrings, npegs)
}
