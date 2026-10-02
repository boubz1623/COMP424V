# L9 Search With Uncertainty

> Source: [original PDF](<../slides/L9 Search With Uncertainty.pdf>) · 47 slides. Text extraction may omit figures and alter equations; check the PDF.

## Slide 1

```text
COMP 424 - Artificial Intelligence
     Searching Under Uncertainty





           Lecture 9: September 30, 2026
      Jackie CK Cheung (jackie.cheung@mcgill.ca)
      Su Lin Blodgett (sulin.blodgett@mcgill.ca)
             Readings:   R&N 4.3, 4.4
```

## Slide 2

```text
Reminders


•  A1 is due tonight at 9pm
      •  24-hour grace period without penalty
      •  Please don’t treat tomorrow 9pm as the deadline! We could
        close the submission folder anytime after that.
      •  You can submit as many times as you’d like. We’ll only grade the
         last submission!
• No class on Monday, Oct 5 because of the provincial
   election.





                                                                                   2
```

## Slide 3

```text
The World Is Uncertain!

Major sources of uncertainty:
 • Outcomes of actions may be non-deterministic
       •  E.g., roll a die in a game

 •  Agent may not have full information about its state
     •  Observable – know the state
     •  Partially observable – some information
     •  Non-observable – don’t know at all!





COMP-424: Artificial intelligence                                                           3
```

## Slide 4

```text
Examples of partial observability

        Card games                         Blindfolded game?





                                   Robots with imperfect sensors       Word games





COMP-424: Artificial intelligence                                                           4
```

## Slide 5

```text
Examples of non-deterministic actions

                                          Attacking, etc., in an RPG
       Rolling dice





 Driving on uneven terrain
                            Anything you say or do as a human being...





COMP-424: Artificial intelligence                                                           5
```

## Slide 6

```text
Compare To Assumptions In First
              Lectures
 •  The environment was fully observable
     •  The agent always knew exactly what state it’s in

 •  The environment was deterministic
     •  The outcome of every action is known with certainty

 • Consequences:
     •  Didn’t need to model perceptions
     •  Solution to a problem is a single sequence of actions
     •  The solution can be predetermined via search

 • Module on game-playing broke these assumptions!
  So will today’s lecture, but in a different way.


COMP-424: Artificial intelligence                                                           6
```

## Slide 7

```text
Key Questions

 • How do we integrate uncertainty into our search process?
     • How do we represent the current progress in our search algorithm?
        Can’t assume we know what state we’re in.
     •  Future states cannot be determined in advance!

 • What does a solution to the search problem look like?
     •  No longer a path.
     •  Instead, a contingency plan (a.k.a., policy or strategy)

 • We’d still like to guarantee reaching a goal state, if possible!





COMP-424: Artificial intelligence                                                         7
```

## Slide 8

```text
Today’s Sample Problem





                                                                     8
```

## Slide 9

```text
Today’s Sample Problem

 Let’s consider the vacuum world:
 •  State:
                                                                          This is the full list
                                                                                    of the 8 possible     • Two rooms can each be clean or dirty
                                                                            underlying states
     • Vacuum’s location (in one room)
 • Actions:
     • Move (L/R)
     • Sweep (S)
 • Goal: to clean both rooms
 • Uncertainty sources:
     • Vacuum’s location (obs/not)
     •  Cleanliness status (obs/not)
     • Outcomes of actions are either
       certain or “noisy”
COMP-424: Artificial intelligence                                                           9
```

## Slide 10

```text
Observable vacuum world

1.  Observable, deterministic case:
     •  Start in a given initial state: {5}
     •  Plan: {Right; Sweep}





                                           Actions:
                                                            {Left, Right, Sweep}
                                            Transitions: As expected
                                      Goal states: {7, 8}


  COMP-424: Artificial intelligence                                                        10
```

## Slide 11

```text
Observable vacuum world: state space


Setting:
Observable•
Deterministic actions





COMP-424: Artificial intelligence                                                          11
```

## Slide 12

```text
Non-observable vacuum world

2.  Non-observable case:
     •  Start in any state: {1,2,3,4,5,6,7,8}
     •  Agent has no way to observe state
          •  No sensors, “blind” execution
     •  Plan: ?





                                           Actions:
                                                            {Left, Right, Sweep}
                                            Transitions: As expected
                                      Goal states: {7, 8}


  COMP-424: Artificial intelligence                                                        12
```

## Slide 13

