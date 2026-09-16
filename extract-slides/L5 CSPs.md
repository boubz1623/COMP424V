# L5 CSPs

> Source: [original PDF](<../slides/L5 CSPs.pdf>) · 71 slides. Text extraction may omit figures and alter equations; check the PDF.

## Slide 1

```text
COMP 424 - Artificial Intelligence
 Constraint Satisfaction Problems




          Lecture 5: September 16th, 2026

     Su Lin Blodgett (sulin.blodgett@mcgill.ca)
     Jackie CK Cheung (jackie.cheung@mcgill.ca)
```

## Slide 2

```text
Announcements

•  Check Ed for announcements on midterm time, A1
  handout.

•  Submit assignments through MyCourses!





                                                                                   2
```

## Slide 3

```text
Recap: Local search and optimization

• Two distinctions drawn compared to previously:
    •  Problem: Often, interested in best state according to evaluation
       function (optimization problem); less interested in path to that state
    •  Search strategy: Start with some initial solution, then employ some
        strategy to gradually improve it; not searching systematically

•  Apply a local search and move in a promising direction.
    •   Hill climbing always moves in the (locally) best direction
    •  Simulated annealing allows some moves towards worse solutions
    •  Parallelism and beam search can be exploited to improve results;
        find a better local optimum
    •  Genetic algorithms are an alternative related to simulated annealing
      which has an analogy to biological evolution


                                                                                  3
```

## Slide 4

```text
Hill climbing

•  Start from an initial configuration X0 with value E(X0)
   X X0, and E E(X0)
•  Repeat until satisfied:
      •  Generate the set of neighbours of Xiand their value E(Xi).
      •  Let Emax = maxi E(Xi) be the value of the best neighbour,
            i* = argmaxi E(Xi) be the index of the best neighbour.
      •    if Emax E:
            return X                  (we are at an optimum)
      •   else:
            let X Xi*, and E Emax.    (take a greedy step)

 •  Can get stuck in a local maximum or plateau!



                                                                                   4
```

## Slide 5

```text
Simulated annealing

•  Idea: allow some "bad" moves to try to escape local maxima
     •  Decrease size and frequency of "bad moves" over time

•  Start from an initial configuration X0 with value E(X0).
   X X0, and E E(X0)
•  Repeat until satisfied:
    •  Let Xibe a random neighbour of X with value E(Xi).
    •  If Ei > E, let Xi*Xi and let E Ei (we found a new better solution).
    •  Else, with some probability p, still accept the move: XXi and E Ei .

• What value to use for p?
    •  p = e-(E-Ei)/T
    • We gradually decrease the value of the temperature T across iterations.


                                                                                   5
```

## Slide 6

```text
Local beam search

•  Keep track of k states rather than just one state
•  Algorithm:
      •  Begin with k randomly generated states
      •  At each step, generate all the neighbours of the k states
         ▪    If one is a goal, terminate and return that state
         ▪  Otherwise, keep the top k solutions across all the neighbours,
             discard the remaining
      •  k is called the beam width





                                                                                  6
```

## Slide 7

```text
Genetic algorithms

• A candidate solution is called an individual.
      •   In a traveling salesman problem, an individual is a tour
•  Each individual has a fitness scored by a fitness function.
• A set of individuals is called a population.
•  Populations change over generations, by applying operations
   to individuals.
      •  operations = {mutation, crossover, selection}
      •   probability of selection is proportional to fitness score
•  Individuals with higher fitness are more likely to survive &
   reproduce.
•  Individual can be represented by a binary string:
      •  Allows operations to be carried out easily.



                                                                                  7
```

## Slide 8

```text
Mutation and crossover

•  Mutation: a way to generate desirable features by injecting
  random change; controlled by mutation rate





•  Crossover: combine parts of individuals to create new ones
      •   Single-point crossover: choose a crossover point, cut individuals
        there, swap the pieces





                                                                                  8
```

## Slide 9

```text
Encoding operators as binary masks





•  Implementation:
     • Use a crossover mask, which is a binary string
      At position i, take from first parent if maski is 1, otherwise take
      from other parent





                                                                                   9
```

## Slide 10

