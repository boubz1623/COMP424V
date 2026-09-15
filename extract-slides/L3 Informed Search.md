# L3 Informed Search

> Source: [original PDF](<../slides/L3 Informed Search.pdf>) · 66 slides. Text extraction may omit figures and alter equations; check the PDF.

## Slide 1

```text
COMP 424 - Artificial Intelligence
             Fall 2026


          Lecture 3: September 9th, 2026
                Informed Search

     Su Lin Blodgett (sulin.blodgett@mcgill.ca)
     Jackie CK Cheung (jackie.cheung@mcgill.ca)
```

## Slide 2

```text
Uninformed Searches

•  Breadth-First Search
•  Depth-First Search
•  Uniform Cost Search
•  Iterative Deepening Search





                                                                                  2
```

## Slide 3

```text
Key Properties
  b ⇒branching factor  d ⇒depth of shallowest solution  m ⇒maximum depth of the search tree

          BFS     DFS     Uniform

Completeness       Yes           No            Yes*
(finite “b”)

Optimality          Yes           No            Yes
(step costs=1)

Optimality          No           No            Yes
(general costs)

Space                O(bd)          O(bm)             O(bC*/ε)
Complexity

Time                 O(bd)           O(bm)             O(bC*/ε)
Complexity




                                                                                      3
```

## Slide 4

```text
Breadth-First Search vs Depth-First Search





                                                                                             Goal!





                                                                                  4
```

## Slide 5

```text
Breadth-First Search vs Depth-First Search





                                                                                             Goal!





                               BFS





                                                                                  5
```

## Slide 6

```text
Breadth-First Search vs Depth-First Search





                                                                                             Goal!





                               BFS
Time complexity = 1 + 2 + 4 + 8 + 16
              = 20 + 21+ 22+ 23+ 24
                         = O(24)
                         = O(bd)
                                                                                  6
```

## Slide 7

```text
Breadth-First Search vs Depth-First Search





                                                                                             Goal!





                                                                                  7
```

## Slide 8

```text
Breadth-First Search vs Depth-First Search





                                                                                             Goal!





                             DFS





                                                                                  8
```

## Slide 9

```text
Breadth-First Search vs Depth-First Search





                                                                                                 Goal!





                                 DFS

Time complexity = 1 + 2 + 4 + 8 + 16 + (32-2) + (64-4)
                               = O(26)
                               = O(bm)

                                                                                      9
```

## Slide 10

```text
Key Properties
  b ⇒branching factor                      ε ⇒minimum graph edge cost  d ⇒depth of shallowest solution          C* ⇒optimal path cost  m ⇒maximum depth of the search tree

          BFS     DFS     Uniform

Completeness       Yes           No            Yes*
(finite “b”)

Optimality          Yes           No            Yes
(step costs=1)

Optimality          No           No            Yes
(general costs)

Space                O(bd)          O(bm)             O(bC*/ε)
Complexity

Time                 O(bd)           O(bm)             O(bC*/ε)
Complexity




                                                                                       10
```

## Slide 11

```text
Example: Uniform Cost Search


                   2
                  D                               5             Goal                                2
                                                         L                                       State: A
          C
                          E                                                                          Cost: 0
                            8                    1
                                                                     5                                                                                                   I
            3      B
                                                   1                                              K
Start  A         9                                H          9
                                  4            1                                          4                                                                 5                  F
                           15     G
                                                     J
                                                3





                                                                                      11
```

## Slide 12

```text
Example: Uniform Cost Search


                   2
                  D                               5             Goal                                2
                                                         L                                       State: A
          C
                          E                                                                          Cost: 0
                            8                    1
                                                                     5                                                                                                   I                                                                                                                                        State: F
            3      B                                                                      State: B             State: I             Cost: 1                                                   1                                              K                      Cost: 3             Cost: 9Start  A         9                                H          9
                                  4            1                                          4                                                                 5                  F
                           15     G
                                                     J
                                                3





                                                                                      12
```

## Slide 13

