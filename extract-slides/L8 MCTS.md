# L8 MCTS

> Source: [original PDF](<../slides/L8 MCTS.pdf>) · 65 slides. Text extraction may omit figures and alter equations; check the PDF.

## Slide 1

```text
Monte Carlo Tree Search





    Readings:   R&N Ch 5.4 (version 4 only)


       Lecture 8: September 28, 2026
Jackie CK Cheung (jackie.cheung@mcgill.ca)
 Su Lin Blodgett (sulin.blodgett@mcgill.ca)
```

## Slide 2

```text
Source: Wikimedia
                           Commons
•  Casino of Monte Carlo – what does this have to do
  with designing game-play bots?


                                                                               2
```

## Slide 3

```text
Issues with Minimax and Alpha-Beta

 •   It’s computationally impossible to search the full game, even
     if we do alpha-beta pruning!

 •  Therefore, all solutions to chess-sized games rely on having a
   reasonable evaluation function in practical cases

 •   It assumes both you and your opponent are playing optimally
   with respect to the same evaluation function





COMP-424: Artificial intelligence                                                         3
```

## Slide 4

```text
Questions About Minimax

 • What if there’s some nondeterminism in the game
   environment?

 • What if we don’t know the game well enough to design a
   good evaluation function?





COMP-424: Artificial intelligence                                                         4
```

## Slide 5

```text
Random Simulations

 Basic idea:
     •  The information from a full play-through can be helpful (if
        imprecise) feedback about the value of states.
     •  A single run wouldn’t be enough, but computers are good at
        repeating cheap operations many times…

 Solution: Random simulation
     •  Play the game from a state, many times, where the move
        selection is at least partly based on drawing random numbers.
     •  Combine the value at terminal outcomes to compute the starting
         state’s value.





COMP-424: Artificial intelligence                                                           5
```

## Slide 6

```text
Example

 •  3 possible next moves





COMP-424: Artificial intelligence                                                           6
```

## Slide 7

```text
Example

 •  3 possible next moves
 •  Simulate 10 games per move (random move choices)





COMP-424: Artificial intelligence                                                           7
```

## Slide 8

```text
Example

 •  3 possible next moves
 •  Simulate 10 games per move (random move choices)





        Blue – we win
      Red – opponent wins





COMP-424: Artificial intelligence                                                           8
```

## Slide 9

```text
Example

 •  3 possible next moves
 •  Simulate 10 games per move (random move choices)


                                                    This is an example of
                                            a Monte Carlo
                                            method – using
                                                  repeated random
                                                 sampling to estimate
        Blue – we win                            some numerical
      Red – opponent wins                                  quantity.

                                                  Think of the Census,
                                                         election polls, etc.


  → Pick the first move since it has the highest win rate

COMP-424: Artificial intelligence                                                           9
```

## Slide 10

```text
Where to spend the search effort?

•  Simulated lines of play do not have
   to be allocated equally to every
  move





 COMP-424: Artificial intelligence                                                          10
```

## Slide 11

```text
Where to spend the search effort?

•  Simulated lines of play do not have
   to be allocated equally to every
  move


•  Intuition: look more closely at the
  promising moves, since the others
  wouldn’t be picked (α-β logic)





 COMP-424: Artificial intelligence                                                          11
```

## Slide 12

```text
Monte Carlo Tree Search (MCTS)

  •  Combine search tree expansion with Monte Carlo
    simulations!
  • MCTS uses the concept of a policy
  • A policy is a mapping, π : S → A, for all states
                          π(s) = a
  •  π may select actions deterministically or stochastically


  •  We’ll distinguish two policies:
        •  Tree policy – high-quality, expensive, used near root
        •  Default policy – cheap, used near leaves; e.g., random move





COMP-424: Artificial intelligence                                                          12
```

## Slide 13

```text
Monte Carlo Tree Search (MCTS)


  1. Selection
        •  Use a tree policy on nodes seen before to select a promising
        path in the search tree (balance best play vs exploration – more
         to come on this later)
  2. Expansion
        •  Expand the tree when we reach the frontier (leaf nodes)
  3. Simulation
        •  From an expansion node, sample playouts (rollouts) using a
         default policy for both players (possibly completely random)
  4. Backpropagation (like back ups)
        •  After the rollout reaches a terminal node, update value and
            visit counts for states visited during selection and expansion



COMP-424: Artificial intelligence                                                          13
```