```text
Encoding operators as binary masks





                                                                                 10
```

## Slide 11

```text
Typical genetic algorithm





                                                                  i.e., crossover





                                                                     11
```

## Slide 12

```text
Selection: Survival of the fittest

•  As in natural evolution, fittest individuals are more likely to
   survive.
•  Several ways to implement this idea:
    1.  Fitness proportionate selection:
       Can lead to crowding (multiple copies being propagated).
    2. Tournament selection:
         Pick i, j at random with uniform probability. With prob p select the fitter
        one. Only requires comparing two individuals.
    3. Rank selection:
        Sort all individuals by fitness. Probability of selection is proportional to
         rank.
    4. Softmax (Boltzmann) selection:

•   Elitist variant: Copy the best individual(s) directly to the
  next generation

                                                                                     12
```

## Slide 13

```text
Example: Solving TSP with a GA

•  Each individual is a tour.
•  Mutation swaps a pair of edges (many other operations
   are possible and have been tried in literature.)
•  Crossover cuts the parents in two and swaps them.
   Reject any invalid offsprings.
•  Fitness is the length of the tour.
•  Note that GA operations (crossover and mutation)
   described here are fancier that the simple binary
  examples given before.





                                                                                   13
```

## Slide 14

```text
Example: Solving TSP with a GA





                                                                             14
```

## Slide 15

```text
The good and bad of GAs

•  Good:
      •   Intuitively appealing, due to evolution analogy.
      •    If tuned right, can be very effective (good solution with few
        steps).
•  Bad:
      •  Performance depends crucially on the problem encoding. Good
       encodings are difficult to find!
      •  Many parameters to tweak! Bad parameter settings can result in
       very slow progress, or the algorithm is stuck in local minima.
      •  With mutation rate is too low, can get overcrowding (many
       copies of the identical individuals in the population).





                                                                                   15
```

## Slide 16

```text
Today: Specifying search problems

• How do we actually formulate practical problems as
   search?
     •   I have 5 midterms in the space of two weeks. The one for COMP
      424 is before the one for COMP 551, but COMP 551 is pretty hard
       so I need to start studying in advance, because I cannot study
     more than 5 hours per course per week, or 8 hours in total across
         all the courses…

• Today’s key idea: specify problems declaratively as
  constraints
     • We list what we know, not how to solve a problem!





                                                                                    16
```

## Slide 17

```text
Searching with constraints

• Many other interesting problems have strict constraints:
     E.g. Must visit city A (to re-supply) before visiting city B (to sell).

• How can we incorporate this information in the search
   process?
     •  At a minimum, ensure the search will be limited to solutions that
       respect the constraints. Sometimes very few “legal solutions”.
     •  Even better, use the constraints to narrow the search space.





                                                                                    17
```

## Slide 18

```text
Example

•  Colour a map so that no adjacent territories have the
  same colour.





                                                                                    18
```

## Slide 19

```text
Constraint satisfaction problems (CSPs)

 • A CSP is defined by:
      •  Set of variables Vi, that can take values from domain Di
      •  Set of constraints specifying what combinations of values are
       allowed (for subsets of variables, e.g., pairs of variables)
      •  Constraints can be represented:
            •  Implicitly, as a function, testing for the satisfaction of the constraint.
               E.g. C1≠C2
            •  Explicitly, as a list of allowable values. E.g. (C1=R, C2=G), (C1=G, C2=R),
             (C1=B, C2=R), …
 • A CSP solution is an assignment of values to all variables
   that does not violate any constraintsl.
 • We typically want to find any solution or find that there is
   no solution.



                                                                                     19
```

## Slide 20

```text
Example





•  Variables WA, NT, Q, NSW, V, SA, T
•  Domains Di = {red, green, blue}

•  Constraints: adjacent regions must have different colors

•   E.g., WA ≠ NT




                                                                                    20
```

## Slide 21

```text
Example





•  Solutions are complete and consistent assignments.

•   E.g., WA = red, NT = green, Q = red, NSW = green, V = red, SA = blue,
       T = green



                                                                                    21
```

## Slide 22