```text
Example: Uniform Cost Search


                   2
                  D                               5             Goal                                2
                                                         L                                       State: A
          C
                          E                                                                          Cost: 0
                            8                    1
                                                                     5                                                                                                   I                                                                                                                                        State: F
            3      B                                                                      State: B             State: I             Cost: 1                                                   1                                              K                      Cost: 3             Cost: 9Start  A         9                                H          9
                                  4            1                                          4                                                                 5                                                                State: G                  F
                           15     G                                                                                           Cost: 16
                                                     J
                                                3





                                                                                      13
```

## Slide 14

```text
Example: Uniform Cost Search


                   2
                  D                               5             Goal                                2
                                                         L                                       State: A
          C
                          E                                                                          Cost: 0
                            8                    1
                                                                     5                                                                                                   I                                                                                                                                        State: F
            3      B                                                                      State: B             State: I             Cost: 1                                                   1                                              K                      Cost: 3             Cost: 9Start  A         9                                H          9
                                  4            1                                          4                                                                 5                                                                State: G                  F
                                                                                                                                    Cost: 16                           15     G                                      State: C             State: E                                                     J
                                                                              Cost: 4             Cost: 11                                                3





                                                                                      14
```

## Slide 15

```text
Example: Uniform Cost Search


                   2
                  D                               5             Goal                                2
                                                         L                                       State: A
          C
                          E                                                                          Cost: 0
                            8                    1
                                                                     5                                                                                                   I                                                                                                                                        State: F
            3      B                                                                      State: B             State: I             Cost: 1                                                   1                                              K                      Cost: 3             Cost: 9Start  A         9                                H          9
                                  4            1                                          4                                                                 5                                                                State: G                  F
                                                                                                                                    Cost: 16                           15     G                                      State: C             State: E                                                     J
                                                                              Cost: 4             Cost: 11                                                3


                                                                        State: D
                                                                      Cost: 6





                                                                                      15
```

## Slide 16

```text
Example: Uniform Cost Search


                   2
                  D                               5             Goal                                2
                                                         L                                       State: A
          C
                          E                                                                          Cost: 0
                            8                    1
                                                                     5                                                                                                   I                                                                                                                                        State: F
            3      B                                                                      State: B             State: I             Cost: 1                                                   1                                              K                      Cost: 3             Cost: 9Start  A         9                                H          9
                                  4            1                                          4                                                                 5                  F
                           15     G                                      State: C             State: E                                                     J
                                                                              Cost: 4             Cost: 11                                                3


                                                                                                          State: H                                                                        State: D
                                                                                                      Cost: 10                                                                      Cost: 6



                                                                                                                  State: G
                                                                                                              Cost: 14

                                                                                                        State: J
                                                                                                    Cost: 17

                                                                                         State: K
                                                                                      Cost: 22


                                                                                                        State: L
                                                                                                     Cost: 27
                                                                                      16
```

## Slide 17

```text
Key Properties
  b ⇒branching factor                      ε ⇒minimum graph edge cost  d ⇒depth of shallowest solution          C* ⇒optimal path cost  m ⇒maximum depth of the search tree

          BFS     DFS     Uniform     IDS

Completeness       Yes           No            Yes*           Yes
(finite “b”)

Optimality          Yes           No            Yes           Yes
(step costs=1)

Optimality          No           No            Yes           No
(general costs)

Space                O(bd)          O(bm)             O(bC*/ε)          O(bd)
Complexity

Time                 O(bd)           O(bm)             O(bC*/ε)           O(bd)
Complexity




                                                                                       17
```

## Slide 18

```text
Iterative Deepening Search

Algorithm: Do depth-limited search, but with increasing
depth.





                                                                                    18
```

## Slide 19

```text
Iterative Deepening Search





                                                                                 Goal!





                                                                       19
```

## Slide 20

```text
Iterative Deepening Search





                                                                                 Goal!





                                                                       20
```

## Slide 21

```text
Iterative Deepening Search





                                                                                 Goal!





                                                                       21
```

## Slide 22

```text
Iterative Deepening Search





                                                                                 Goal!





                                                                       22
```

## Slide 23

```text
Iterative Deepening Search





                                                                                 Goal!





                                                                       23
```

## Slide 24

```text
Iterative Deepening Search





                                                                                 Goal!





                                                                       24
```

## Slide 25

```text
Iterative Deepening Search





                                                                                 Goal!





                                                                       25
```

