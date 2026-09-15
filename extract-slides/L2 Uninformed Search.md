# L2 Uninformed Search

> Source: [original PDF](<../slides/L2 Uninformed Search.pdf>) · 93 slides. Text extraction may omit figures and alter equations; check the PDF.

## Slide 1

```text
COMP 424 - Artificial Intelligence
             Fall 2026


          Lecture 2: September 2nd, 2026
              Uninformed Search

     Su Lin Blodgett (sulin.blodgett@mcgill.ca)
     Jackie CK Cheung (jackie.cheung@mcgill.ca)
```

## Slide 2

```text
Announcements

•  Ed is up and running. You all should have been added.
      •  Please contact us if you’re registered for the course, but you
       haven’t received an email from Ed.

•  Office hours are now scheduled:
      •  Su Lin: Mondays, 2:00pm - 3:30pm in McConnell 312
      •   Jackie: Wednesdays, 9:30am – 11am in McConnell 108N

•  Starting next week (Sept 9), we'll be in MCMED 522!





                                                                                  3
```

## Slide 3

```text
The Goal Today





                                                          4
```

## Slide 4

```text
Search in AI

       Search is at the heart of all AI systems!



                        do the right thingThinking      Thinking
Humanly      Rationally
                          OR

 Acting         Acting                        search for what can be done
Humanly      Rationally
                   and then choose the right thing





                                                                              5
```

## Slide 5

```text
Search in AI

Typical setup of search in AI:

 •  Knowledge: Formal representation of the problem
                                                            S: state space     •   State: where are we?                                                             s0 ∈S: initial state     •   Actions: what can we do in a state?
                                                      A: set of actions         (also called Operators)
     •   Transitions: how will the state change if we do an action? T: (s, a) -> s’     •   Goals: how will we know we’re done?  G ⊂S: set of goal states
     •  Costs/rewards: which ‘path’ to the goal is better? C: cost of paths

 •  Search: Algorithmic component that finds a solution





                                                                                    12
```

## Slide 6

```text
Example: Maze





• States?
• Actions?
•  Transitions?
• Goals?
• Path cost?



                                                                         13
```

## Slide 7

```text
Example: Maze





• States? The maze and our location in the maze
• Actions? Up, down, right, and left (where there isn’t a wall)
•  Transitions? Our location changes based on the action
• Goals? Reaching the ‘End’
• Path cost? Length of the path



                                                                         14
```

## Slide 8

```text
Example: Eight-Puzzle





• States?
• Actions?
•  Transitions?
• Goals?
• Path cost?



                                                                         15
```

## Slide 9

```text
Example: Eight-Puzzle





• States? List of where each number is
• Actions? Swap the blank with an adjacent tile
•  Transitions? Update the swapped number’s new location
• Goals? Target configuration on the right
• Path cost? Number of moves



                                                                         16
```

## Slide 10

```text
Example: Pac Man





• States?
• Actions?
•  Transitions?

• Goals?
• Path cost?


                                                                         17
```

## Slide 11

```text
Example: Pac Man





• States? The maze, the location of pellets, pac-man, and all ghosts
• Actions? Up, down, right, and left (where there isn’t a wall)
•  Transitions? Pac-man’s and all ghosts’ locations change
           A pellet might get eaten, pac-man might die
• Goals? All pellets are eaten and pac-man hasn’t died
• Path cost? Number of moves


                                                                         18
```

## Slide 12

```text
The Value of Games in AI

•  Games have well-defined rules and clear markers of
   success
• Game complexity can be easily adjusted without
  changing the underlying problem


•  Games are great at abstracting real problems





                                                                                   19
```

## Slide 13

```text
The Value of Games in AI





                                                                                      Source:
                                                              https://www.theconstruct.ai/robotigniteacademy_learnr
                                                                                    os/ros-courses-library/





                                                                      20
```

## Slide 14

```text
The Value of Games in AI





Source: https://sudoku-puzzles.net/asterisk-sudoku-
                      easy/





                                                                                 21
```

## Slide 15

```text
More Examples
Airplane gate assignment              Warehouse management





 Poaching enforcement                  Multi-agent collaboration





                           Dynamic airport gate assignment with improved Shuffled Frog-Leaping Algorithm and triangle membership function
                      PAWS — A Deployed Game-Theoretic Application to Combat Poaching
                               https://www.linkedin.com/pulse/warehousing-inventory-management-critical-topics-within-meshack-sofof
                          PSOPF-MATD3: A multi-agent collaborative radioactive source search strategy             22
```

## Slide 16

```text
More Examples





                                     Automated program repair



Hyperparameter optimization

                                                 A genetic programming approach to automated software repair
                                                                https://blog.ml.cmu.edu/2018/12/12/massively-parallel-hyperparameter-optimization/23
```

## Slide 17