```text
Sudoku

      •  Every row, column, 3x3 block must contain exact one
        instance of a number from 1 to 9.





                    Initial state                Solution

Image source: https://blogs.unimelb.edu.au/sciencecommunication/2016/10/23/i-promise-you-that-sudoku-could-win-you-a-million-dollars-but-youll-have-to-read-this-entire-blog-post-to-find-out-how/22
```

## Slide 23

```text
Types of variables

Many possibilities
•  Boolean variables (e.g., satisfiability)
•  Finite domain, discrete variables (e.g., colouring)
•  Infinite domain, discrete variables (e.g., integers)
•  Continuous variables (e.g., reals)

Problem complexity? Ranges from solvable in poly-time
   (e.g., linear programming) to NP-complete to undecidable.





                                                                                    23
```

## Slide 24

```text
Types of constraints

•  Unary: involve 1 variable
    •   e.g., WA ≠ green
•  Binary: involve 2 variables
    •   e.g., WA ≠ NT
•  Higher-order: involve ≥ 3 variables
    •   e.g., Between(X, Y, Z)
•  Relations:
     •  T1 + d1 ≤ T2 (Task2 has to come after Task1)    Scheduling
     •  Alldiff(variables in a row), Alldiff(variables in a column),
       Alldiff(variables in a 3x3 square)            Sudoku
•  Preferences (soft constraints): can be represented using
   costs and lead to constrained optimization problems.
    •   e.g., morning vs. afternoon preferences in exam scheduling



                                                                                    24
```

## Slide 25

```text
Real-world CSPs

Often involves allocating limited resources:
•  Timetable problems (e.g. which class is offered when, where)
•  Hardware configuration
•  Transportation scheduling, factory scheduling
•  Puzzle solving (crosswords, Sudoku)





                                                                                    25
```

## Slide 26

```text
Example: 4 queens problem

•  Put 4 queens on 4x4 board so that none attack each other:

      Partial assignment:




•  Formulate this as a CSP by defining:
     •  Variables and domains
     •  Constraints





                                                                                       26
```

## Slide 27

```text
4 Queens Problem

Put one queen per column. Let value indicate row of each
queen.
     •  Variables: {Q1, Q2, Q3, Q4}
     • Domain (same for all variables): {1, 2, 3, 4}
     •  Constraints:
         Qi ≠ Qj    (cannot be in same row)
         |Qi-Qj| ≠ |i - j| (cannot be in same diagonal)
•  Can also translate each constraint into set of allowable
   values for its variables:
     •  Values for (Q1, Q2): (Q1 =1,Q2 = 3),(Q1 =1,Q2 = 4),(Q1 =2,Q2 = 4) etc.





                                                                                    27
```

## Slide 28

```text
Example: Sudoku

•  Formulate sudoku as a CSP





                                                                                    28
```

## Slide 29

```text
Sudoku as a CSP

•  Variables?


•  Constraints?





                                                                                    29
```

## Slide 30

```text
Sudoku as a CSP

•  Variables
     •   Celli,j for row i from [1, 9], and col j from [1, 9]
     •  Domain: {1, …, 9} (same for all variables)
•  Constraints
     •  Cell1,1 = 5;  Cell1,2 = 3; etc. (filling in all known values)
     •  Alldiff(Cell1,j for all indices j); Alldiff(Cell2, j for all indices j); etc.
     •  Alldiff(Celli,1 for all indices i); Alldiff(Celli, 2 for all indices i); etc.
           • (To specify Alldiff):
             |uniqueset(Cell1,j for all indices j)}| = | Cell1,j for all indices j|
     •  For each 3x3 subtable with cells C:
           •  Alldiff(C)





                                                                                    30
```

## Slide 31

```text
Overview of approaches for solving CSPs

 •  Constructive approach
      •  State is defined by the set of values assigned so far
      •  Apply forward search to fill the solution
      •  General-purpose algorithm which works for all CSPs

 •  Local search approach
      •  Start with a broken but complete assignment of values to variables
      •  Gradually fix broken constraints by re-assigning variables
      • Use optimization approaches to decrease # broken constraints (hill-
          climbing, simulated annealing)





                                                                                      31
```

## Slide 32