## Slide 26

```text
Questions

•  Iterative Deepening Search:
   o Why isn't the time complexity larger? Isn't there a lot of repetition?

•  Uniform Cost Search:
   o Why the asterisk for completeness?

   o What happens to optimality if edge weights are negative?
         ▪  Can this be fixed by adding a positive constant to all edges?

   o Why is space complexity the same as time complexity?

   o  What's the relationship between UCS and BFS?

   o Why is uniform cost search called "uniform"?



                                                                                   26
```

## Slide 27

```text
Example: Shortest Path


                   2
                  D                               5             Goal                                2
                                                         L                                       State: A
          C
                          E                                                                          Cost: 0
                            8                    1
                                                                     5                                                                                                   I                                                                                                                                        State: F
            3      B                                                                      State: B             State: I             Cost: 1                                                   1                                              K                      Cost: 3             Cost: 9Start  A         9                                H          9
                                  4            1                                          4                                                                 5                                                                State: G                  F
                                                                                                                                    Cost: 16                           15     G                                      State: C             State: E                                                     J
                                                                              Cost: 4             Cost: 11                                                3


                                                                        State: D
                                                                      Cost: 6





                                                                                      29
```

## Slide 28

```text
Questions

•  Iterative Deepening Search:
   o Why isn't the time complexity larger? Isn't there a lot of repetition?

•  Uniform Cost Search:
   o Why the asterisk for completeness?

   o What happens to optimality if edge weights are negative?
         ▪  Can this be fixed by adding a positive constant to all edges?

   o Why is space complexity the same as time complexity?

   o  What's the relationship between UCS and BFS?

   o Why is uniform cost search called "uniform"?



                                                                                   30
```

## Slide 29

```text
Example: Shortest Path


                   2
                  D                               5             Goal                                2
                                                         L                                       State: A
          C
                          E                                                                          Cost: 0
                            8                    1
                                                                     5                                                                                                   I
                                                                                                                                        State: F            3      B                                                                      State: B             State: I                                                                                                                                    Cost: 1                                                   1                                              K                      Cost: 3             Cost: 9Start  A         9                                H          9
                                  4            1                                          4                                                                 5                                                                 State: G                  F
                           15     G                                         State: C              State: E                          Cost: 16                                                     J
                                                                                     Cost: 4             Cost: 11                                                3

                                                                        State: D         State: D         State: H                                                                                                                              State: J
                                                                      Cost: 6          Cost: 13        Cost: 10                                                                                                                          Cost: 18


                                                                                              State: F            State: G
                                                                                           Cost: 14            Cost: 14

                                                                                                        State: J
                                                                                                    Cost: 17

                                                                                         State: K
                                                                                      Cost: 22

                                                                              State: E                   State: L
                                                                           Cost: 27                  Cost: 27
                                                                                      32
```

## Slide 30

```text
Uninformed Search





UCS, the good: Complete* and optimal*
UCS, less good: Explores options in every "direction"; no info about goal location


                                                                           Québec                                                               257
                                                                                                      City                                         199                            ...   Vancouver                    Ottawa          Montréal
                                                         156156
                                                                     Sherbrooke


                                                                                     34
```

## Slide 31

```text
Example Heuristic: Driving to Vancouver

   • What is a reasonable heuristic?
    o  i.e., What is a reasonable estimate of how close a state is to our goal?
    o  h(n) = straight-line distance
   •  Is it always right?
    o No – actual distances driven can be much longer
    o But still helpful!


                                                                             QuébecQuébec                                                                 257257
                                                                                                        CityCity                                          199199                               ......     VancouverVancouver                    OttawaOttawa          MontréalMontréal
                                                           156156156
                                                                       SherbrookeSherbrooke





                                                                                       38
```

## Slide 32

```text
Example Heuristic: Eight-Puzzle

• What would be a good heuristic for this problem?
       •   h1(n) = number of misplaced tiles                                        Sum of horizontal and
                                                                     vertical moves needed to       •   h2(n) = Manhattan distance
                                                       reach the target position
                                                                   (think moving on city blocks)





                                                                                    40
```

## Slide 33

```text
Where do heuristics come from?





                                                                            41
```