```text
Non-observable vacuum world

2.  Non-observable case:
     •  Start state set: {1,2,3,4,5,6,7,8}
     •  Agent has no way to observe state
     •  Plan: {Right; ? }


 •  Taking an action (e.g., Right) moves the
    agent to a new set of states
 •  We must reason over sets now
 •  We call these sets “beliefs”
                                           Actions:
                                                            {Left, Right, Sweep}
                                            Transitions: As expected
                                      Goal states: {7, 8}


  COMP-424: Artificial intelligence                                                        13
```

## Slide 14

```text
Belief States

 • A belief state is the set of possible physical states an agent might
   be in.
     •   i.e., the agent’s current belief about the set of states that are
        possible, given the sequence of actions and observations

 •  What’s the total number of distinct belief states?
       •  Each of the 8 possible states may be included (or not) in the
        belief state
     • We can think of a belief state as an 8-bit vector: 28 = 256
          •  Technically 28-1, since the belief has to include at least 1 state





COMP-424: Artificial intelligence                                                        14
```

## Slide 15

```text
Searching with unobservable states

 •  What’s the total number of possible beliefs? 28-1
     •  The representational power of the belief formulation

 •  But what’s the number of reachable belief states?
     •  Note that there are many fewer underlying states and actions
       compared to the large number of beliefs.
     •  Need to consider the problem dynamics. Some states may be
        mutually exclusive and other sub-sets will be impossible to reach
       from the starting belief.





COMP-424: Artificial intelligence                                                        15
```

## Slide 16

```text
Non-observable vacuum:
        reachable belief space


                                                                              Setting:
                                                                    Non-observable
                                                                          Deterministic actions


                                                                                           Initial belief state
                                                                  =
                                                                               total ignorance

                                                                  =
                                                           8 physical states





                                                             NB: this figure
                                                                 omits self links!


COMP-424: Artificial intelligence                                                          16
```

## Slide 17

```text
Non-observable vacuum:
        reachable belief space


                                                                              Setting:
                                                                    Non-observable
                                                                          Deterministic actions


                                                                        Result of Right
                                                                  =
                                                      Vacuum is in the
                                                                                 right room
                                                                  =
                                                           4 physical states





                                                             NB: this figure
                                                                 omits self links!


COMP-424: Artificial intelligence                                                          17
```

## Slide 18

```text
Non-observable vacuum:
        reachable belief space


                                                                              Setting:
                                                                    Non-observable
                                                                          Deterministic actions


                                                                 Continue with a
                                                           Sweep
                                                                  =
                                                            We’re still in right
                                                              room, and it’s
                                                                           clean
                                                                  =
                                                           2 physical states




                                                             NB: this figure
                                                                 omits self links!


COMP-424: Artificial intelligence                                                          18
```

## Slide 19

```text
Non-observable vacuum:
        reachable belief space


                                                                              Setting:
                                                                    Non-observable
                                                                          Deterministic actions


                                                                                   Full path R,S,L,S
                                                                  =
                                                            We’re back to left
                                                            room. Both rooms
                                                                     are now clean
                                                                  =
                                                           1 physical state, a
                                                                          goal state




                                                             NB: this figure
                                                                 omits self links!


COMP-424: Artificial intelligence                                                          19
```

## Slide 20

```text
Searching with unobservable states

 •  Recall 28-1 belief states by counting the binary membership

 •  However, the number of reachable belief states is only 12
     •  Planning over this space can be reasonably efficient. Works on the
        belief-space graph shown previously.
     •  Note that these plans are “open-loop”. They do not adapt at all to
       which underlying state we’re in. That’s still unobserved.





COMP-424: Artificial intelligence                                                        20
```

## Slide 21

```text
Searching with unobservable states

• We have no observations, but actions are (so far)
   deterministic.
•  Start in any state:
    b = {1, 2, 3, 4, 5, 6, 7, 8}

• How to use actions?
    b = {1, 2, 3, 4, 5, 6, 7, 8} →Right {2, 4, 6, 8} = b’


    For deterministic actions: |b’| ≤ |b|

•  Plan?





  COMP-424: Artificial intelligence                                                        21
```

## Slide 22

