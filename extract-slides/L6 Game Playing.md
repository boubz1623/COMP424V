# L6 Game Playing

> Source: [original PDF](<../slides/L6 Game Playing.pdf>) · 46 slides. Text extraction may omit figures and alter equations; check the PDF.

## Slide 1

```text
COMP 424 - Artificial Intelligence
         Game Playing





           Lecture 6: September 21, 2026


      Jackie CK Cheung (jackie.cheung@mcgill.ca)
      Su Lin Blodgett (sulin.blodgett@mcgill.ca)
              Readings:   R&N Ch 5
```

## Slide 2

```text
Announcements

•  A1 is released on MyCourses!
     •  Due on Sep 30, 2026 at 9pm.





                                                                                   2
```

## Slide 3

```text
Review: Graph Colouring as a CSP

 •  Nodes are variables, arcs show constraints
 •  Graph structure can be exploited to accelerate solution
   search
E.g. Map colouring:


        C1     C2                   C1       C2
   C3
                                         C5

                                     C3                                              C6
              C5
                                                  C4     C6                 C4



                                                                                     3
```

## Slide 4

```text
Review: Forward checking

  Idea: Keep track of legal values for unassigned variables.
        •  When you assign a variable X
               •   look at each unassigned variable Y connected to X (by a constraint)
               •   delete from Y’s domain any value that is inconsistent the value of
             X

                             Nothing
  E.g. Map coloring.         assigned
                   C1   RGB
C1       C2                   C2   RGB
    C5              C3   RGB
                   C4   RGB
C3         C6
                   C5   RGB
              C4      C6   RGB



                                                                                      4
```

## Slide 5

```text
Forward checking

  Idea: Keep track of legal values for unassigned variables.
        •  When you assign a variable X
               •   look at each unassigned variable Y connected to X (by a constraint)
               •   delete from Y’s domain any value that is inconsistent the value of
             X

                             Nothing   Assign
  E.g. Map coloring.         assigned  C1 = Red
                   C1   RGB    R
C1       C2                   C2   RGB    GB
    C5              C3   RGB    GB
                   C4   RGB    RGB
C3         C6
                   C5   RGB    GB
              C4      C6   RGB    RGB



                                                                                      5
```

## Slide 6

```text
Forward checking

  Idea: Keep track of legal values for unassigned variables.
        •  When you assign a variable X
               •   look at each unassigned variable Y connected to X (by a constraint)
               •   delete from Y’s domain any value that is inconsistent the value of
             X

                             Nothing   Assign      Assign
  E.g. Map coloring.         assigned  C1 = Red    C2 = G
                   C1   RGB    R        R
C1       C2                   C2   RGB    GB       G
    C5              C3   RGB    GB       GB
                   C4   RGB    RGB      RGB
C3         C6                                                              by forward                   C5   RGB    GB       B
                                                                      checking!
              C4      C6   RGB    RGB      RB



                                                                                      6
```

## Slide 7

```text
Quick recap

 Standard assumptions:
 •  Discrete (vs continuous) state space

 •  Deterministic (vs stochastic) environment

 •  Observable (vs unobservable) environment

 •  Static (vs changing) environment

 •  There is only a single AI agent





COMP-424: Artificial intelligence                                                         7
```

## Slide 8

```text
Quick recap

 Standard assumptions:
 •  Discrete (vs continuous) state space

 •  Deterministic (vs stochastic) environment

 •  Observable (vs unobservable) environment

 •  Static (vs changing) environment

 •  There is only a single AI agent

       • Maybe we could simply model games as “uncertainty” in the
       environment? Chess opponents may be unpredictable.
       •  Doesn’t account for the fact that the other player has its own goal.
       While somewhat unknown, we can compute over their decisions too!





COMP-424: Artificial intelligence                                                         8
```

## Slide 9

```text
Today’s lecture

 •  Adversarial search → games with 2 players
     •  Planning ahead in a world where other agents are planning
        against us
 •  Minimax search
 •  Evaluation functions
 •  Alpha-beta pruning
 •  State-of-the-art game playing programs





COMP-424: Artificial intelligence                                                           9
```

## Slide 10