## Slide 14

```text
MCTS Steps





                                       adapted from Couetoux et al. (2013)





COMP-424: Artificial intelligence                                                          14
```

## Slide 15

```text
MCTS Steps





                                                                         Note: this is a
                                                         new node added
                                                                                   to the tree policy
                                                                           during this round!



                                       adapted from Couetoux et al. (2013)





COMP-424: Artificial intelligence                                                          15
```

## Slide 16

```text
MCTS step by step




Simulation 1



               Tree Policy





                                           new node in the tree

                                                node stored in tree

                                                             state visited but not stored

                                                         terminal state

                                                         current simulation

                                                         previous simulation



                                                                          16
```

## Slide 17

```text
MCTS step by step




Simulation 1



               Tree Policy





                                           new node in the tree

                                                node stored in tree

                                                             state visited but not stored

                                                         terminal state

                                                         current simulation

                                                        previous simulation



                                                                          17
```

## Slide 18

```text
MCTS step by step




Simulation 1



     0/0
               Tree Policy





                                           new node in the tree

                                                node stored in tree

                                                             state visited but not stored

                                                         terminal state

                                                         current simulation

                                                        previous simulation



                                                                          18
```

## Slide 19

```text
MCTS step by step




Simulation 1



     0/0
               Tree Policy


               Default Policy



                                           new node in the tree

                                                node stored in tree

                                                             state visited but not stored

                                                         terminal state

                                                         current simulation

                                                        previous simulation



                                                                          19
```

## Slide 20

```text
MCTS step by step




Simulation 1



     0/0
               Tree Policy


               Default Policy



                                           new node in the tree

                                                node stored in tree

                                                             state visited but not stored

                                                         terminal state

                                                         current simulation

                                                        previous simulation



                                                                          20
```

## Slide 21

```text
MCTS step by step




Simulation 1



     0/0
               Tree Policy


               Default Policy



                                           new node in the tree

                                                node stored in tree

                                                             state visited but not stored

                                                         terminal state

                                                         current simulation

                                                        previous simulation



                                                                          21
```

## Slide 22

```text
MCTS step by step




Simulation 1



     0/0
               Tree Policy


               Default Policy



                                           new node in the tree

                                                node stored in tree

                                                             state visited but not stored
    1
                                                         terminal state

                                                         current simulation

                                                        previous simulation



                                                                          23
```

## Slide 23

```text
MCTS step by step




Simulation 1



     1/1
               Tree Policy


               Default Policy



                                           new node in the tree

                                                node stored in tree

                                                             state visited but not stored
    1
                                                         terminal state

                                                         current simulation

                                                        previous simulation



                                                                          24
```

## Slide 24

```text
MCTS step by step




Simulation 2



     1/1




                    Tree Policy


                                           new node in the tree

                                                node stored in tree

                                                             state visited but not stored

                                                         terminal state

                                                         current simulation

                                                        previous simulation



                                                                          25
```

## Slide 25

```text
MCTS step by step




Simulation 2



     1/1



               0/0
                    Tree Policy


                                           new node in the tree

                                                node stored in tree

                                                             state visited but not stored

                                                         terminal state

                                                         current simulation

                                                        previous simulation



                                                                          26
```

## Slide 26

```text
MCTS step by step




Simulation 2



     1/1



               0/0
                    Tree Policy

                    Default Policy                                           new node in the tree

                                                node stored in tree

                                                             state visited but not stored

                                                         terminal state

                                                         current simulation           0

                                                        previous simulation



                                                                          28
```

## Slide 27

```text
MCTS step by step




Simulation 2



     1/2



               0/1
                    Tree Policy

                    Default Policy                                           new node in the tree

                                                node stored in tree

                                                             state visited but not stored

                                                         terminal state

                                                         current simulation           0

                                                        previous simulation



                                                                          29
```

## Slide 28

```text
MCTS step by step




    Simulation 3



          1/2



0/0                0/1
                        Tree Policy


                                             new node in the tree

                                                   node stored in tree

                                                                 state visited but not stored

                                                             terminal state

                                                             current simulation

                                                            previous simulation



                                                                             30
```

## Slide 29