```text
A Common Representation:
          State Space Graphs

•  Graph defined by a set of vertices and edges where:
      •  Vertices correspond to states in S
      •  Edges indicate that some operator allows transitioning between
        states



                                          2
                                                                                                                  5                                           D                                                                   Goal                                                                   2

                                                                                                                            L
                           C
                                                             E
                                                          8                                            1
                                                                                                                                       5
                                                                                                                                                                                                                          I
                                                                              2
                                     B
                             3
                                                                                                     1
                                                                                                    K
        Start    A                 9                                                                        H
                                                                                                                 9
                                                                     4
                               1
                                                                                    4
                                                                                                                              5
                                            F

                                                           15           G
                                                                                                                    J

                                                                                                 3



                                                                                   25
```

## Slide 18

```text
Search Trees

•  Represents the exploration paths in a search procedure
      •  Nodes represent current progress, must store latest state in S
      and any extra info required by the search method
      •  Edges correspond to operators

• We want to search only until a goal is found, and then
   retrace our steps to return the path


                                                                                State: A
                                                                                Cost: 0





                                            State: B                            State: I                             State: F
                                          Cost: 3                            Cost: 9                            Cost: 1


                   …                                 …



                                                                                   26
```

## Slide 19

```text
State Space Graphs vs Search Trees



                        2
                                                                            5             Goal                          D       2
                                                                                   L               C                                                State space
                                      E
                                    8                          1                                         graph                                                                                          5                                                                                                                                               I
                                                  2
               3          B
                                                                  1               K
Start  A            9                             H                                                                           9
                                            4
                1                                                       4                                                                                    5
                          F
                                     15       G
                                                                             J
                                                               3



                                             State: A
                                           Cost: 0
                                                     Sample search
                                                                tree
                State: B                     State: I                     State: F
                Cost: 3                     Cost: 9                     Cost: 1


     …                          …




                                                                                 27
```

## Slide 20

```text
Questions?





                                                     28
```

## Slide 21

```text
Uninformed Search

• Goal states have binary “goal” information.
• Non-goal states have no information about distance to
  goal.
• Hence, all you can do is move systematically between
  states until you stumble on a goal.





                                                                                    29
```

## Slide 22

```text
Breadth-First Search vs Depth-First Search





                                                                                   30
```

## Slide 23

```text
Breadth-First Search vs Depth-First Search


              BFS                              DFS

        “siblings over children”                   “children over siblings”





                                                                                   31
```

## Slide 24

```text
Breadth-First Search vs Depth-First Search


              BFS                              DFS

        “siblings over children”                   “children over siblings”
                                         initial node





                                                                                   32
```

## Slide 25

```text
Breadth-First Search vs Depth-First Search


                  BFS                              DFS

            “siblings over children”                   “children over siblings”
                                              initial node
Round 1                     unexpanded nodes





                                                                                        33
```

## Slide 26

```text
Breadth-First Search vs Depth-First Search


                  BFS                              DFS

            “siblings over children”                   “children over siblings”
                                              initial node
Round 2                     unexpanded nodes
                            expanded nodes





                                                                                        34
```

## Slide 27

```text
Breadth-First Search vs Depth-First Search


                  BFS                              DFS

            “siblings over children”                   “children over siblings”
                                              initial node
Round 3                     unexpanded nodes
                            expanded nodes





                                                                                        35
```

## Slide 28

```text
Breadth-First Search vs Depth-First Search


                  BFS                              DFS

            “siblings over children”                   “children over siblings”
                                              initial node
Round 4                     unexpanded nodes
                            expanded nodes





                                                                                        36
```

## Slide 29

```text
Breadth-First Search vs Depth-First Search


                  BFS                              DFS

            “siblings over children”                   “children over siblings”
                                              initial node
Round 5                     unexpanded nodes
                            expanded nodes





                                                                                        37
```

## Slide 30

```text
Breadth-First Search vs Depth-First Search


                  BFS                              DFS

            “siblings over children”                   “children over siblings”
                                              initial node
Round 6                     unexpanded nodes
                            expanded nodes





                                                                                        38
```

## Slide 31

```text
Breadth-First Search vs Depth-First Search


                  BFS                              DFS

            “siblings over children”                   “children over siblings”
                                              initial node
Round 7                     unexpanded nodes
                            expanded nodes





                                                                                        39
```

## Slide 32

```text
Breadth-First Search vs Depth-First Search


                  BFS                              DFS

            “siblings over children”                   “children over siblings”
                                              initial node
Round 8                     unexpanded nodes
                            expanded nodes





                                                                                        40
```

## Slide 33

```text
Breadth-First Search vs Depth-First Search


                  BFS                              DFS

            “siblings over children”                   “children over siblings”
                                              initial node
Round 9                     unexpanded nodes
                            expanded nodes





                                                                                        41
```

## Slide 34

```text
Breadth-First Search vs Depth-First Search


                  BFS                              DFS

             “siblings over children”                   “children over siblings”
                                               initial node
Round 10                    unexpanded nodes
                             expanded nodes





                                                                                        42
```

## Slide 35

```text
Breadth-First Search vs Depth-First Search


                  BFS                              DFS

             “siblings over children”                   “children over siblings”
                                               initial node
Round 11                    unexpanded nodes
                             expanded nodes





                                                                                        43
```

## Slide 36