```text
Constructive search for CSPs

•  Problem definition:
     •  State: defined by set of values assigned so far, could be partial
      and/or inconsistent assignment
     •  Initial state: all variables are unassigned.
     •  Operators: assign a value to an unassigned variable.
     •  Goal test: all variables assigned, no constraint violated.
          i.e., complete and consistent assignment

•  Problem has deterministic action, fully observable state.
    Important observation: Depth is limited to the number of variables, n.
    So we can apply DFS (or depth-limited search)





                                                                                    32
```

## Slide 33

```text
Example

•  Color abstract map so that adjacent countries don’t same
   color.
     •  Variables: Countries Ci
     •  Domains: {Red, Blue, Green}
     •  Constraints: {C1≠C2, C1≠C5, …}
                           C    C
                       C      1         2

                                            3

                               C

                                                             5
                        C                  C4

                                              6



                                                                                    33
```

## Slide 34

```text
Standard uninformed search for map
               coloring
                                                     choose 1 of n variables
                                                     choose 1 of d values for that variable





                                                    choose 1 of (n -1) variables
•  Is this complete? Optimal?              choose 1 of d values for that variable

•  Is this a practical approach? What is the complexity?





                                                                                    34
```

## Slide 35

```text
Standard uninformed search for map
               coloring
                                                     choose 1 of n variables
                                                     choose 1 of d values for that variable





                                                    choose 1 of (n -1) variables
•  Is this complete? Optimal?              choose 1 of d values for that variable
    Yes: known (not infinite) solution depth. Yes: If we check the constraints.
•  Is this a practical approach? What is the complexity?
   [n x d] x [(n-1) x d] x [(n-2) x d] x …… x [2 x d] x d = n! dn



                                                                                    35
```

## Slide 36

```text
Analysis of the simple approach

Branching factor is very high:
     ∑i d   (i sums over unassigned variables)

BUT: There can be only dn unique complete assignments.

More important observations:
•  Order in which variables are assigned is irrelevant -> Many
  paths are equivalent!
•  Adding assignments cannot correct a violated constraint!





                                                                                    36
```

## Slide 37

```text
Backtracking search

At each step, pick a remaining unassigned variable at each level
of search tree, then pick a value for that variable
    •   i.e., consider only assignments to a single variable at each node
    •  This way, b=|Di|
Algorithm:
     •  Select an unassigned variable, X.
     •  For each value={x1,…, xn} in the domain of that variable
           •  If the value satisfies the constraints, let X = xi and exit the loop.
     •   If an assignment was found, move to the next variable.
     •   If no assignment, go back to preceding variable and try different
       value.
•  This is the basic uninformed algorithm for CSPs.
     • Can solve n-queens for n ≈ 25.


                                                                                       37
```

## Slide 38

```text
Backtracking search





                                                               41
```

## Slide 39

```text
Backtracking search

At each step, pick a remaining unassigned variable at each level
of search tree, then pick a value for that variable
    •   i.e., consider only assignments to a single variable at each node
    •  This way, b=|Di|
Algorithm:
     •  Select an unassigned variable, X.
     •  For each value={x1,…, xn} in the domain of that variable
           •  If the value satisfies the constraints, let X = xi and exit the loop.
     •   If an assignment was found, move to the next variable.
     •   If no assignment, go back to preceding variable and try different
       value.

      Let’s focus on how we order the variables and the
     values for each variables


                                                                                       42
```

## Slide 40

```text
Selecting a variable

Heuristics:
     1. Minimum-remaining values: Choose the variable that is the
      most constrained (i.e., fewest legal values).
        ▪   e.g., after WA = red and NT = green, assign SA instead of Q





                                                                                    44
```

## Slide 41

```text
Selecting a variable

Heuristics:
     1. Minimum-remaining values: Choose the variable that is the
      most constrained (i.e., fewest legal values).


     2. Degree heuristic: Choose the variable that is involved in the
        largest number of constraints on other unassigned values
           • Use this to break ties from Minimum-remaining value heuristic
           •  e.g., choosing the first region to colour in Australia





                                                                                    45
```

## Slide 42