```text
Game playing

 • One of the oldest, best studied domains in AI! Why?
      •  They’re fun! People enjoy games and are good at playing them
      • Many games are hard:
            •  State spaces can be huge and complicated
                  • Chess has branching factor of 35 and games go to 50 moves per
                 player → 35100 nodes in the search tree!
            • Games may be stochastic and partially observable
            • Real-time constraints (e.g., fixed amount of time between moves)
            • Games require the ability to make some decision even when
             calculating the optimal decision is infeasible
      •  Clear, clean description of the environment and actions
      •  Easy performance indicator: winning is everything



COMP-424: Artificial intelligence                                                          10
```

## Slide 11

```text
Types of games

 •  Perfect information vs. Imperfect information
      •  Perfect: players observe the exact state of the game
      •  Imperfect: information is hidden from players
       •  Fully observable vs. partially observable

 •  Deterministic vs. Stochastic
      •  Deterministic: state changes are fully determined by player moves
      •  Stochastic: state changes are partially determined by chance





COMP-424: Artificial intelligence                                                          11
```

## Slide 12

```text
What type of game?


                             Perfect information?

                    Yes               No

                 Checkers
                                        Mastermind                   Othello
 Deterministic                                     Solitaire*               Chess
             Go

                                          Scrabble
               Backgammon           Monopoly   Stochastic
                                        Poker
                                       Most card games





COMP-424: Artificial intelligence                                                          12
```

## Slide 13

```text
Game playing as search

 •  Consider 2-player, turn-taking, perfect information,
   deterministic games
 •  Can we formulate them as a search problem?





COMP-424: Artificial intelligence                                                          13
```

## Slide 14

```text
Game playing as search

 •  Consider 2-player, turn-taking, perfect information,
   deterministic games
 •  Can we formulate them as a search problem? Yes!





COMP-424: Artificial intelligence                                                          14
```

## Slide 15

```text
Game playing as search

 •  Consider 2-player, turn-taking, perfect information,
   deterministic games
 •  Can we formulate them as a search problem? Yes!
     State, s:             the state of the board + which player moves
     Operators, o:        Legal moves in a given state
     Transition fcn:       Defines the result of a move
     Terminal states:      States in which the game is over
                         (won/lost/drawn)
      Utility fcn:           Defines a numeric value for the game for
                          player p, when the game ends in terminal
                           state s.
                        Simple case: +1 for win, -1 for loss, 0 for draw.
                    More complex cases: points won, money, …


COMP-424: Artificial intelligence                                                          15
```

## Slide 16

```text
Game playing as search

 •  Consider 2-player, turn-taking, perfect information,
   deterministic games

 •  Can we formulate them as a search problem? Yes!

 • We want to find a strategy (a way of picking moves) that
   maximizes utility
     •   i.e., maximize the probability of winning or the expected points,
       minimize the cost, ...





COMP-424: Artificial intelligence                                                          16
```

## Slide 17

```text
Game search challenge

 •   It’s not quite the same as simple searching

 •  There’s an opponent! That opponent is adversarial!





COMP-424: Artificial intelligence                                                          17
```

## Slide 18

```text
Game search challenge

 •   It’s not quite the same as simple searching

 •  There’s an opponent! That opponent is adversarial!





      •  The opponent has its own goals which don’t match our goals
      •  Opponent tries to make things good for itself and bad for us
      • We must simulate the opponent’s decisions


COMP-424: Artificial intelligence                                                          18
```

## Slide 19

```text
Zero-Sum Games


 • A special case is where one player’s gain equally balances
   the other player’s loss: the zero-sum game


 •  In order to reason about this, introduce utility, a function
   over outcomes of the game, in Player 1’s point-of-view.
      •  Let high utility mean player 1 is happy (so player 2 is sad)
      •  Let low utility mean player 2 is happy (so player 1 is sad)





COMP-424: Artificial intelligence                                                          19
```

## Slide 20

```text
Zero-Sum Games


  •  Zero-sum games
        •  Each player's gain or loss of utility is exactly balanced by the
          losses or gains of the utility of the other player


        •    If I win, you lose: U(p1) = 1 → U(p2) = -1
                        U(p1) + U(p2) = 0


        •  Important problem within Game Theory, where we can use
       some famous concepts when reasoning about our solutions:
              •  Minimax Theorem of von Neuman 1928
              •  Nash Equilibria 1951





COMP-424: Artificial intelligence                                                          20
```

## Slide 21

```text
Game search challenge

 •   It’s not quite the same as simple searching

 •  There’s an opponent! That opponent is adversarial!
      •   It has its own goal which does not match our goal
      • We must simulate the opponent’s decisions

 •  Key idea: Define
      •  a max player (who wants to maximize the utility)
      •  a min player (who wants to minimize it)





COMP-424: Artificial intelligence                                                          21
```