```text
Breadth-First Search vs Depth-First Search


                  BFS                              DFS

             “siblings over children”                   “children over siblings”
                                               initial node
Round 12                    unexpanded nodes
                             expanded nodes





                                                                                        44
```

## Slide 37

```text
Breadth-First Search vs Depth-First Search


                  BFS                              DFS

             “siblings over children”                   “children over siblings”
                                               initial node
Round 13                    unexpanded nodes
                             expanded nodes





                                                                                        45
```

## Slide 38

```text
Breadth-First Search vs Depth-First Search


                  BFS                              DFS

             “siblings over children”                   “children over siblings”
                                               initial node
Round 14                    unexpanded nodes
                             expanded nodes





                                                                                        46
```

## Slide 39

```text
Breadth-First Search vs Depth-First Search


                  BFS                              DFS

             “siblings over children”                   “children over siblings”
                                               initial node
Round 15                    unexpanded nodes
                             expanded nodes





                                                                                        47
```

## Slide 40

```text
Breadth-First Search vs Depth-First Search


                  BFS                              DFS

             “siblings over children”                   “children over siblings”
                                               initial node
Round 16                    unexpanded nodes
                             expanded nodes





                                                                                        48
```

## Slide 41

```text
Key Properties of an Algorithm

• Completeness: Are we assured to find a solution, if one
  exists?
• Optimality: How good is the solution?
• Space complexity: How much storage is needed?
• Time complexity: How many operations are needed?





                                                                                    49
```

## Slide 42

```text
Key Properties of an Algorithm

• Completeness: Are we assured to find a solution, if one
  exists?
• Optimality: How good is the solution?
• Space complexity: How much storage is needed?
• Time complexity: How many operations are needed?

• Typically conditioned on:
    • The precise implementation of the search method (do we check
      duplicates? Early/late goal check?)
    • Properties of the search graph (contains loops? (in)finite? goal
      depth?)





                                                                                    50
```

## Slide 43

```text
Another Detour: Big O Notation

• How long does code run, or how much memory does it
 consume?
• Big O is about finding an asymptotic upper bound.
    •  i.e., how an algorithm's runtime or spacetime scales as input grows
• We want a summary of the dominant scaling factor:
    • f(n) = O(g(n)) if there exist positive constants c, n0 s.t. f(n) ≤ c*g(n)
       for all n ≥ n0





                                                                                    51
```

## Slide 44

```text
Key Properties
 b ⇒branching factor d ⇒depth of shallowest solution m ⇒maximum depth of the search tree

          BFS     DFS

Completeness
(finite “b”)

Optimality
(step costs=1)

Space
Complexity

Time
Complexity





                                                                                      52
```

## Slide 45

```text
Key Properties
 b ⇒branching factor d ⇒depth of shallowest solution m ⇒maximum depth of the search tree

          BFS     DFS

Completeness
(finite “b”)

Optimality
(step costs=1)

Space
Complexity

Time                 O(bd)           O(bm)
Complexity





                                                                                      53
```

## Slide 46

```text
Key Properties
 b ⇒branching factor d ⇒depth of shallowest solution m ⇒maximum depth of the search tree

          BFS     DFS

Completeness
(finite “b”)

Optimality
(step costs=1)

Space                O(bd)         O(bm)
Complexity

Time                 O(bd)           O(bm)
Complexity





                                                                                      54
```

## Slide 47

```text
Key Properties
 b ⇒branching factor d ⇒depth of shallowest solution m ⇒maximum depth of the search tree

          BFS     DFS

Completeness       Yes          No
(finite “b”)

Optimality
(step costs=1)

Space                O(bd)         O(bm)
Complexity

Time                 O(bd)           O(bm)
Complexity





                                                                                      55
```

## Slide 48

```text
Key Properties
 b ⇒branching factor d ⇒depth of shallowest solution m ⇒maximum depth of the search tree

          BFS     DFS

Completeness       Yes          No
(finite “b”)

Optimality          Yes          No
(step costs=1)

Space                O(bd)         O(bm)
Complexity

Time                 O(bd)           O(bm)
Complexity





                                                                                      56
```

## Slide 49

```text
General Step Cost

• Actions often have different costs

• e.g., I can buy a burger for $5 or fries for $3

• e.g., I can walk to the classroom outside at a cost of 500
 units of warmth, or I can walk through the underground
 tunnels at a cost of 5 units of warmth





                                                                                    57
```

## Slide 50

```text
Uniform Cost Search

• Goal: Fix BFS to ensure an optimal path with general step
 costs (i.e., in a weighted graph).
Important distinction:
    • Unit cost = Problem where each action has the same cost.
    • General cost = Actions can have different costs.





                                                                                    58
```

## Slide 51

```text
Uniform Cost Search

• Goal: Fix BFS to ensure an optimal path with general step
 costs (i.e., in a weighted graph).
Important distinction:
    • Unit cost = Problem where each action has the same cost.
    • General cost = Actions can have different costs.
• Approach:
    • Use a priority queue instead of a simple queue.
    • Insert nodes in the increasing order of the cost of the path so far.
• Properties:
    • Guaranteed to find optimal solution for graph with general step
     costs (same as BFS when all operators have the same cost).





                                                                                    59
```