```text
MCTS step by step




    Simulation 3



          1/2



0/0                0/1
                        Tree Policy

                        Default Policy                                             new node in the tree

                                                   node stored in tree

                                                                 state visited but not stored

                                                             terminal state

                                                             current simulation
 1
                                                            previous simulation



                                                                             31
```

## Slide 30

```text
MCTS step by step




    Simulation 3



          2/3



1/1                0/1
                        Tree Policy

                        Default Policy                                             new node in the tree

                                                   node stored in tree

                                                                 state visited but not stored

                                                             terminal state

                                                             current simulation
 1
                                                            previous simulation



                                                                             32
```

## Slide 31

```text
MCTS step by step




          Simulation 4



                 2/3



        1/1                0/1



0/0
                                                  new node in the tree                              Tree Policy

                                                        node stored in tree

                                                                       state visited but not stored

                                                                    terminal state

                                                                    current simulation

                                                                   previous simulation



                                                                                   33
```

## Slide 32

```text
MCTS step by step




          Simulation 4



                 2/3



        1/1                0/1



0/0
                                                  new node in the tree                              Tree Policy

                                                        node stored in tree
                              Default Policy
                                                                       state visited but not stored

                                                                    terminal state

                                                                    current simulation

                                                                   previous simulation

 0

                                                                                   34
```

## Slide 33

```text
MCTS step by step




          Simulation 4



                 2/4



        1/2                0/1



0/1
                                                  new node in the tree                              Tree Policy

                                                        node stored in tree
                              Default Policy
                                                                       state visited but not stored

                                                                    terminal state

                                                                    current simulation

                                                                   previous simulation

 0

                                                                                   35
```

## Slide 34

```text
MCTS step by step




          Simulation 5



                 2/4



        1/2                0/1



0/1            0/0
                                                  new node in the tree                              Tree Policy

                                                        node stored in tree

                                                                       state visited but not stored

                                                                    terminal state

                                                                    current simulation

                                                                   previous simulation



                                                                                   36
```

## Slide 35

```text
MCTS step by step




          Simulation 5



                 2/4



        1/2                0/1



0/1            0/0
                                                  new node in the tree                              Tree Policy

                                                        node stored in tree
                              Default Policy
                                                                       state visited but not stored

                                                                    terminal state

                                                                    current simulation

                                                                   previous simulation

            1

                                                                                   37
```

## Slide 36

```text
MCTS step by step




          Simulation 5



                 3/5



        2/3                0/1



0/1            1/1
                                                  new node in the tree                              Tree Policy

                                                        node stored in tree
                              Default Policy
                                                                       state visited but not stored

                                                                    terminal state

                                                                    current simulation

                                                                   previous simulation

            1

                                                                                   38
```

## Slide 37

```text
Example of Accumulating Statistics





COMP-424: Artificial intelligence                                                          39
```

## Slide 38

```text
MCTS Properties

 •  The purely MC evaluation function depends only on the
   observed outcomes of simulations
       •  No hand-crafted features, weights, or functions


 •  The evaluation function continues to improve from
    additional simulations
       •   In the limit of infinite memory and computation, it converges on the
        optimal search tree (i.e., minimax)


 •  The search develops in a selective, best-first manner; It
   expands promising regions of the search space much more
   deeply




COMP-424: Artificial intelligence                                                          40
```

## Slide 39

```text
Tree Policy

 • How should we select the next moves in the search tree?
 • We need to balance two opposing concerns:
       •  Exploitation: pick a node that looks promising according to
        current estimates based on previous simulations
       •  Exploration: pick a node that hasn’t participated in many
        simulations yet; we want more information on it





COMP-424: Artificial intelligence                                                          41
```

## Slide 40

```text
Tree Policy

 • How should we select the next moves in the search tree?
 • We need to balance two opposing concerns:
       •  Exploitation: pick a node that looks promising according to
        current estimates based on previous simulations
       •  Exploration: pick a node that hasn’t participated in many
        simulations yet; we want more information on it


 Let’s define the following:
 •  Q(s, a) ≡ the value of action a in state s, based on simulations so far
     •  Note that max will value positive utility, min will value negative
 •   n(s, a) ≡the number of times we have taken action a in state s
 •   n(s) ≡ the number of times we have visited s in simulations



COMP-424: Artificial intelligence                                                          42
```

## Slide 41