## Slide 22

```text
Example: Game Tree for Tic-Tac-Toe





                                                                                 Ply:
                                                       Term for the move of one
                                                                          player. A full move is two ply.

                                                                 Search Tree:
                                                   A tree superimposed on the
                                                                                           full game tree that examines
                                                          enough nodes for the player to
                                                              determine what move to
                                                            make.



COMP-424: Artificial intelligence                                                          22
```

## Slide 23

```text
Minimax search

An algorithm for finding the optimal strategy: the best move
 to play at each state (node)

How it works:
 •  Expand the complete search tree until terminal states
   have been reached

 •  Compute utilities of the terminal states

 •  Back up from the leaves towards the current game state:
      •  At each min node: back up the worst value among its children
      •  At each max node: back up the best value among its children




COMP-424: Artificial intelligence                                                          23
```

## Slide 24

```text
Minimax search

 •  Expand the search tree to the terminal states
 • Compute utilities at terminal states
 •  Back up from the leaves towards the current game state
      •  At each min node: back up the worst value among the children
      •  At each max node: back up the best value among the children





COMP-424: Artificial intelligence                                                          24
```

## Slide 25

```text
Minimax search





COMP-424: Artificial intelligence                                                          25
```

## Slide 26

```text
Minimax search





COMP-424: Artificial intelligence                                                          26
```

## Slide 27

```text
Minimax search





COMP-424: Artificial intelligence                                                          27
```

## Slide 28

```text
Minimax search





COMP-424: Artificial intelligence                                                          28
```

## Slide 29

```text
Minimax search





COMP-424: Artificial intelligence                                                          29
```

## Slide 30

```text
Minimax search





     The minimax value at each node tells us how to play an optimal game!

COMP-424: Artificial intelligence                                                          30
```

## Slide 31

```text
Minimax Algorithm

operator MinimaxDecision()
   for each legal operator o:
            apply the operator o and obtain the new
      game state s.
            Value[o] = MinimaxValue(s)
   return the operator o with the highest value
   Value[o].

double MinimaxValue(s)
   if isTerminal(s), return Utility(s).
   for each state s’ in Successors(s)
      let Value(s’) = MinimaxValue(s’).
   if Max’s turn to move in s, return maxs’Value(s’).
   if Min’s turn to move in s, return mins’Value(s’).


 COMP-424: Artificial intelligence                                                          31
```

## Slide 32

```text
Exercise

 •  Apply minimax search to the following game search tree





  4     3   2     1      3     7   8     9




COMP-424: Artificial intelligence                                                          32
```

## Slide 33

```text
Exercise

      •  Apply minimax search to the following game search tree

Max                                  ?


               ?                                     ?Min


Max     ?                  ?           ?                                                            ?




     4     3   2     1      3     7   8     9




      COMP-424: Artificial intelligence                                                          33
```

## Slide 34

```text
Properties of Minimax search

 •  Complete?

 •  Optimal?

 •  Time complexity?

 •  Space complexity?





COMP-424: Artificial intelligence                                                          34
```

## Slide 35

```text
Properties of Minimax search

 •  Complete?  If the game tree is finite

 •  Optimal? Against an optimal opponent, yes
       •   It maximizes the worst-case outcome for Max
       •  There might exist better strategies for suboptimal opponents

 •  Time complexity?  O(bm)

 •  Space complexity? O(bm) if we use DFS





COMP-424: Artificial intelligence                                                          35
```

## Slide 36

```text
Properties of Minimax search

 •  Complete?  If the game tree is finite

 •  Optimal? Against an optimal opponent, yes
       •   It maximizes the worst-case outcome for Max
       •  There might exist better strategies for suboptimal opponents

 •  Time complexity?  O(bm)

 •  Space complexity? O(bm) if we use DFS

 •  So is Minimax suitable for solving chess?



COMP-424: Artificial intelligence                                                          36
```

## Slide 37

```text
Properties of Minimax search

 •  Complete?  If the game tree is finite

 •  Optimal? Against an optimal opponent, yes
       •   It maximizes the worst-case outcome for Max
       •  There could be superior strategies for suboptimal opponents

 •  Time complexity?  O(bm)

 •  Space complexity? O(bm) if we use DFS

 •  So is Minimax suitable for solving chess?
      •  In chess: b≈35, m≈100, so an exact solution is impossible!


COMP-424: Artificial intelligence                                                          37
```