## Slide 34

```text
Best-First Search

•  Algorithm: expand the most promising node according to
  the heuristic.

•  Example:


     • Numbers on edges indicate the edge/operator cost, notations
      below the nodes ”h=…” give the heuristic value





                                                                                    43
```

## Slide 35

```text
Best-First Search



                                                                         Start
                                                                        h: 4





                                                            44
```

## Slide 36

```text
Best-First Search



                                                                         Start
                                                                        h: 4



                                                  A
                                                                      h: 3





                                                            45
```

## Slide 37

```text
Best-First Search



                                                                         Start
                                                                        h: 4



                                                  A
                                                                      h: 3



                                     B                         C
                                                h: 2                              h: 1





                                                            46
```

## Slide 38

```text
Best-First Search



                                                                         Start
                                                                        h: 4



                                                  A
                                                                      h: 3



                                     B                         C
                                                h: 2                              h: 1




                                                              Goal
                                                                        h: 0





                                                            47
```

## Slide 39

```text
Best-First Search



                                                                         Start
                                                                        h: 4



                                                  A
                                                                      h: 3



                                     B                         C
                                                h: 2                              h: 1




                                                              Goal
                                                                        h: 0





                                                            48
```

## Slide 40

```text
Best-First Search

•  Algorithm: expand the most promising node according to
  the heuristic.

•  Example:


     • What is the sequence of nodes visited in Best-First Search?
        START -> A -> C -> GOAL                                                   Cost is 2+4+2=8
     • What about this?
        START -> A -> B -> C -> GOAL                     vs

                                              2+1+1+2=6

                                                       Proof that Best-First
                                                 Search is not optimal

                                                                                    49
```

## Slide 41

```text
Fixing Best-First Search

•  What’s the problem with best-first search?
      •   It does not consider the cost so far!!

•  Let’s use both
      •   g(n): Cost of path from the start to the node
      •   h(n): Heuristic cost of the path from the node to the goal

                                    h = 1
                            A
                      10

                 Start                                 Goal

                      50
                             B
                                    h = 1

                                                                                   50
```

## Slide 42

```text
Fixing Best-First Search

•  What’s the problem with best-first search?
      •   It does not consider the cost so far!!

•  Let’s use both
      •   g(n): Cost of path from the start to the node
      •   h(n): Heuristic cost of the path from the node to the goal

•  A* search: greedy with respect to f(n) = g(n) + h(n)
      •  Using only g(n) → Uniform cost search
         ▪  Orders by path cost, or backward cost
      •  Using only h(n) → Best-first search
         ▪  Orders by distance to goal, or forward cost





                                                                                   52
```

## Slide 43

```text
A* search

•





                                                                                    53
```

## Slide 44

```text
A* search


                                                                                              Start
                                                                                                   g: 0
                                                                                            h: 4
                                                                                                                               f: 0+4 = 4



f(n) = g(n) + h(n)





                                                                          54
```

## Slide 45

```text
A* search


                                                                                              Start
                                                                                                   g: 0
                                                                                            h: 4
                                                                                                                               f: 0+4 = 4


                                                                A
                                                                                                   g: 2
                                                                                            h: 3
                                                                                                                              f: 2+3 = 5
f(n) = g(n) + h(n)





                                                                          55
```

## Slide 46

```text
A* search


                                                                                              Start
                                                                                                   g: 0
                                                                                            h: 4
                                                                                                                               f: 0+4 = 4


                                                                A
                                                                                                   g: 2
                                                                                            h: 3
                                                                                                                              f: 2+3 = 5
f(n) = g(n) + h(n)                                                    B
                                                                          g: 3                                                                                  C
                                                                     h: 2                                                                                                               g: 6
                                                                                              f: 3+2 = 5                                                                                                       h: 1
                                                                                                                                               f: 6+1 = 7





                                                                          56
```

## Slide 47

