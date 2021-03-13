//
// Compile like: g++ -std=c++11  -Wall hanoi.cpp
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
#include <iostream>
#include <list>
#include <vector>

//
// Print the tower so we can check our progress
//
void print_tower(std::vector< std::list< int > > &pegs, int nrings) {
    auto npegs = pegs.size();
    for (auto y = 0; y < nrings; y++) {
        auto h = nrings - y;
        for (auto x = 0U; x < npegs; x++) {
            if (pegs[x].size() >= static_cast<size_t>(h)) {
                auto l = pegs[x].begin();
                std::advance(l, pegs[x].size() - h);
                printf("%d ", *l);
            } else {
                printf("| ");
            }
        }
        printf("\n");
    }
    printf("-----\n");
}

void solve_tower(int nrings, int npegs) {
    std::vector< std::list< int > > pegs;

    //
    // Create empty lists for the pegs
    //
    pegs.resize(npegs);

    //
    // push the rings on
    //
    for (auto i = 0; i < nrings; i++) {
        pegs[0].push_back(i + 1);
    }

    //
    // For N == odd numbers we will need to repeat this twice
    //
    for (auto tries = 0; tries < 1 + nrings % 2; tries++) {
        print_tower(pegs, nrings);
        auto move_peg_one_right = true;

        //
        // Repeat the steps a) or b) for 2^N-1 times
        //
        for (auto moves = 0; moves < (1 << nrings) - 1; moves++) {
            //
            // step a)
            //
            if (move_peg_one_right) {
                for (auto peg = 0; peg < npegs; peg++) {
                    if (pegs[peg].size() > 0) {
                        if (pegs[peg].front() == 1) {
                            auto next_peg = (peg + 1) % npegs;
                            auto popped = pegs[peg].front();
                            pegs[peg].pop_front();
                            pegs[next_peg].push_front(popped);

                            printf("Moving value 1 from peg %d to peg %d\n\n", peg + 1, next_peg + 1);
                            break;
                        }
                    }
                }
            } else {
                //
                // step b)
                //
                auto moved_a_ring = false;
                for (auto peg = 0; peg < npegs; peg++) {
                    //
                    // Look for a ring on a peg to move
                    //
                    if (pegs[peg].size() > 0) {
                        auto value = pegs[peg].front();
                        //
                        // Don't move the ring value "1" as we move that in a)
                        //
                        if (value != 1) {
                            for (auto n = 0; n < npegs; n++) {
                                //
                                // The next peg is the one to the right of this peg. If we reach the last peg then we
                                // need to move to the first peg.
                                //
                                auto next_peg = (peg + n) % npegs;

                                //
                                // Don't move to the same peg; that would be silly
                                //
                                if (next_peg == peg) {
                                    continue;
                                }

                                //
                                // If the destination peg is empty, move there
                                //
                                if (pegs[next_peg].empty()) {
                                    pegs[peg].pop_front();
                                    pegs[next_peg].push_front(value);
                                    moved_a_ring = true;
                                    printf("Moving value %d from peg %d to empty peg %d\n\n", value, peg + 1, next_peg + 1);
                                    break;
                                } else if (value < pegs[next_peg].front()) {
                                    //
                                    // Else if the destination peg has a lower value, move there
                                    //
                                    pegs[peg].pop_front();
                                    pegs[next_peg].push_front(value);
                                    moved_a_ring = true;
                                    printf("Moving < value %d from peg %d to peg %d dest %d\n\n", value, peg + 1, next_peg + 1, pegs[next_peg].front());
                                    break;
                                }
                            }
                        }
                    }

                    if (moved_a_ring) {
                        break;
                    }
                }

                if (! moved_a_ring) {
                    throw("Error, failed to move");
                }
            }

            print_tower(pegs, nrings);

            //
            // Alternate between a) and b)
            //
            move_peg_one_right = ! move_peg_one_right;
        }
        printf("Finished pass\n\n");
    }
}

int main () {
    auto nrings = 3;
    auto npegs = 3;
    solve_tower(nrings, npegs);
    return 0;
}