## Slide 52

```text
Uniform Cost Search

• Goal: Fix BFS to ensure an optimal path with general step   Priority queue
 costs (i.e., in a weighted graph).s1, 12  (here a min heap)
Important distinction:
    • Unit cost = Problem where each action has the same cost.
    • General cost = Actions can have different costs.
• Approach:           s2, 37           s3, 19
    • Use a priority queue instead of a simple queue.
    • Insert nodes in the increasing order of the cost of the path so far.
• Properties:
    • Guaranteed to find optimal solution for with general step costs                s5, 55            s4, 23           s6, 46    (same as BFS when all operators have the same cost).





                                                                                    60
```

## Slide 53

```text
Example: Shortest Path



                        2
                                                                            5             Goal                          D       2
                                                                                   L                                                             State: A
               C
                                      E                                                                                                                  Cost: 0
                                    8                          1
                                                                                          5                                                                                                                                                I
               3          B
                                                                  1               K
Start  A            9                             H                                                                           9
                                            4
                1                                                       4                                                                                    5
                          F
                                     15       G
                                                                             J
                                                               3





                                                                                      61
```

## Slide 54

```text
Example: Shortest Path



                        2
                                                                            5             Goal                          D       2
                                                                                   L                                                             State: A
               C
                                      E                                                                                                                  Cost: 0
                                    8                          1
                                                                                          5                                                                                                                                                I
                                                                                                                                                                                                                 State: F
               3          B                                                                                                              State: B                       State: I                      Cost: 1
                                                                  1               K                                   Cost: 3                       Cost: 9
Start  A            9                             H                                                                           9
                                            4
                1                                                       4                                                                                    5
                          F
                                     15       G
                                                                             J
                                                               3





                                                                                      62
```

## Slide 55

```text
Example: Shortest Path



                        2
                                                                            5             Goal                          D       2
                                                                                   L                                                             State: A
               C
                                      E                                                                                                                  Cost: 0
                                    8                          1
                                                                                          5                                                                                                                                                I
                                                                                                                                                                                                                 State: F
               3          B                                                                                                              State: B                       State: I                      Cost: 1
                                                                  1               K                                   Cost: 3                       Cost: 9
Start  A            9                             H                                                                           9
                                            4
                1                                                       4
                                                                                    5                                                                                                    State: G                          F
                                                                                                                                                                                                       Cost: 16                                     15       G
                                                                             J
                                                               3





                                                                                      63
```

## Slide 56

```text
Example: Shortest Path



                        2
                                                                            5             Goal                          D       2
                                                                                   L                                                             State: A
               C
                                      E                                                                                                                  Cost: 0
                                    8                          1
                                                                                          5                                                                                                                                                I
                                                                                                                                                                                                                 State: F
               3          B                                                                                                              State: B                       State: I                      Cost: 1
                                                                  1               K                                   Cost: 3                       Cost: 9
Start  A            9                             H                                                                           9
                                            4
                1                                                       4
                                                                                    5                                                                                                    State: G                          F
                                                                                                                                                                                                       Cost: 16                                     15       G                                                                                                                             State: C                        State: E                                                                             J
                                                                                                                       Cost: 4                       Cost: 11
                                                               3





                                                                                      64
```

## Slide 57

```text
Example: Shortest Path



                        2
                                                                            5             Goal                          D       2
                                                                                   L                                                             State: A
               C
                                      E                                                                                                                  Cost: 0
                                    8                          1
                                                                                          5                                                                                                                                                I
                                                                                                                                                                                                                 State: F
               3          B                                                                                                              State: B                       State: I                      Cost: 1
                                                                  1               K                                   Cost: 3                       Cost: 9
Start  A            9                             H                                                                           9
                                            4
                1                                                       4
                                                                                    5                                                                                                    State: G                          F
                                                                                                                                                                                                       Cost: 16                                     15       G                                                                                                                             State: C                        State: E                                                                             J
                                                                                                                       Cost: 4                       Cost: 11
                                                               3



                                                                                                               State: D
                                                                                                           Cost: 6





                                                                                      65
```

## Slide 58

```text
Example: Shortest Path



                        2
                                                                            5             Goal                          D       2
                                                                                   L                                                             State: A
               C
                                      E                                                                                                                  Cost: 0
                                    8                          1
                                                                                          5                                                                                                                                                I
                                                                                                                                                                                                                 State: F
               3          B                                                                                                              State: B                       State: I                      Cost: 1
                                                                  1               K                                   Cost: 3                       Cost: 9
Start  A            9                             H                                                                           9
                                            4
                1                                                       4
                                                                                    5                                                                                                    State: G                          F
                                                                                                                                                                                                       Cost: 16                                     15       G                                                                                                                             State: C                        State: E                                                                             J
                                                                                                                       Cost: 4                       Cost: 11
                                                               3



                                                                                                               State: D
                                                                                                           Cost: 6





                                                                                      66
```

## Slide 59