```text
Selecting a value

•  Heuristic:
     •  Least-constraining value: Assign the value that rules out the
      fewest values for other variables


•  Note that we want the variable that is the most
   constrained with the fewest remaining values (to quickly
   rule out many possible solutions), but the value that is
   least constraining, to offer flexibility to find some solution.





                                                                                    46
```

## Slide 43

```text
Selecting a value

•  Heuristic:
     •  Least-constraining value: Assign the value that rules out the
      fewest values for other variables
        ▪e.g., after WA = red and NT = green, prefer Q = red over Q = blue





                                                                                    47
```

## Slide 44

```text
How to solve CSPs?

General strategies:
•  Search
     •  Constructive methods (e.g., backtracking search)
     •  Local search
•  Inference
     •  Prune the domains of the variables by using the constraints that
      those variables are involved in





                                                                                    48
```

## Slide 45

```text
Recall example

•  Colour a map so that no adjacent territories have the
  same colour.





                                                                                    49
```

## Slide 46

```text
Data structure: Constraint graph
•  Nodes are variables, arcs show constraints
•  Graph structure can be exploited to accelerate solution
   search
E.g. Map colouring:


        C1     C2                   C1       C2
   C3
                                         C5

                                     C3                                             C6
              C5
                                                  C4     C6                 C4


                                                                                     50
```

## Slide 47

```text
Using constraint graph

•  Perform inference using constraint graph in order to
  reduce search space
•  Idea: Pre-process the graph before running a search
   algorithm to remove obvious inconsistencies

•  e.g., Two variables: A, B
      domain(A) = domain(B) = {1, 2, 3}
       Constraint: A < B
       Inference step: A cannot be 3 and B cannot be 1





                                                                                    51
```

## Slide 48

```text
Arc consistency

• A variable is arc consistent if every value in its domain
   satisfies that variable’s binary constraints (i.e., those with
  one other variable).
   o  i.e., Xi is arc-consistent w.r.t. Xj if for every value in Di, there is some
       value in Dj that satisfies the constraint on (Xi, Xj)
• A variable is generalized arc consistent if every value in its
  domain satisfies that variable’s n-ary constraints (with n-1
   other variables).

• A network is arc consistent if all of its variables are
   simultaneously arc consistent.





                                                                                    52
```

## Slide 49

```text
Example: Consistency constraints

A CSP with variables A, B, C, each with domain {1, 2, 3, 4}:

                    A<B      B<C
           A     B     C

After some pruning:
   A={1, 2, 3}; B={2, 3}; C={2, 3, 4}
  but network is still not arc consistent! (Check A < B again)

Arc consistent variable assignment:
   A={1, 2}; B={2, 3}; C={3, 4}





                                                                                    53
```

## Slide 50

```text
Possible outcomes after inference

What do the following outcomes after pruning mean?

1.  At least one variable’s domain is now the empty set.

2.  Every variable’s domain has exactly one remaining value
     left.

3.  Every variable’s domain has one or more remaining
   values left (and we’re not in case 2).





                                                                                    54
```

## Slide 51

```text
AC-3 Algorithm

•  Given a CSP (with binary constraints), perform inference
   to make the associated constraint graph arc consistent.


AC-3(CSP):
   worklist ←all arcs in the CSP’s constraint graph
   while worklist is not empty:
       (X, Y) ← worklist.pop()
       prune dom(X) wrt constraints involving Y
       if size(dom(X)) == 0: no solution
       if dom(X) was changed:
             for N in neighbours of X except Y:
                    worklist.push((N, X))
   done [start running search algorithm if necessary]




                                                                                    55
```

## Slide 52

```text
Example

A CSP with variables A, B, C, each with domain {1, 2, 3, 4}:

                    A<B      B<C
           A     B     C


Let’s run AC-3 on this problem.





                                                                                    56
```

## Slide 53

```text
Example details

A CSP with variables A, B, C, each with domain {1, 2, 3, 4}:

                    A<B      B<C
           A     B     C

Domains
A:          1     2     3     4
B:          1     2     3     4
C:          1     2     3     4

Worklist: { (A,B) (B,A) (B,C) (C,B)        }





                                                                                    57
```

## Slide 54

