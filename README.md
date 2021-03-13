Non recursive solution to the towers of hanoi
=============================================

[Solution in python3](hanoi.py)

[Solution in golang](hanoi.go)

[Solution in c++11](hanoi.cpp)

The way to solve this is quite simple but does differ slightly for N = odd or even numbers of rings.

At each move you do either a) or b):

    a) move the "1" value to the peg to the right, wrapping around to the first peg if needed

    b) make the only other legal move

And then repeat either a) or b) for (2 ^ numrings) - 1.

So for N=3, you would do the above steps 7 times.

The catch that I alluded to earlier is that for N == odd (3,5,...), you will need to repeat this
entire algorithm one more time as the above will only move the rings one peg to the right. 

So in pseudo code, we have:

```Python
    for tries in range(0, 1 + nrings % 2):
        for moves in range(0, (1 << nrings) - 1):
            move_peg_one_right = True
            if move_peg_one_right:
                move_peg_one_right_in_a_modulo_loop()
            else:
                make_only_legal_move()

            move_peg_one_right = not move_peg_one_right
```

Here is the output for n == 3:
```
1 | | 
2 | | 
3 | | 
-----
Moving value 1 from peg 1 to peg 2

| | | 
2 | | 
3 1 | 
-----
Moving value 2 from peg 1 to empty peg 3

| | | 
| | | 
3 1 2 
-----
Moving value 1 from peg 2 to peg 3

| | | 
| | 1 
3 | 2 
-----
Moving value 3 from peg 1 to empty peg 2

| | | 
| | 1 
| 3 2 
-----
Moving value 1 from peg 3 to peg 1

| | | 
| | | 
1 3 2 
-----
Moving < value 2 from peg 3 to peg 2 dest 2

| | | 
| 2 | 
1 3 | 
-----
Moving value 1 from peg 1 to peg 2

| 1 | 
| 2 | 
| 3 | 
-----
Finished pass

| 1 | 
| 2 | 
| 3 | 
-----
Moving value 1 from peg 2 to peg 3

| | | 
| 2 | 
| 3 1 
-----
Moving value 2 from peg 2 to empty peg 1

| | | 
| | | 
2 3 1 
-----
Moving value 1 from peg 3 to peg 1

| | | 
1 | | 
2 3 | 
-----
Moving value 3 from peg 2 to empty peg 3

| | | 
1 | | 
2 | 3 
-----
Moving value 1 from peg 1 to peg 2

| | | 
| | | 
2 1 3 
-----
Moving < value 2 from peg 1 to peg 3 dest 2

| | | 
| | 2 
| 1 3 
-----
Moving value 1 from peg 2 to peg 3

| | 1 
| | 2 
| | 3 
-----
Finished pass

```