```text
Example: Shortest Path



                        2
                                                                            5             Goal                          D       2
                                                                                   L                                                             State: A
               C
                                      E                                                                                                                  Cost: 0
                                    8                          1
                                                                                          5                                                                                                                                                I
                                                                                                                                                                                                                 State: F
               3          B                                                                                                              State: B                       State: I                      Cost: 1
                                                                  1               K                                   Cost: 3                       Cost: 9
Start  A            9                             H                                                                           9
                                            4
                1                                                       4
                                                                                    5                                                                                                    State: G                          F
                                                                                                                                                                                                       Cost: 16                                     15       G                                                                                                                             State: C                        State: E                                                                             J
                                                                                                                       Cost: 4                       Cost: 11
                                                               3



                                                                                                                                                                    State: H                                                                                                               State: D                                                                                                                                                                                                 State: J                                                                                                                                                            Cost: 10                                                                                                           Cost: 6                                                                                                                                                                                      Cost: 18





                                                                                      67
```

## Slide 60

```text
Example: Shortest Path



                        2
                                                                            5             Goal                          D       2
                                                                                   L                                                             State: A
               C
                                      E                                                                                                                  Cost: 0
                                    8                          1
                                                                                          5                                                                                                                                                I
                                                                                                                                                                                                                 State: F
               3          B                                                                                                              State: B                       State: I                      Cost: 1
                                                                  1               K                                   Cost: 3                       Cost: 9
Start  A            9                             H                                                                           9
                                            4
                1                                                       4
                                                                                    5                                                                                                    State: G                          F
                                                                                                                                                                                                       Cost: 16                                     15       G                                                                                                                             State: C                        State: E                                                                             J
                                                                                                                       Cost: 4                       Cost: 11
                                                               3



                                                                                                                                                                    State: H                                                                                                               State: D                                                                                                                                                                                                 State: J                                                                                                                                                            Cost: 10                                                                                                           Cost: 6                                                                                                                                                                                      Cost: 18



                                                                                                                                                 State: F                       State: G
                                                                                                                                          Cost: 14                     Cost: 14





                                                                                      68
```

## Slide 61

```text
Example: Shortest Path



                        2
                                                                            5             Goal                          D       2
                                                                                   L                                                             State: A
               C
                                      E                                                                                                                  Cost: 0
                                    8                          1
                                                                                          5                                                                                                                                                I
                                                                                                                                                                                                                 State: F
               3          B                                                                                                              State: B                       State: I                      Cost: 1
                                                                  1               K                                   Cost: 3                       Cost: 9
Start  A            9                             H                                                                           9
                                            4
                1                                                       4                                                                                    5
                          F
                                     15       G                                                                                                                             State: C                        State: E                                                                             J
                                                                                                                       Cost: 4                       Cost: 11
                                                               3



                                                                                                                                                                    State: H                                                                                                               State: D                                                                                                                                                                                                 State: J                                                                                                                                                            Cost: 10                                                                                                           Cost: 6                                                                                                                                                                                      Cost: 18




                                                                                                                                                                               State: G
                                                                                                                                                                      Cost: 14





                                                                                      69
```

## Slide 62

```text
Example: Shortest Path



                        2
                                                                            5             Goal                          D       2
                                                                                   L                                                             State: A
               C
                                      E                                                                                                                  Cost: 0
                                    8                          1
                                                                                          5                                                                                                                                                I
                                                                                                                                                                                                                 State: F
               3          B                                                                                                              State: B                       State: I                      Cost: 1
                                                                  1               K                                   Cost: 3                       Cost: 9
Start  A            9                             H                                                                           9
                                            4
                1                                                       4                                                                                    5
                          F
                                     15       G                                                                                                                             State: C                        State: E                                                                             J
                                                                                                                       Cost: 4                       Cost: 11
                                                               3



                                                                                                                                          State: D                  State: H                                                                                                               State: D                                                                                                                                                                                                 State: J                                                                                                                                   Cost: 13                 Cost: 10                                                                                                           Cost: 6                                                                                                                                                                                      Cost: 18




                                                                                                                                                                               State: G
                                                                                                                                                                      Cost: 14





                                                                                      70
```

## Slide 63

```text
Example: Shortest Path



                        2
                                                                            5             Goal                          D       2
                                                                                   L                                                             State: A
               C
                                      E                                                                                                                  Cost: 0
                                    8                          1
                                                                                          5                                                                                                                                                I
                                                                                                                                                                                                                 State: F
               3          B                                                                                                              State: B                       State: I                      Cost: 1
                                                                  1               K                                   Cost: 3                       Cost: 9
Start  A            9                             H                                                                           9
                                            4
                1                                                       4                                                                                    5
                          F
                                     15       G                                                                                                                             State: C                        State: E                                                                             J
                                                                                                                       Cost: 4                       Cost: 11
                                                               3



                                                                                                                                                                    State: H                                                                                                               State: D                                                                                                                                                                                                 State: J                                                                                                                                                            Cost: 10                                                                                                           Cost: 6                                                                                                                                                                                      Cost: 18




                                                                                                                                                                               State: G
                                                                                                                                                                      Cost: 14





                                                                                      71
```

## Slide 64