```text
Upper Confidence Trees (UCT)





        Q(s, a)   value of taking action a in state s
         n(s, a)   number of times we have taken action a in state s
         n(s)     number of times we have visited s in simulations
        c         scaling constant
COMP-424: Artificial intelligence                                                          43
```

## Slide 42

```text
Upper Confidence Trees (UCT)
                          Approximates the value of taking action a
                                 in state s, by how much we might still
                            gain by exploring more.





        Q(s, a)   value of taking action a in state s
         n(s, a)   number of times we have taken action a in state s
         n(s)     number of times we have visited s in simulations
        c         scaling constant
COMP-424: Artificial intelligence                                                          44
```

## Slide 43

```text
Upper Confidence Trees (UCT)

                                              Exploitation (= current estimate)





        Q(s, a)   value of taking action a in state s
         n(s, a)   number of times we have taken action a in state s
         n(s)     number of times we have visited s in simulations
        c         scaling constant
COMP-424: Artificial intelligence                                                          45
```

## Slide 44

```text
Upper Confidence Trees (UCT)

                                              Exploitation    Exploration (= uncertainty)





        Q(s, a)   value of taking action a in state s
         n(s, a)   number of times we have taken action a in state s
         n(s)     number of times we have visited s in simulations
        c         scaling constant
COMP-424: Artificial intelligence                                                          46
```

## Slide 45

```text
Upper Confidence Trees (UCT)

                                              Exploitation    Exploration (= uncertainty)





                                            •  This defines the upper bound of
                                                a confidence interval for the
                                                     value of a in s

                                            •   It gives a bonus to actions we
                                                     haven't tried much!


        Q(s, a)   value of taking action a in state s
         n(s, a)   number of times we have taken action a in state s
         n(s)     number of times we have visited s in simulations
        c         scaling constant
COMP-424: Artificial intelligence                                                          47
```

## Slide 46

```text
Exercise





        Q(s, a)   value of taking action a in state s
         n(s, a)   number of times we have taken action a in state s
         n(s)     number of times we have visited s in simulations
        c         scaling constant
COMP-424: Artificial intelligence                                                          48
```

## Slide 47

```text
Answer





                    → black picks action 1





COMP-424: Artificial intelligence                                                          49
```

## Slide 48

```text
MCTS questions




                          1. The computed values at each node are not the
                    sum of the children. Why? Is this an error?
                 3/5          Where are the extra values coming from?

       2/3                0/1    2. Why don’t we add every single node visited
                                       (i.e., visited by the default policy) during every
                             single simulation?
0/1            1/1

                          3.  Is the tree policy fixed over the entire process
                            or does it change? If so, how?





                                                                             50
```

## Slide 49

```text
MCTS in real games





                                                               51
```

## Slide 50

```text
Scrabble

 •  Stochastic game (letters drawn randomly)
 •  Imperfect information (can’t see opponent’s hand)
 •  Computers have an advantage because they can store and search the
    dictionary (move generation is easy)




 •  Quite complex!
      •  ~700 branching factor
      •  ~25 depth for a game
      • Rough complexity: 1070 search states
 •  Strategy is difficult! What letters to keep?




COMP-424: Artificial intelligence                                                          52
```

## Slide 51

```text
The Story of Go

 •  The Chinese game of Go is
   2000 years old
 •   It’s considered the hardest
    classic board game
 •   It was posed as a grand
   challenge task for AI
 •  Traditional approaches to
   game-tree search are
    insufficient for victory





COMP-424: Artificial intelligence                                                          53
```

## Slide 52

```text
The Game of Go

 • Game characteristics:
      •  ~10170 unique positions
      •  ~200 moves long
      •  ~200 branching factor
      •  ~10360 complexity





COMP-424: Artificial intelligence                                                          54
```

## Slide 53

```text
The Rules of Go

 •  Usually played on 19x19 board (also 13x13 or 9x9 board)
 •  Simple rules, complex strategy
 •  Black and white place stones alternately





COMP-424: Artificial intelligence                                                          55
```

## Slide 54

```text
Capturing

 •   If stones are completely surrounded, they are captured





COMP-424: Artificial intelligence                                                          56
```

## Slide 55

```text
Winner

 •  The game is finished when both players pass
 •  Intersections surrounded by each player are known as
    territory
 •  The player with more territory wins the game





COMP-424: Artificial intelligence                                                          57
```