```text
A* search


                                                                                              Start
                                                                                                   g: 0
                                                                                            h: 4
                                                                                                                               f: 0+4 = 4


                                                                A
                                                                                                   g: 2
                                                                                            h: 3
                                                                                                                              f: 2+3 = 5
f(n) = g(n) + h(n)                                                    B
                                                                          g: 3                                                                                  C
                                                                     h: 2                                                                                                               g: 6
                                                                                              f: 3+2 = 5                                                                                                       h: 1
                                                                                                                                               f: 6+1 = 7

                                              C
                                                              g: 4
                                                          h: 1
                                                                             f: 4+1 = 5





                                                                          57
```

## Slide 48

```text
A* search


                                                                                              Start
                                                                                                   g: 0
                                                                                            h: 4
                                                                                                                               f: 0+4 = 4


                                                                A
                                                                                                   g: 2
                                                                                            h: 3
                                                                                                                              f: 2+3 = 5
f(n) = g(n) + h(n)                                                    B
                                                                          g: 3
                                                                     h: 2
                                                                                              f: 3+2 = 5


                                              C
                                                              g: 4
                                                          h: 1
                                                                             f: 4+1 = 5





                                                                          58
```

## Slide 49

```text
A* search


                                                                                              Start
                                                                                                   g: 0
                                                                                            h: 4
                                                                                                                               f: 0+4 = 4


                                                                A
                                                                                                   g: 2
                                                                                            h: 3
                                                                                                                              f: 2+3 = 5
f(n) = g(n) + h(n)                                                    B
                                                                          g: 3
                                                                     h: 2
                                                                                              f: 3+2 = 5


                                              C
                                                              g: 4
                                                          h: 1
                                                                             f: 4+1 = 5



                                      Goal
                                                g: 6
                                             h: 0
                                                            f: 6+0 = 6
                                                                          59
```

## Slide 50

```text
A* search


                                                                                              Start
                                                                                                   g: 0
                                                                                            h: 4
                                                                                                                               f: 0+4 = 4


                                                                A
                                                                                                   g: 2
                                                                                            h: 3
                                                                                                                              f: 2+3 = 5
f(n) = g(n) + h(n)                                                    B
                                                                          g: 3
                                                                     h: 2
                                                                                              f: 3+2 = 5


                                              C
                                                              g: 4
                                                          h: 1
                                                                             f: 4+1 = 5



                                      Goal
                                                g: 6
                                             h: 0
                                                            f: 6+0 = 6
                                                                          60
```

## Slide 51

```text
When Is A* Optimal?


                                    h = 6
                            A
                      1                  3

                 Start                                 Goal
                               5                                                     h = 0

•  Optimal path: Start -> A -> Goal
•  Path from A*: Start -> Goal
•  What went wrong?
   o  Estimate of good path cost (1 + 6) > actual bad path cost (5)
•  Need h(A) to be no greater than cost(A, Goal)




                                                                                   62
```

## Slide 52

```text
Properties of Heuristic

•  Admissibility: The heuristic is always ‘optimistic’   h(s) ≤ h*(s) ∀s, where h*(s) is the true cost to the nearest
   goal
   o  i.e., it never overestimates
   o  Driving to Vancouver: is the straight-line distance
      admissible?

•  Consistency: The heuristic gets more ‘precise’ as it gets
   closer to the goal   h(s) ≤ c(s, s’) + h(s’) ∀s,s’ where ∃edge from s to s’





                                                                                   64
```

## Slide 53

```text
Properties of Heuristic

•  Admissibility: The heuristic is always ‘optimistic’   h(s) ≤h*(s) ∀s, where h*(s) is the true cost to the nearest
   goal

  Needed for optimality


•  Consistency: The heuristic gets more ‘precise’ as it gets
   closer to the goal   h(s) ≤c(s, s’) + h(s’) ∀s,s’ where ∃edge from s to s’

                                                      s'



                    s                                   g

                                                                                   66
```

## Slide 54

```text
Properties of Heuristic

•  Admissibility: The heuristic is always ‘optimistic’   h(s) ≤ h*(s) ∀s, where h*(s) is the true cost to the nearest
   goal

  Needed for optimality


•  Consistency: The heuristic gets more ‘precise’ as it gets
   closer to the goal   h(s) ≤ c(s, s’) + h(s’) ∀s,s’ where ∃edge from s to s’
   o  This means that for a graph with all costs c(s,s') > 0, f cannot
       decrease along any path:
            f(s) = g(s) + h(s) ≤ g(s) + c(s,s’) + h(s’) = f(s’)
   o  Stronger than admissibility


                                                                                   67
```