```text
Searching with unobservable states

• We have no observations, but actions are (so far) deterministic.
•  Start in any state:
    b = {1, 2, 3, 4, 5, 6, 7, 8}

• How to use actions?
    b = {1, 2, 3, 4, 5, 6, 7, 8} →Right {2, 4, 6, 8} = b’


    For deterministic actions: |b’| ≤ |b|

•  Plan? Use a conformant plan
           {1, 2, 3, 4, 5, 6, 7, 8} →Right {2, 4, 6, 8} →Sweep{4, 8} →Left {3,7} →Sweep{7}

From a state of total uncertainty, we can coerce the world into state {7}



  COMP-424: Artificial intelligence                                                        22
```

## Slide 23

```text
Conformant planning

•  Goal: a plan that is guaranteed to take us from any initial state
   to a goal state, no matter what the effect of actions is

• A good search heuristic is to favor actions that reduce
   uncertainty
 → reduce the belief state to a single physical state
 → you might need to back up from bad belief states

• Once you know what physical state you’re in, apply standard
   search to reach the goal!

•  Use conformant planning when there are NO observations


                                                                                   23
```

## Slide 24

```text
Visual analogy

•  Feeding parts for manufacturing:
    http://goldberg.berkeley.edu/fences.mpg





                                                                                                                                                                                                                          fences.mpg





                                                                                   24
```

## Slide 25

```text
Faulty vacuum world

3.  Non-deterministic (but observable) case:
     •  Start in a given state: {1}
      •  Transitions are no longer as fully predictable:
          • Sweeping in a dirty square sometimes also cleans the adjacent square;
          Sweeping in a clean square sometimes deposits dirt
     •  Plan?





  COMP-424: Artificial intelligence                                                        25
```

## Slide 26

```text
Non-deterministic actions: AND-OR search


   •  In the case of non-deterministic actions, we also start by
     constructing a search tree
   • We augment trees to use two node types: AND and OR





             Sweep                             Right                       OR




          AND





COMP-424: Artificial intelligence                                                        26
```

## Slide 27

```text
Non-deterministic actions: AND-OR search


 AND-OR search tree:

  •  OR nodes: branching is induced by the agent’s choice between actions

  •  AND nodes: branching is induced by the environment’s choice of outcome



             Sweep                             Right                       OR




          AND





COMP-424: Artificial intelligence                                                        27
```

## Slide 28

```text
NB:
              Sweep       OR                                            AND nodes only branch
                                                 when the related action
                                                                                       is stochastic.

         AND


          Sweep   OR               OR     Sweep



         AND                           AND




                                       Sweep
                   OR


                                                            Setting:
                                                    Observable
                                                       Non-deterministic actions
                                                                 (faulty vacuum)



COMP-424: Artificial intelligence                                                          28
```

## Slide 29

```text
Non-deterministic vacuum: AND-OR search


 A solution for an AND-OR search problem is a subtree that

 satisfies the following conditions:

       1.  It specifies one action at each OR node

       2.  It includes every outcome at each AND node

      3.  It has a goal node at every leaf





COMP-424: Artificial intelligence                                                        29
```

## Slide 30

```text
Sweep       OR




         AND


          Sweep   OR               OR     Sweep



         AND                           AND




                                     Sweep
                   OR


                                                            Setting:
                                                    Observable
                                                       Non-deterministic actions
                                                                 (faulty vacuum)



COMP-424: Artificial intelligence                                                          30
```

## Slide 31

```text
In the AND-OR setting we
                                                   can find a solution with
              Sweep       OR
                                                           modified depth-first, or
                                                             breadth-first strategy.
                                                        Informed search strategies
                                                            also possible.         AND


          Sweep   OR               OR     Sweep



         AND                           AND




                                     Sweep
                   OR


                                                            Setting:
                                                    Observable
                                                       Non-deterministic actions
                                                                 (faulty vacuum)



COMP-424: Artificial intelligence                                                          31
```

## Slide 32

```text
Another case: The slippery vacuum

Movement actions, {Left, Right}, sometimes fail, leaving the
 agent in the same location.  E.g. {1} ->Right {1, 2}





COMP-424: Artificial intelligence                                                        32
```

## Slide 33

```text
Another case: The slippery vacuum

Movement actions, {Left, Right}, sometimes fail, leaving the
   agent in the same location. E.g., {1} ->Right {1, 2}



                       Sweep





 There are no longer any acyclic solutions starting from State 1.
 Thus, AND-OR search will return with failure. What now?

COMP-424: Artificial intelligence                                                        33
```

## Slide 34