```text
Example result

A CSP with variables A, B, C, each with domain {1, 2, 3, 4}:

                    A<B      B<C
           A     B     C

Domains
A:          1     2     3     4
B:          1     2     3     4
C:          1     2     3     4

Worklist: { (A,B) (B,A) (B,C) (C,B) (A,B)}





                                                                                    58
```

## Slide 55

```text
Notes on AC-3

•   If there is an arc between (X, Y) in the CSP’s constraint
   graph, need to add both (X, Y) and (Y, X) to the worklist.
     •  Potentially need to reduce both dom(X) and dom(Y)
•  Time complexity: 𝑂(𝑒𝑑3)     •  𝑒is number of edges     •  𝑑is maximum size of domain across variables     •  Each edge can be added 𝑂(𝑑) times, because an edge is added     when a value is deleted, 𝑂(𝑒𝑑) in total     •  Each check for a binary constraint takes 𝑂(𝑑2)





                                                                                    59
```

## Slide 56

```text
Interleaving search and inference

•  For very large problems, may not want to do inference on
  the whole CSP all at once at the start.

• What if we interleaved search and inference?
     •  Take a step in search
     •  Then perform some local inference to prune some variables’
      domains
     •  Then continue search
     • …





                                                                                    60
```

## Slide 57

```text
Forward checking
Idea: Keep track of legal values for unassigned variables.
     • When you assign a variable X
           • look at each unassigned variable Y connected to X (by a constraint)
           •  delete from Y’s domain any value that is inconsistent with the value of X
     • Can solve n-queens for n ≈ 30.





                                                                                    61
```

## Slide 58

```text
Forward checking
 Idea: Keep track of legal values for unassigned variables.
       • When you assign a variable X
             • look at each unassigned variable Y connected to X (by a constraint)
             •  delete from Y’s domain any value that is inconsistent with the value of X

 E.g. Map colouring                             Nothing
                             assigned
                    C1   RGB
C1       C2                    C2   RGB
    C5              C3   RGB
                    C4   RGBC3         C6
                    C5   RGB
              C4      C6   RGB



                                                                                      62
```

## Slide 59

```text
Forward checking
 Idea: Keep track of legal values for unassigned variables.
       • When you assign a variable X, establish arc consistency for it
             • look at each unassigned variable Y connected to X (by a constraint)
             •  delete from Y’s domain any value that is inconsistent with the value of X

 E.g. Map colouring                             Nothing   Assign
                             assigned  C1 = Red
                    C1   RGB    R
C1       C2                    C2   RGB    GB
    C5              C3   RGB    GB
                    C4   RGB    RGBC3         C6
                    C5   RGB    GB
              C4      C6   RGB    RGB



                                                                                      63
```

## Slide 60

```text
Forward checking
 Idea: Keep track of legal values for unassigned variables.
       • When you assign a variable X, establish arc consistency for it
             • look at each unassigned variable Y connected to X (by a constraint)
             •  delete from Y’s domain any value that is inconsistent with the value of X

 E.g. Map colouring                             Nothing   Assign      Assign
                             assigned  C1 = Red    C2 = G
                    C1   RGB    R        R
C1       C2                    C2   RGB    GB       G
    C5              C3   RGB    GB       GB
                    C4   RGB    RGB      RGBC3         C6                                                              by forward                    C5   RGB    GB       B
                                                                      checking!
              C4      C6   RGB    RGB      RB



                                                                                      64
```

## Slide 61

```text
Forward checking
 Idea: Keep track of legal values for unassigned variables.
       • When you assign a variable X, establish arc consistency for it
             • look at each unassigned variable Y connected to X (by a constraint)
             •  delete from Y’s domain any value that is inconsistent with the value of X

 E.g. Map colouring                             Nothing   Assign      Assign
                             assigned  C1 = Red    C2 = G
                    C1   RGB    R        R
C1       C2                    C2   RGB    GB       G
    C5              C3   RGB    GB       GB
                    C4   RGB    RGB      RGBC3         C6                                                              by forward                    C5   RGB    GB       B
                                                                      checking!
              C4      C6   RGB    RGB      RB
   Can also apply AC-3 to get further pruning!


                                                                                      65
```

## Slide 62