## Slide 55

```text
Admissibility and Optimality for A*

•   If A* selects a path p, then p is the lowest-cost path.
•  Proof by contradiction. Suppose another path p' is actually the
   shortest path to a goal.
•  Consider the moment just before p is chosen from the frontier.
  Some part of path p' will also be on the frontier (because p is
  expanded before p'). Call this partial path p''.
•  Because p is expanded before p'', f(p) ≤ f(p'') --
    i.e., g(p) + h(p) ≤ g(p'') + h(p'').
•  Because p is a goal, h(p) = 0. Thus g(p) ≤ g(p'') + h(p'').
•  Because h is admissible, g(p'') + h(p'') ≤ g(p') for any path p' to a
   goal that extends p''.
•  Thus g(p) ≤ g(p'') + h(p'') ≤g(p'). This contradicts our assumption
   that p' is the shortest path.
                                                                                           Proof statement: Kevin Leyton-Brown      68
```

## Slide 56

```text
Statements you can try to prove →

•  Consistency is a stronger property than admissibility


•  Consistency guarantees completeness (it's not required, but
    it's an easy way to get it)


• A heuristic created by solving a relaxed version of the problem
   will always be admissible, and will usually be consistent (if the
   relaxed problem formulation respects triangle inequality)





                                                                                     71
```

## Slide 57

```text
Dominance
•   If          ∀n (both heuristics are admissible)     h1(n) ≤h2(n)
      then h2 dominates h1



                    Goal
          to


                                                                             h*                                        Distance
                                                                                    h2

                                                                                  h1

                                         States


                                                                                     73
```

## Slide 58

```text
Dominance

 • Why does this matter?
    o We want as large an h as possible, or as tight a bound as possible
                                      h(a) = 50              f(b) = g(b) + h(b) = 100 + 20 = 120
                                                                           f(a) = g(a) + h(a) = 60 + 50 = 110                             a
                                    75                   60                                                      h(b) = 20

              s                                b               gh(s) = 100                                                     20                           100

                                      h(a) = 65              f(b) = g(b) + h(b) = 100 + 20 = 120
                                                                           f(a) = g(a) + h(a) = 60 + 65 = 125                              a
                                    75                   60                                                      h(b) = 20

               s                                b               gh(s) = 100                                                     20                           100

                                                                                       77
```

## Slide 59

```text
Example heuristic: eight-puzzle

• What would be a good heuristic for this problem?
       •   h1(n) = number of misplaced tiles = 7
       •   h2(n) = manhattan distance = 4+2+2+2+2+3+3=18





                                                                                    78
```

## Slide 60

```text
Combining Heuristics

•   If h3(n) = max(h1(n), h2(n)) dominates both h1 and h2




                    Goal
          to


                                                                             h*                                        Distance
                                                                                    h2

                                                                                  h1

                                         States


                                                                                     81
```

## Slide 61

```text
Properties of A*

•





                                                                                    82
```

## Slide 62

```text
Iterative Deepening A* (IDA*)

•  Depth-first search to avoid memory concerns.
•  But use an f-value limit, rather than a depth limit.

•  IDA* has the same properties as A* but uses less memory.
•  In order to avoid always expanding new nodes, old ones
  can be remembered if memory permits (this version is
  known as Simplified Memory-bounded A*, SMA*)





                                                                                    85
```

## Slide 63

```text
Learning Heuristic Functions

•





                          This is enrichment material, not testable. However, it
                       can easily be a component of the project submission,
                      and help in real-world AI projects!


                                                                                    86
```

## Slide 64

```text
Recap

•  Iterative Deepening Search (IDS)

•  Uninformed Search vs Informed Search
      •   Heuristics

•  Best-First Search and A* Search

•  Properties of Heuristics
      •   Admissibility and Consistency
      •  Dominance

•  Iterative Deepening A*





                                                                                   87
```

## Slide 65

```text
The Goal Today
BFS                                     DFS





IDS                                   A*





                                                                     88
```

## Slide 66

```text
Next Class

•  Search for Optimization





                                                                                   89
```