```text
Keep on trying until it works

 Cyclic solution: keep on trying an action until it works.
 Is this a good solution?
   Depends on source of the stochasticity:
      • OK if caused by a random event
            •   e.g., Die roll
      •  Not OK if caused by an unobserved event
            •   e.g., broken vacuum
                                                             Sweep





                  Setting:
                Observable
                 Non-deterministic actions
                    (slippery vacuum)



COMP-424: Artificial intelligence                                                        34
```

## Slide 35

```text
Exercise: Tic-Tac-Toe

 • What would the AND-OR tree for tic-tac-toe look like?
   Draw it for a few levels.
 • What is a goal node?
 •  Suppose you are the starting player (X), and your
   opponent is (O).





COMP-424: Artificial intelligence                                                          35
```

## Slide 36

```text
Exercise: Tic-Tac-Toe





COMP-424: Artificial intelligence                                                          36
```

## Slide 37

```text
Exercise: Tic-Tac-Toe





COMP-424: Artificial intelligence                                                          37
```

## Slide 38

```text
Exercise: Tic-Tac-Toe





COMP-424: Artificial intelligence                                                          38
```

## Slide 39

```text
Exercise: Tic-Tac-Toe





COMP-424: Artificial intelligence                                                          39
```

## Slide 40

```text
Partial observability

•  Partially observable states lie between fully observable and
  unobservable states
•  E.g., perhaps the vacuum can only sense locally: it senses if
  the current room is dirty or clean but not the adjacent room

•  In this case, the agent must account for possible observations
•  Observations (percepts) are very useful: they tell the agent
  something partial about its new state
•  But they don’t tell it everything. It must again maintain a
   belief over possibilities





 COMP-424: Artificial intelligence                                                          40
```

## Slide 41

```text
Partial observability

•  The problem formulation must specify how the environment
   generates observations from the state (observation fcn)
•  Typically, several states can generate the same observation


• We can think of transitions from one belief state to the next
   for a given action as occurring in three stages:
     1. prediction: from the given action and the current belief, predict the
       next belief state (same as in unobservable case)
     2. observation prediction: predict which observations could be
       emitted in the predicted belief state
     3. update: for each possible observation, determine the resulting
        belief state; this is the set of states that could have produced the
       observation


COMP-424: Artificial intelligence                                                          41
```

## Slide 42

```text
Search with partial observations

 •  Deterministic case:
                                                 3.
                                      2.                              1.
                                                                         Setting:
                                                                               Partially observable
                                                                                 (local sensing)
                                                                     Deterministic actions



                                                                           3.
 •  Non-deterministic case:                           2.
                                                            1.


      Setting:
      Partially observable
        (local sensing)
     Non-deterministic actions
       (slippery vacuum)




COMP-424: Artificial intelligence                                                        42
```

## Slide 43

```text
Searching the belief space

 •  In general, we can apply any standard search algorithm
   for partially observable problems
 •  E.g., AND-OR search for the local-sensing vacuum:





                               Sweep





  •  AND-OR search returns a conditional plan that tests the
    belief state rather than the actual state



COMP-424: Artificial intelligence                                                        43
```

## Slide 44

```text
Searching the belief space

 •  In general, can apply any standard search algorithm for
    partially observable problems
 •  However, scalability is a major issue!

 •  Problem #1: Number of reachable beliefs can be very
   large
      •  Use sampling or pruning to reduce this

 •  Problem #2: Number of physical states in each belief
   state can be very large
      •  Use a compact state representation
      •  Plan for each state separately (not as a search over belief space)



COMP-424: Artificial intelligence                                                        44
```

## Slide 45

```text
Questions


•  What are the differences between the assumptions
  behind how we handle uncertainty during the last few
   lectures on game playing, vs. in this lecture?



• How do these differences propagate into the choice of
   representations, data structures, and algorithms?





                                                                                 45
```

## Slide 46

```text
Summary

 •  Actions can be {deterministic, nondeterministic}

 •  States can be {fully observable, unobservable, partially
   observable (deterministic), partially observable (non-
   deterministic)}

 •  Belief states represent the set of possible physical states
   an agent is in

 • AND-OR trees can be used to represent and search
   through a belief state space to produce a plan, even when
   there is uncertainty



COMP-424: Artificial intelligence                                                        46
```

## Slide 47

```text
Exercise: Mastermind

 http://www.web-games-online.com/mastermind/index.php
 •  Belief space?
 •  Initial belief?
 •  Action space?
 •  Deterministic / non-deterministic actions?
 •  Possible percepts?
 •  Perception function?
 •  Goal test?
 •  Step cost?





COMP-424: Artificial intelligence                                                          47
```