```text
Forward checking
 Idea: Keep track of legal values for unassigned variables.
       • When you assign a variable X, establish arc consistency for it
             • look at each unassigned variable Y connected to X (by a constraint)
             •  delete from Y’s domain any value that is inconsistent with the value of X

 E.g. Map colouring                             Nothing   Assign      Assign
                             assigned  C1 = Red    C2 = G
                    C1   RGB    R        R
C1       C2                    C2   RGB    GB       G
    C5              C3   RGB    GB       GB  G
                    C4   RGB    RGB      RGBC3         C6
                    C5   RGB    GB       B
              C4      C6   RGB    RGB      RB   R
   Can also apply AC-3 to get further pruning!


                                                                                      66
```

## Slide 63

```text
Forward checking
 Idea: Keep track of legal values for unassigned variables.
       • When you assign a variable X, establish arc consistency for it
             • look at each unassigned variable Y connected to X (by a constraint)
             •  delete from Y’s domain any value that is inconsistent with the value of X

 E.g. Map colouring                             Nothing   Assign      Assign
                             assigned  C1 = Red    C2 = G
                    C1   RGB    R        R
C1       C2                    C2   RGB    GB       G
    C5              C3   RGB    GB       GB  G
                    C4   RGB    RGB      RGB  GBC3         C6
                    C5   RGB    GB       B
              C4      C6   RGB    RGB      RB   R
   Can also apply AC-3 to get further pruning!


                                                                                      67
```

## Slide 64

```text
Taking advantage of problem structure


•  Worst-case complexity is dn (where d is the number of
   possible values and n is the number of variables).
•  But a lot of problems are much easier!
•  Disjoint components can be solved independently
•  Trees can be solved inexpensively





                                                                                       68
```

## Slide 65

```text
Taking advantage of problem structure
•  Trees can be solved inexpensively
•  Creating trees: topological sort





•  Slightly different definition of consistency: directed arc
   consistency
     •  Under an ordering of variables X1, X2, …, Xn, DAC iff every Xi is arc-
       consistent with each Xj for j > 1
•  Tree-structured constraint graph: complexity is O(nd2)


                                                                                       69
```

## Slide 66

```text
Taking advantage of problem structure
•  Nearly-tree structured graph: complexity is O(dc(n-c)d2)
   using cutset conditioning:
     •  Find a set of variables which, when removed, turn graph into tree.
     •  Instantiate them all possible ways. Good if c (size of cutset) is
       small.





    Key insight: Leverage structure to accelerate solving!




                                                                                       70
```

## Slide 67

```text
How to solve CSPs?

General strategies:
•  Search
     •  Constructive methods (e.g., backtracking search)
     •  Local search
•  Inference
     •  Prune the domains of the variables by using the constraints that
      those variables are involved in





                                                                                    71
```

## Slide 68

```text
Local search for CSPs

General idea: Iterative improvement algorithm
•  Start with a broken but complete assignment of values to
   variables.
•  Allow variable assignments that don’t satisfy some
   constraints.
•  Randomly select any conflicted variables.
•  Operators reassign variable values.
     •  Min-conflicts heuristic chooses value that results in the fewest
     number of constraint violations.

a.k.a. Hill-climbing optimization! (Could also use simulated
annealing.)


                                                                                    72
```

## Slide 69

```text
Example: 4-Queens

•  States: 4 queens in 4 columns (44 = 256 states)
•  Operators: move queen in column
•  Goal test: no attacks
•  Evaluation function: number of attacks





                                                                                    73
```

## Slide 70

```text
Performance of min-conflicts heuristic

•  Given random initial state, can solve n-queens in almost
   constant time for arbitrary n with high probability (e.g. n=107).
•  The same appears to be true for many randomly-generated
   CSPs, except in a narrow range of the ratio:





                                                                                    74
```

## Slide 71

```text
Summary

•  CSPs are everywhere. Be able to recognize them!
• Know how to cast CSP solving as a search problems
•  Understand basic concepts: constraint graph, arc
   consistency
•  Understand both constructive and iterative improvement
  methods to solve CSPs
• Know how to apply the various heuristics:
    minimum-remaining-values, least-constraining value, degree
•  Iterative improvement methods using min-conflict
   heuristic are very general and often work better





                                                                                    75
```