```text
Example: Shortest Path



                        2
                                                                            5             Goal                          D       2
                                                                                   L                                                             State: A
               C
                                      E                                                                                                                  Cost: 0
                                    8                          1
                                                                                          5                                                                                                                                                I
                                                                                                                                                                                                                 State: F
               3          B                                                                                                              State: B                       State: I                      Cost: 1
                                                                  1               K                                   Cost: 3                       Cost: 9
Start  A            9                             H                                                                           9
                                            4
                1                                                       4                                                                                    5
                          F
                                     15       G                                                                                                                             State: C                        State: E                                                                             J
                                                                                                                       Cost: 4                       Cost: 11
                                                               3



                                                                                                                                                                    State: H                                                                                                               State: D                                                                                                                                                                                                 State: J                                                                                                                                                            Cost: 10                                                                                                           Cost: 6                                                                                                                                                                                      Cost: 18




                                                                                                                                                                               State: G
                                                                                                                                                                      Cost: 14



                                                                                                                                                                State: J
                                                                                                                                                       Cost: 17





                                                                                      72
```

## Slide 65

```text
Example: Shortest Path



                        2
                                                                            5             Goal                          D       2
                                                                                   L                                                             State: A
               C
                                      E                                                                                                                  Cost: 0
                                    8                          1
                                                                                          5                                                                                                                                                I
                                                                                                                                                                                                                 State: F
               3          B                                                                                                              State: B                       State: I                      Cost: 1
                                                                  1               K                                   Cost: 3                       Cost: 9
Start  A            9                             H                                                                           9
                                            4
                1                                                       4                                                                                    5
                          F
                                     15       G                                                                                                                             State: C                        State: E                                                                             J
                                                                                                                       Cost: 4                       Cost: 11
                                                               3



                                                                                                                                                                    State: H                                                                                                               State: D
                                                                                                                                                            Cost: 10                                                                                                           Cost: 6





                                                                                                                                                                               State: G
                                                                                                                                                                      Cost: 14



                                                                                                                                                                State: J
                                                                                                                                                       Cost: 17





                                                                                      73
```

## Slide 66

```text
Example: Shortest Path



                        2
                                                                            5             Goal                          D       2
                                                                                   L                                                             State: A
               C
                                      E                                                                                                                  Cost: 0
                                    8                          1
                                                                                          5                                                                                                                                                I
                                                                                                                                                                                                                 State: F
               3          B                                                                                                              State: B                       State: I                      Cost: 1
                                                                  1               K                                   Cost: 3                       Cost: 9
Start  A            9                             H                                                                           9
                                            4
                1                                                       4                                                                                    5
                          F
                                     15       G                                                                                                                             State: C                        State: E                                                                             J
                                                                                                                       Cost: 4                       Cost: 11
                                                               3



                                                                                                                                                                    State: H                                                                                                               State: D
                                                                                                                                                            Cost: 10                                                                                                           Cost: 6





                                                                                                                                                                               State: G
                                                                                                                                                                      Cost: 14



                                                                                                                                                                State: J
                                                                                                                                                       Cost: 17


                                                                                                                                          State: K
                                                                                                                                   Cost: 22



                                                                                      74
```

## Slide 67

```text
Example: Shortest Path



                        2
                                                                            5             Goal                          D       2
                                                                                   L                                                             State: A
               C
                                      E                                                                                                                  Cost: 0
                                    8                          1
                                                                                          5                                                                                                                                                I
                                                                                                                                                                                                                 State: F
               3          B                                                                                                              State: B                       State: I                      Cost: 1
                                                                  1               K                                   Cost: 3                       Cost: 9
Start  A            9                             H                                                                           9
                                            4
                1                                                       4                                                                                    5
                          F
                                     15       G                                                                                                                             State: C                        State: E                                                                             J
                                                                                                                       Cost: 4                       Cost: 11
                                                               3



                                                                                                                                                                    State: H                                                                                                               State: D
                                                                                                                                                            Cost: 10                                                                                                           Cost: 6





                                                                                                                                                                               State: G
                                                                                                                                                                      Cost: 14



                                                                                                                                                                State: J
                                                                                                                                                       Cost: 17


                                                                                                                                          State: K
                                                                                                                                   Cost: 22


                                                                                                                        State: E                                 State: L
                                                                                                                  Cost: 27                               Cost: 27
                                                                                      75
```

## Slide 68

```text
Example: Shortest Path



                        2
                                                                            5             Goal                          D       2
                                                                                   L                                                             State: A
               C
                                      E                                                                                                                  Cost: 0
                                    8                          1
                                                                                          5                                                                                                                                                I
                                                                                                                                                                                                                 State: F
               3          B                                                                                                              State: B                       State: I                      Cost: 1
                                                                  1               K                                   Cost: 3                       Cost: 9
Start  A            9                             H                                                                           9
                                            4
                1                                                       4                                                                                    5
                          F
                                     15       G                                                                                                                             State: C                        State: E                                                                             J
                                                                                                                       Cost: 4                       Cost: 11
                                                               3



                                                                                                                                                                    State: H                                                                                                               State: D
                                                                                                                                                            Cost: 10                                                                                                           Cost: 6





                                                                                                                                                                               State: G
                                                                                                                                                                      Cost: 14



                                                                                                                                                                State: J
                                                                                                                                                       Cost: 17


                                                                                                                                          State: K
                                                                                                                                   Cost: 22



                                                                                                                                                                State: L
                                                                                                                                                        Cost: 27
                                                                                      76
```