## Slide 38

```text
Coping with resource limitations

 •  Suppose we have 100 seconds to make a move, and we
   can search 104 nodes per second
      •  Then we can only search 106 nodes
       (Or even fewer, if we spend time deciding which nodes to search)

 •  Possible approach:
      •  Use a cutoff test (e.g., based on a depth limit)
      •  Use an evaluation function for the nodes where we cut the
       search (since they’re not terminal states, we don’t know the true
          utility)

 • Need to think about real-time search




COMP-424: Artificial intelligence                                                          38
```

## Slide 39

```text
Evaluation functions

 • An evaluation function v(s) estimates the expected utility
   of a state (e.g., the likelihood of winning from that state)
       •  Performance depends strongly on the quality of v(s)
       •   If it is too inaccurate it will lead the agent astray
 •  Desiderata:
       •   It should order the terminal states according to their true utility
       •   It should be relatively quick to compute
       •  For nonterminal states, it should be strongly correlated with the
        actual chances of winning
 • An evaluation function can be designed by an expert or
   learned from experience





COMP-424: Artificial intelligence                                                          39
```

## Slide 40

```text
Evaluation functions

• Most evaluation functions work by calculating features of the
   state (e.g., # of pawns, queens, etc.)
•  Features define categories or equivalence classes of states
•  Typically, we compute features separately and then combine
  them for an aggregate value
•  E.g., if the features of the board are independent, use a
  weighted linear function:
                        v(s) = w1 f1(s) + w2 f2(s) + … + wn fn(s)

•  Independence is a strong, likely incorrect assumption. But it
   could still be useful!
      • An extra bishop is worth more in the endgame; its weight should depend
      on the “move number” feature

  COMP-424: Artificial intelligence                                                          40
```

## Slide 41

```text
Example: Chess





         Black to move                 White to move
        White slightly better            Black winning

 •  Linear evaluation function: v(s) =       +                            w1 f1(s)  w2 f2(s)
      f1(s) = (# white queens) - (# black queens)
      f2(s) = (# white pawns) - (# black pawns)



COMP-424: Artificial intelligence                                                          41
```

## Slide 42

```text
Example: Chess





         Black to move                 White to move
        White slightly better            Black winning

 •  Linear evaluation function: v(s) =       +                            w1 f1(s)  w2 f2(s)
      f1(s) = (# white queens) - (# black queens)            w1 = 9
      f2(s) = (# white pawns) - (# black pawns)              w2 = 3



COMP-424: Artificial intelligence                                                          42
```

## Slide 43

```text
How precise should the evaluation fcn be?

 •  For deterministic games, all that matters is that the fcn
   preserve the ordering of the nodes
 •  Thus, the move chosen is invariant under monotonic
   transformations of the evaluation function





 •  In deterministic games, payoff acts as an ordinal utility
   function




COMP-424: Artificial intelligence                                                          43
```

## Slide 44

```text
Minimax with an evaluation function

 •  Use the evaluation function to evaluate non-terminal
   nodes
      •  This helps make a decision without searching until the end of the
      game

 • Minimax cutoff algorithm:
  Same as standard Minimax, except stop at some
  maximum depth m, use the evaluation function on those
   nodes, back up from there





COMP-424: Artificial intelligence                                                          44
```

## Slide 45

```text
Minimax cutoff in chess

 • How many moves ahead can we search in chess?
        If our hardware could search 106 nodes in the available time, then
    minimax cutoff with b=35 could search 4 moves ahead

 •  Is that good?
      4 moves ahead ≈ novice player
      8 moves ahead ≈ human master, typical PC
      12 moves ahead ≈ Deep Blue, Kasparov

 •  Key idea:
     Instead of exhaustive search, let’s search a few lines of play, but
       deeply
   We need pruning!


COMP-424: Artificial intelligence                                                          45
```

## Slide 46

```text
Conclusion


•  Minimax search is a powerful algorithm, and all you need
   for small games.
      •  Captures adversarial, two-player, zero-sum nature
      •  Does all the “thinking” for both you and an optimal opponent
      •  Important note: Not the best way to exploit your friends’ weak
       play (WHY?)


•  Minimax still does not scale to large problems. We will
  see better methods coming up!





                                                                                 46
```