## Slide 56

```text
Position Evaluation for AI

 • Game outcome, z
      •  Black wins:         z = 1
      •  White wins:        z = 0

 •  Value of state s, V(s)
      • 𝑉𝜋= 𝐸𝜋𝑧|𝑠       ← Monte-Carlo simulation
      • 𝑉∗= 𝑚𝑖𝑛𝑖𝑚𝑎𝑥𝑉𝜋(𝑠)  ← Tree search





COMP-424: Artificial intelligence                                                          58
```

## Slide 57

```text
Monte-Carlo Simulation





COMP-424: Artificial intelligence                                                          59
```

## Slide 58

```text
Rapid Action-Value Estimation (RAVE)

•  Can we share knowledge among
   related nodes?

•  Assumption: the value of a move
    is unaffected by moves played
   elsewhere on the board

                                            Estimate the value of
                                               playing action a
                                         immediately by the
                                           average outcome of
                                                              all simulations in
                                        which action a occurs!





  COMP-424: Artificial intelligence                                                          60
```

## Slide 59

```text
Rapid Action-Value Estimation (RAVE)

•  Can we share knowledge among
   related nodes?

•  Assumption: the value of a move
    is unaffected by moves played
   elsewhere on the board

                                            Estimate the value of•  RAVE heuristic provides more
                                               playing action a
   information: a move can appear
                                         immediately by the
   several times over a handful of                                           average outcome of
   simulations                                                              all simulations in
                                        which action a occurs!
•  RAVE shares knowledge across
   nodes and gives a rapid, biased
   value estimate




  COMP-424: Artificial intelligence                                                          61
```

## Slide 60

```text
State Representation Matters!

 •  Original assumption: each move at each position in the
   board has its quality estimated separately
      •  This doesn’t make use of commonalities between board positions
      •  As a result, we need many simulations for each position

 • RAVE assumption: only the move itself matters
      •  Simplifies state space, requiring fewer simulations to get good
       estimates
      •  Might oversimplify, leading to inaccurate estimates

 •  This trade-off between model complexity and
   representational power is pervasive in statistical
   estimation!

COMP-424: Artificial intelligence                                                          62
```

## Slide 61

```text
MC-RAVE in MoGo (2007)





COMP-424: Artificial intelligence                                                          63
```

## Slide 62

```text
MoGo (2007)

 • MoGo = heuristic MCTS + MC-RAVE + handcrafted default
   policy

 • 99% winning rate against best traditional programs

 •  Gold medal at Computer Go Olympiad

 •  First victory against professional players (on a 9x9 board)





COMP-424: Artificial intelligence                                                          64
```

## Slide 63

```text
AlphaGo (2016)

 •  Based on advances in
       state representation, value estimation,
       policy learning using deep neural networks





 •  Victory (4-1) over Lee Sedol on the full 19x19 board


COMP-424: Artificial intelligence                                                          65
```

## Slide 64

```text
Monte-Carlo tree search (vs α-β)

Advantages
     •  Not as pessimistic
     •  Converges to the Minimax solution in the limit
     •   It’s an anytime algorithm: its performance improves with number of
        lines of play
     •  Less affected by the branching factor:
           • we get to the end of the game simulating one branch only
           • we can control the number of lines of play to match the available time
           •  if branching factor is huge, search can go much deeper, which is a big gain
     •  Easy to parallelize
Disadvantages
     • May miss optimal play (because it won’t see all moves at deeper nodes)
     •  Policy used to generate candidate plays is very important.
     •  E.g., can use an opponent model, or just simple randomization


COMP-424: Artificial intelligence                                                          66
```

## Slide 65

```text
Recap Questions

 •  L6 discussed minimax search for two-player, perfect
   information games
      • What is a two player zero-sum game?
      • What assumptions does it make about how your opponent will
       behave?
 • L7 talked about ways to prune the search tree
      • Why does alpha-beta pruning always give the minimax answer?
      • What is an evaluation function, and its role in these algorithms?
 •  L8 used random simulations for learning to play games
     •  Know the difference between tree and default policies
     •  Think about what inputs are needed from the programmer
     •  When do you expect MCTS to do well? Poorly?
     •   If we have code for another strong solution, can we use it within
      MCTS?
COMP-424: Artificial intelligence                                                          67
```