## Slide 69

```text
Example: Shortest Path



                        2
                                                                            5             Goal                          D       2
                                                                                   L                                                             State: A
               C
                                      E                                                                                                                  Cost: 0
                                    8                          1
                                                                                          5                                                                                                                                                I
                                                                                                                                                                                                                 State: F
               3          B                                                                                                              State: B                       State: I                      Cost: 1
                                                                  1               K                                   Cost: 3                       Cost: 9
Start  A            9                             H                                                                           9
                                            4
                1                                                       4                                                                                    5
                          F
                                     15       G                                                                                                                             State: C                        State: E                                                                             J
                                                                                                                       Cost: 4                       Cost: 11
                                                               3



                                                                                                                                                                    State: H                                                                                                               State: D
                                                                                                                                                            Cost: 10                                                                                                           Cost: 6





                                                                                                                                                                               State: G
                                                                                                                                                                      Cost: 14



                                                                                                                                                                State: J
                                                                                                                                                       Cost: 17


                                                                                                                                          State: K
                                                                                                                                   Cost: 22



                                                                                                                                                                State: L
                                                                                                                                                        Cost: 27
                                                                                      77
```

## Slide 70

```text
Example: Shortest Path



                        2
                                                                            5             Goal                          D       2
                                                                                   L                                                             State: A
               C
                                      E                                                                                                                  Cost: 0
                                    8                          1
                                                                                          5                                                                                                                                                I
                                                                                                                                                                                                                 State: F
               3          B                                                                                                              State: B                       State: I                      Cost: 1
                                                                  1               K                                   Cost: 3                       Cost: 9
Start  A            9                             H                                                                           9
                                            4
                1                                                       4                                                                                    5
                          F
                                     15       G                                                                                                                             State: C                        State: E                                                                             J
                                                                                                                       Cost: 4                       Cost: 11
                                                               3



                                                                                                                                                                    State: H                                                                                                               State: D
                                                                                                                                                            Cost: 10                                                                                                           Cost: 6





                                                                                                                                                                               State: G
                                                                                                                                                                      Cost: 14



                                                                                                                                                                State: J
                                                                                                                                                       Cost: 17


                                                                                                                                          State: K
                                                                                                                                   Cost: 22



                                                                                                                                                                State: L
                                                                                                                                                        Cost: 27
                                                                                      78
```

## Slide 71

```text
Key Properties of an Algorithm

• Completeness: Are we assured to find a solution, if one
  exists?
• Optimality: How good is the solution?
• Space complexity: How much storage is needed?
• Time complexity: How many operations are needed?





                                                                                    79
```

## Slide 72

```text
Key Properties
  b ⇒branching factor                      ε ⇒minimum (positive) edge cost  d ⇒depth of shallowest solution          C* ⇒optimal path cost  m ⇒maximum depth of the search tree

          BFS     DFS     Uniform

Completeness       Yes           No            Yes*
(finite “b”)

Optimality          Yes           No            Yes
(step costs=1)

Optimality          No           No            Yes
(general costs)
Space                O(bd)          O(bm)           O(bC*/𝝐)
Complexity
Time                 O(bd)           O(bm)           O(bC*/𝝐)
Complexity




                                                                                       80
```

## Slide 73

```text
Depth-Limited Search

Depth-first search, but terminate a path either if a goal state
is found, or if the maximum depth allowed is reached.

Always terminates:
    • Avoids the problem of search never terminating by imposing a hard
      limit on the depth of any search path.

However, it is still not complete (the goal depth may be
greater than the limit allowed.)





                                                                                    81
```

## Slide 74

```text
Iterative Deepening Search

Algorithm: Do depth-limited search, but with increasing
depth.





                                                                                    82
```

## Slide 75

```text
Key Properties
  b ⇒branching factor                      ε ⇒minimum (positive) edge cost  d ⇒depth of shallowest solution          C* ⇒optimal path cost  m ⇒maximum depth of the search tree

          BFS     DFS     Uniform     IDS

Completeness       Yes           No            Yes*           Yes
(finite “b”)

Optimality          Yes           No            Yes           Yes
(step costs=1)

Optimality          No           No            Yes           No
(general costs)
Space                O(bd)          O(bm)           O(bC*/𝝐)         O(bd)
Complexity
Time                 O(bd)           O(bm)           O(bC*/𝝐)          O(bd)
Complexity




                                                                                       83
```

## Slide 76

```text
Generic Search Algorithm





                                                                     84
```

## Slide 77

```text
Generic Search Algorithm

Initialize the search tree with the initial state s0 as root





                                                                                    85
```

## Slide 78

```text
Generic Search Algorithm

Initialize the search tree with the initial state s0 as root

Repeat:
          If no node can be expanded:
        return Failure





                                                                                    86
```

## Slide 79

```text
Generic Search Algorithm

Initialize the search tree with the initial state s0 as root

Repeat:
          If no node can be expanded:
        return Failure

       Choose a node for expansion, using some search strategy





                                                                                    87
```

## Slide 80

```text
Generic Search Algorithm

Initialize the search tree with the initial state s0 as root

Repeat:
          If no node can be expanded:
        return Failure

       Choose a node for expansion, using some search strategy
          If the node is the goal:
        return Corresponding Path
        Else:
       For each applicable action a at the state s of the node:
                      Apply the transition (s, a) -> s’ and add s’ to the tree




                                                                                    88
```

## Slide 81

```text
Generic Search Algorithm

Initialize the search tree with the initial state s0 as root

Repeat:
          If no node can be expanded:
        return Failure

       Choose a node for expansion, using some search strategy
          If the node is the goal:
        return Corresponding Path
        Else:
       For each applicable action a at the state s of the node:
                      Apply the transition (s, a) -> s’ and add s’ to the tree




                                                                                    89
```

## Slide 82

```text
Generic Search Algorithm

Initialize the search tree with the initial state s0 as root

Repeat:
          If no node can be expanded:
                                                 What if we checked
        return Failure                                                            the goal when
                                                           expanding?
       Choose a node for expansion, using some search strategy
                                                                   This is called early vs
          If the node is the goal:                                                                       late goal evaluation.
        return Corresponding Path
        Else:
       For each applicable action a at the state s of the node:
                      Apply the transition (s, a) -> s’ and add s’ to the tree




                                                                                    90
```

## Slide 83

```text
Generic Search Algorithm

Initialize the search tree with the initial state s0 as root

Repeat:
          If no node can be expanded:
        return Failure

       Choose a node for expansion, using some search strategy
          If the node is the goal:
        return Corresponding Path
        Else:
       For each applicable action a at the state s of the node:
                      Apply the transition (s, a) -> s’ and add s’ to the tree
                               How to deal with revisiting a
                                               state during expansion?

                                                                                    91
```

## Slide 84

```text
Quick Detour: Implementation Details

• Defining a search tree node:
    • A state from the planning problem
    • Additional information needed by the algorithm:
          • The parent state pointer and the action used to generate it
          • Cost of the path so far
          • Depth of the node
• Tree edges:
    • Correspond to the actions taken
    • Record of edges followed lives in node back pointers





                                                                                    92
```

## Slide 85

```text
Quick Detour: Implementation Details

• Search methods proceed by expanding a search tree node:
    • Start from a selected search tree node
    • Apply all legal operators to the state
    • Generating new nodes for all the corresponding successor states
• Critical property of expansion:
    • The nodes resulting from the action remain un-expanded until the
      algorithm later selects them. They must be stored somewhere.





                                                                                    93
```

## Slide 86

```text
Quick Detour: Implementation Details

• Need to keep track of the nodes to be expanded:
    • the frontier of open nodes.
• Implement this using a queue:





                                                                                    94
```

## Slide 87

```text
Quick Detour: Implementation Details

• Need to keep track of the nodes to be expanded:
    • the frontier of open nodes.
• Implement this using a queue:


    Initialize the queue with the initial state s0 node
   Repeat:
                   If queue is empty:
               return Failure
            Dequeue a node
                   If the node is the goal:
               return Corresponding Path
               Else:
             For each applicable action a at the state s of the node:
                                 Apply the transition (s, a) -> s’ and add s’ to the queue





                                                                                    95
```

## Slide 88

```text
Quick Detour: Implementation Details

• Need to keep track of the nodes to be expanded:
    • the frontier of open nodes.
• Implement this using a queue:


    Initialize the queue with the initial state s0 node
   Repeat:
                   If queue is empty:
               return Failure
            Dequeue a node
                   If the node is the goal:
               return Corresponding Path
               Else:
             For each applicable action a at the state s of the node:
                                 Apply the transition (s, a) -> s’ and add s’ to the queue

Search algorithms differ in their queuing function.


                                                                                    96
```

## Slide 89

```text
Assumptions (for next few lectures)

• Static                   (c.f. dynamic) environment
• Observable           (c.f. unobservable) environment
• Discrete                (c.f. continuous) states
• Deterministic         (c.f. stochastic) environment

Today: simplified assumptions. Later, we will consider search
in other settings.





                                                                                    97
```

## Slide 90

```text
Recap

•  Search in AI: Knowledge representation with state space
  models

•  State space graphs and search trees

• A generic search algorithm: The ‘expansion’ operation

•  Uninformed search:
      •  BFS, DFS, Uniform, IDS





                                                                                   98
```

## Slide 91

```text
The Goal Today
BFS                                     DFS





                       IDS





                                                                     99
```

## Slide 92

```text
The Goal Today
BFS                                     DFS





                       IDS





                                                                  100
```

## Slide 93

```text
Next class

•  Informed search

•  Starting next week (Sept 9), we'll be in MCMED 522!





                                                                                101
```
