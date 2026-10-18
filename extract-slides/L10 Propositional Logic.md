# L10 Propositional Logic

> Source: [original PDF](<../slides/L10 Propositional Logic.pdf>) · 79 slides. Text extraction may omit figures and alter equations; check the PDF.

## Slide 1

```text
COMP 424 - Artificial Intelligence
             Fall 2026


           Lecture 10: October 7th, 2026
                 Propositional Logic

     Su Lin Blodgett (sulin.blodgett@mcgill.ca)
     Jackie CK Cheung (jackie.cheung@mcgill.ca)
```

## Slide 2

```text
Announcements

•  Midterm help sessions coming soon – check Ed for
   details!

•  Midterm crib sheet, review doc





                                                                                  2
```

## Slide 3

```text
The Goal Today





                                                          3
```

## Slide 4

```text
The Goal Today

 •  Can you play battleship with
       •  Constructive or Local Searches?
       •  MiniMax Search?
       •  MCTS?

       •  AND-OR Search?

We'd like a more expressive kind of knowledge:
• How to represent it
• How to reason about it → infer what to do next





                                                                                  6
```

## Slide 5

```text
A knowledge-based agent

Two key components:
     •  The knowledge base, which contains a set of facts expressed in
     some formal, standard language
     •  The inference engine, which uses general rules to deduce new
        facts from those in the KB





                                                                                   7
```

## Slide 6

```text
A knowledge-based agent

Two key components:
     •  The knowledge base, which contains a set of facts expressed in
     some formal, standard language
     •  The inference engine, which uses general rules to deduce new
        facts from those in the KB


         Knowledge base             Domain-specific content

          Inference engine            Domain-independent algorithms





                                                                                   8
```

## Slide 7

```text
A knowledge-based agent



                                             Domain-specific content        Knowledge base

         Inference engine            Domain-independent algorithms


•  KB may be initialized with background knowledge
• When the agent perceives an observation, it adds the
   related fact to its KB
•   It queries the KB for what action to take in a given state
•   It adds the fact that it took the action to the KB
•  All the while, the inference engine may be expanding the
   set of facts in the KB



                                                                                  9
```

## Slide 8

```text
An example: Wumpus World

Percepts: Breeze, Glitter, Stench
    (local perception only)

Actions: Turn-left, Turn-right, Forward, Grab, Shoot

Goal: Get the Gold and return to Start;
     Don’t enter a Pit or alive Wumpus square

Rules of the environment:
•   Squares adjacent to Wumpus are smelly (Stench)
•   Squares adjacent to Pit are breezy (Breeze)
•   Glitter if and only if Gold is in the same square
                                                          Agent•   Shooting kills the Wumpus if you are facing it
•   Shooting uses up the only Arrow
•  Grabbing picks up the Gold if in the same square


                                                                                        10
```

## Slide 9

```text
An example: Wumpus World

Percepts: Breeze, Glitter, Stench
    (local perception only)

Actions: Turn-left, Turn-right, Forward, Grab, Shoot

Goal: Get the Gold and return to Start;
     Don’t enter a Pit or alive Wumpus square

Rules of the environment:
•   Squares adjacent to Wumpus are smelly (Stench)
•   Squares adjacent to Pit are breezy (Breeze)
•   Glitter if and only if Gold is in the same square
•   Shooting kills the Wumpus if you are facing it
•   Shooting uses up the only Arrow
•  Grabbing picks up the Gold if in the same square


                                                                                        11
```

## Slide 10

```text
Wumpus World Characteristics

•  The world is static: positions of the pits, gold, and
  monster do not change during the game

•  The actions have deterministic effects

•  The state is partially observable
     •  The agent doesn’t know the map beforehand and can only
       perceive what’s in the square it occupies
     • → It must infer the map from local perception

•  What’s the belief state for this domain?





                                                                                    12
```

## Slide 11

```text
Wumpus World Characteristics

•  The world is static: positions of the pits, gold, and
  monster do not change during the game

•  The actions have deterministic effects

•  The state is partially observable
     •  The agent doesn’t know the map beforehand and can only
       perceive what’s in the square it occupies
     • → It must infer the map from local perception

•  What’s the belief state for this domain?
      •  All possible configurations of the board (that haven’t been ruled
      out by observations) → HUGE


                                                                                    13
```

## Slide 12

```text
Exploring a Wumpus World





                                           A= Agent
                                           B= Breeze
                                           S= Smell
                                           P= Pit
                                    W= Wumpus
                                      OK = Safe
                                   G = Glitter





                                                                        14
```

## Slide 13

```text
Exploring a Wumpus World





                                           A= Agent
                                           B= Breeze
                                           S= Smell
                                           P= Pit
                                    W= Wumpus
                                      OK = Safe
                                   G = Glitter





                                                                        15
```

## Slide 14

```text
Exploring a Wumpus World





                                           A= Agent
                                           B= Breeze
                                           S= Smell
                                           P= Pit
                                    W= Wumpus
                                      OK = Safe
                                   G = Glitter





                                                                        16
```

## Slide 15

```text
Exploring a Wumpus World





                                           A= Agent
                                           B= Breeze
                                           S= Smell
                                           P= Pit
                                    W= Wumpus
                                      OK = Safe
                                   G = Glitter





                                                                        17
```

## Slide 16

```text
Exploring a Wumpus World





                                           A= Agent
                                           B= Breeze
                                           S= Smell
                                           P= Pit
                                    W= Wumpus
                                      OK = Safe
                                   G = Glitter





                                                                        18
```

## Slide 17

```text
Exploring a Wumpus World





                                           A= Agent
                                           B= Breeze
                                           S= Smell
                                           P= Pit
                                    W= Wumpus
                                      OK = Safe
                                   G = Glitter





                                                                        19
```

## Slide 18

```text
Exploring a Wumpus World





                                           A= Agent
                                           B= Breeze
                                           S= Smell
                                           P= Pit
                                    W= Wumpus
                                      OK = Safe
                                   G = Glitter





                                                                        20
```

## Slide 19

```text
Using actions to gain knowledge

•  Suppose we enter another Wumpus cave•  Perceive Smell in (1, 1) ⇒cannot move
•  Use a strategy of coercion:
     •  Shoot straight ahead     • Wumpus was there ⇒dead ⇒safe
                                 S     • Wumpus wasn’t there ⇒safe
                                   A


Logic is a type of knowledge representation that supports
   this reasoning!





                                                                                    21
```

## Slide 20

```text
Logic

•  Logics are formal languages for representing information
•  They enable conclusions to be drawn from what is known
• A logic is defined by the following:
     •  The syntax defines which sentences are allowed in the language
     •  The semantics define the “meaning” of sentences,
          i.e., the truth of a sentence in a given world





                                                                                    22
```

## Slide 21

```text
Logic

•  Logics are formal languages for representing information
•  They enable conclusions to be drawn from what is known
• A logic is defined by the following:
     •  The syntax defines which sentences are allowed in the language
     •  The semantics define the “meaning” of sentences,
          i.e., the truth of a sentence in a given world

  An analogy: The language of arithmetic
      x+2 ≥ y is a sentence
      x2 + y > is not a sentence
      x+2 ≥ y is true iff the number x+2 is no less than the number y
      x+2 ≥ y is true in a world where x=7, y=1
      x+2 ≥ y is false in a world where x=0, y=6



                                                                                    23
```

## Slide 22

```text
Types of logic

•  Logics are characterized by what they allow as “primitives”
      •  Ontological commitment: what exists? (facts/objects/time/beliefs)
      •  Epistemological commitment: what do we know? (states of knowledge)

   Language        Ontological commitment     Epistemological commitment

Propositional logic                  facts                     true/false/unknown

 First-order logic          facts, objects, relations             true/false/unknown

  Temporal logic       facts, objects, relations, times          true/false/unknown

Probability theory                  facts                    degree of belief [0, 1]

    Fuzzy logic             degree of truth               degree of belief [0, 1]





                                                                                       24
```

## Slide 23

```text
Propositional logic

•  Propositions are the basic elements
    •  They are assertions about the state of the world/game/problem
    •  They can be true or false
     •  e.g. “Today is Thursday”, “Today is Wednesday”

•  Syntax specifies the valid sentences in the logic
     •  Atomic sentences consist of a single proposition symbol, like the
      sentence P1 or W1,3
     • Complex sentences are constructed from simpler sentences
     • We combine sentences using parentheses and logical connectives





                                                                                    25
```

## Slide 24

```text
Propositional logic: Syntax

  There are five standard logical connectives:
negation: ¬     conjunction: ∧    disjunction: ∨    implication: ⇒   biconditional: ⇔
    not           and               or              implies                     iff


  Syntax defines the allowable sentences:
        •  Atomic sentences are sentences
        •   If S is a sentence,           ¬S is a sentence        •   If S1 and S2 are sentences,   S1 ∧S2 is a sentence        •   If S1 and S2 are sentences,   S1 ∨S2 is a sentence        •   If S1 and S2 are sentences,   S1 ⇒S2 is a sentence        •   If S1 and S2 are sentences,  S1 ⇔S2 is a sentence


                                                                                       26
```

## Slide 25

```text
Propositional logic: Syntax

Some examples

W(3,1)   W(3,2)   P(2,2)   B(2,1)
W(3,1) ⋀W(3,2)P(2, 2) ⇒B(2, 1)
(W(3,1) ⋀W(3,2)) ∨(P(2,2) ⇒B(2,1))





                                                                                    27
```

## Slide 26

```text
Propositional logic: Semantics

•  The semantics defines the rules for determining the truth of
  a sentence

•  Truth is always determined with respect to a model
• A model is an assignment of truth values, one for every
   proposition symbol. e.g.,
         m = {P1 = true, P2 = false, P3 = true}

 •  A sentence may be true in one model and false in another





                                                                                    28
```

## Slide 27

```text
Propositional logic: Semantics

•  The semantics defines the rules for determining the truth of
  a sentence, with respect to a particular model

•  Rules for evaluating truth with respect to model m:

    ¬S        is true iff    S is false                               in m
                   is true iff     S1 is true    and     S2 is true       in m   S1 ∧S2
                   is true iff     S1 is true     or      S2 is true       in m   S1 ∨S2
                   is true iff     S1 is false     or      S2 is true       in m   S1 ⇒S2
                                      m                   is true iff  S1⇒S2 is true  and  S2⇒S1 is true    in   S1 ⇔S2
S1 ⇒S2 can also be written as ¬S1 ∨S2S1 ⇔S2 can also be written as (¬S1 ∨S2) ∧(S1 ∨¬S2)

                                                                                    30
```

## Slide 28

```text
Interpretations: True or False

Some terminology:
• A sentence is valid if it is true in all models
• A sentence is satisfiable if it is true in at least one model
• A sentence is unsatisfiable if it is false in all models

•  The truth of a sentence may depend on the model

                e.g., Sentence = “Today is Wednesday.”
                        Is this valid? Is it satisfiable?





                                                                                    31
```

## Slide 29

```text
Exercise

•  For each of the following logical statements, say whether
    it is valid, satisfiable or unsatisfiable:
   A ∨¬B
    (A ∧B) ∨(¬A ∨¬B)
   ¬A ⇒A
   B ∧(B ⇒¬B)





                                                                                    32
```

## Slide 30

```text
Exercise

•  For each of the following logical statements, say whether
    it is valid, satisfiable or unsatisfiable:
                                                                     True ∨¬True   A ∨¬B                                                                     True ∨¬False                                                                              False ∨¬True    (A ∧B) ∨(¬A ∨¬B)                                                False ∨¬False
   ¬A ⇒A
   B ∧(B ⇒¬B)





                                                                                    33
```

## Slide 31

```text
Exercise

•  For each of the following logical statements, say whether
    it is valid, satisfiable or unsatisfiable:
                                                                     True ∨¬True   A ∨¬B                                    satisfiable                                                                     True ∨¬False                                                                              False ∨¬True    (A ∧B) ∨(¬A ∨¬B)                                                False ∨¬False
   ¬A ⇒A
   B ∧(B ⇒¬B)





                                                                                    34
```

## Slide 32

```text
Exercise

•  For each of the following logical statements, say whether
    it is valid, satisfiable or unsatisfiable:
   A ∨¬B                                    satisfiable                                                               (True ∧True) ∨(¬True ∨¬True)                                                               (True ∧False) ∨(¬True ∨¬False)    (A ∧B) ∨(¬A ∨¬B)                                                                      (False ∧True) ∨(¬False ∨¬True)                                                                     (False ∧False) ∨(¬False ∨¬False)   ¬A ⇒A
   B ∧(B ⇒¬B)





                                                                                    35
```

## Slide 33

```text
Exercise

•  For each of the following logical statements, say whether
    it is valid, satisfiable or unsatisfiable:
   A ∨¬B                                    satisfiable                                                               (True ∧True) ∨(¬True ∨¬True)                                                               (True ∧False) ∨(¬True ∨¬False)    (A ∧B) ∨(¬A ∨¬B)                     valid                                                                      (False ∧True) ∨(¬False ∨¬True)                                                                     (False ∧False) ∨(¬False ∨¬False)   ¬A ⇒A
   B ∧(B ⇒¬B)





                                                                                    36
```

## Slide 34

```text
Exercise

•  For each of the following logical statements, say whether
    it is valid, satisfiable or unsatisfiable:
   A ∨¬B                                    satisfiable
    (A ∧B) ∨(¬A ∨¬B)                     valid
                                                               ¬True ⇒True   ¬A ⇒A                                                                     ¬False ⇒False
   B ∧(B ⇒¬B)





                                                                                    37
```

## Slide 35

```text
Exercise

•  For each of the following logical statements, say whether
    it is valid, satisfiable or unsatisfiable:
   A ∨¬B                                    satisfiable
    (A ∧B) ∨(¬A ∨¬B)                     valid
                                                               ¬True ⇒True   ¬A ⇒A                                   satisfiable                                                                     ¬False ⇒False
   B ∧(B ⇒¬B)





                                                                                    38
```

## Slide 36

```text
Exercise

•  For each of the following logical statements, say whether
    it is valid, satisfiable or unsatisfiable:
   A ∨¬B                                    satisfiable
    (A ∧B) ∨(¬A ∨¬B)                     valid
   ¬A ⇒A                                   satisfiable
                                                                   True ∧(True ⇒¬True)   B ∧(B ⇒¬B)                                                                           False ∧(False ⇒¬False)





                                                                                    39
```

## Slide 37

```text
Exercise

•  For each of the following logical statements, say whether
    it is valid, satisfiable or unsatisfiable:
   A ∨¬B                                    satisfiable
    (A ∧B) ∨(¬A ∨¬B)                     valid
   ¬A ⇒A                                   satisfiable
                                                                   True ∧(True ⇒¬True)   B ∧(B ⇒¬B)                           unsatisfiable                                                                           False ∧(False ⇒¬False)





                                                                                    40
```

## Slide 38

```text
Using logic

 • We want to derive sound conclusions from what we
   already know

 •  Thus, we want a process for generating new sentences
    that are guaranteed to be true
       •   (in any world in which the premises are true)
•  The first step is the concept of entailment: α ⊨β
      • We say α entails β
      •  Or, β follows logically from α





                                                                                    41
```

## Slide 39

```text
Entailment

•  Sentence α entails sentence β if and only if β is true in all
  worlds where α is true:           α ⊨β  if and only if M(α) ⊆M(β)

                                                  The set of all models in which α is true.
                                                    “The set of all models that satisfy α.”
 •  α is a stronger assertion than β, since α rules out more
    possible worlds

 •  Another arithmetic illustration:
          sentence x = 0 entails sentence xy = 0





                                                                                    43
```

## Slide 40

```text
Entailment in Wumpus World

Let’s consider this situation:
•  The agent detects Nothing in [1,1], moves right, and detects
  Breeze in [2,1]

•  The agent wants to infer the presence of pits in squares
   [1,2], [2,2], and [3,1]

•  There are 3 Boolean (true-false) choices:
      •   P[1,2] = true           P[1,2] = false
      •   P[2,2] = true           P[2,2] = false
      •   P[3,1] = true           P[3,1] = false    ⇒8 possible models


                                                                                    44
```

## Slide 41

```text
Models in Wumpus World





                                                                      45
```

## Slide 42

```text
KB in Wumpus World

• KB = wumpus-world rules + observations





                KB





                                                                                    46
```

## Slide 43

```text
Model checking in Wumpus World

• KB = wumpus-world rules + observations

•  Consider β1 = “square [1,2] is safe”

•  Is it the case that KB     ?                ⊨β1

•  Let’s use model checking => Enumerate models and check





                                                                                        47
```

## Slide 44

```text
Model checking in Wumpus World

• KB = wumpus-world rules + observations
•  Consider β1 = “square [1,2] is safe”


                                       By model checking,
          KB                          KB                                   ⊨β1





                                    β1
                                                                      Recall:
                                                 KB entails β
                                                                                                 if and only if
                                                      β is true in all worlds
                                                     where KB is true.


                                                                                        48
```

## Slide 45

```text
Model checking in Wumpus World

• KB = wumpus-world rules + observations

•  Consider β2 = “square [2,2] is safe”

•  Is it the case that KB     ?                ⊨β2





                                                                                        49
```

## Slide 46

```text
Model checking in Wumpus World

• KB = wumpus-world rules + observations
•  Consider β2 = “square [2,2] is safe”


                                       By model checking,                                                          β2
          KB                          KB                                   ⊭β2





                                                                      Recall:
                                                 KB entails β
                                                                                                 if and only if
                                                      β is true in all worlds
                                                     where KB is true.


                                                                                        50
```

## Slide 47

```text
The Knowledge-based Agent

•  Recall our agent, with its knowledge base and inference
  procedure

• Now we have an idea for what the KB actually is:
    •  a set of sentences in propositional logic!

• We can also see the utility of entailment    If KB ⊨β then:
      •  in every model in which KB is true, β is also true
      • we can derive the conclusion β from what we already know (the KB)

                        The process of logical inference!


                                                                                    53
```

## Slide 48

```text
Inference procedure

• KB   β      ⊢i
   means sentence β can be derived from KB by inference procedure i

•  Desired qualities of inference procedure i:
                                      β is true, it is also true that    Soundness:  i is sound if, whenever KB ⊢i     KB ⊨β.
       In other words, we only infer entailed sentences.
    Completeness:  i is complete if, whenever KB ⊨β is true, it is also true
                    β.       that KB ⊢i
       In other words, we can generate all the entailed sentences.





                                                                                      54
```

## Slide 49

```text
Two inference methods

1. Model checking:
     •  Truth table enumeration

2. Application of inference rules





                                                                                    55
```

## Slide 50

```text
Propositional inference
Truth table method:    Let β = A ∨B and KB = (A ∨C) ∧(B ∨¬C)     Is it the case that KB ⊨β ?

    Check all possible models: β must be true whenever KB is true.  A     B     C    A ∨C  B ∨¬C  KB   β = A ∨B
  False     False     False
  False     False     True
  False     True     False
  False     True     True
  True     False     False
  True     False     True
  True     True     False
  True     True     True


                                                                                    56
```

## Slide 51

```text
Propositional inference
Truth table method:    Let β = A ∨B and KB = (A ∨C) ∧(B ∨¬C)     Is it the case that KB ⊨β ?

    Check all possible models: β must be true whenever KB is true.  A     B     C    A ∨C  B ∨¬C  KB   β = A ∨B
  False     False     False   False     True      False   False
  False     False     True   True      False     False   False
  False     True     False   False     True      False   True
  False     True     True   True     True     True    True
  True     False     False   True     True     True    True
  True     False     True   True      False     False   True
  True     True     False   True     True     True    True
  True     True     True   True     True     True    True


                                                                                    57
```

## Slide 52

```text
Propositional inference
Truth table method:    Let β = A ∨B and KB = (A ∨C) ∧(B ∨¬C)     Is it the case that KB ⊨β ?           YES!

    Check all possible models: β must be true whenever KB is true.  A     B     C    A ∨C  B ∨¬C  KB   β = A ∨B
  False     False     False   False     True      False   False
  False     False     True   True      False     False   False
  False     True     False   False     True      False   True
  False     True     True   True     True     True    True
  True     False     False   True     True     True    True
  True     False     True   True      False     False   True
  True     True     False   True     True     True    True
  True     True     True   True     True     True    True


                                                                                    58
```

## Slide 53

```text
Properties of the truth table method

•  Is it sound?        Yes.

•  Is it complete?     Yes. It checks truth in all possible models.

•  Time / space complexity?
      •  Highly inefficient! 2n models for n literals!

• A literal is an atomic sentence (positive literal) or a negated
  atomic sentence (negative literal)





                                                                                    60
```

## Slide 54

```text
Two kinds of inference methods

1. Model checking:
     •  Truth table enumeration (sound and complete, but expensive)

1.  Application of inference rules (theorem proving):
     • A proof is a sequence of inference rule applications that
      generates the desired sentence
     • We can use inference rules as operators in a standard search
       algorithm to automate theorem proving





                                                                                    61
```

## Slide 55

```text
Inference rules for propositional logic

•  Resolution:                     (α ∨β),  (¬β ∨γ)                          (α ∨γ)

• Modus Ponens:         …      ∧…    ⇒β)             α1, α2,    αn, (α1 ∧α2    ∧αn
                        β

•  Contraposition:                     α ⇒β                    ¬β ⇒¬α



                                                                                    64
```

## Slide 56

```text
Other useful rules

•  And-elimination:              ∧…                     α1 ∧α2    ∧αn
                          α1, α2, … , αn

•  Implication elimination:                     α ⇒β                  ¬α ∨β

• De Morgan’s law:       ¬(α ∨β)                         ¬(α ∧β)      (¬α) ∧(¬β)                        (¬α) ∨(¬β)



                                                                                    65
```

## Slide 57

```text
Searching with inference rules

•  Inference rules can be used with forward search or
  backward search

•  This brings the algorithms we’ve seen previously, like
   iterative deepening, into play for theorem proving

•  Thus, logic enables us to automate reasoning





                                                                                    66
```

## Slide 58

```text
Forward chaining

• When a new sentence p is added to the KB
      •  Look for all sentences that share literals with p
      •  Perform inference
      •  Add new sentences to the KB and continue until p is added or
       more inferences can be made

• Two important properties:
     •  Forward chaining is data-driven:
          It infers properties and categories for new percepts
     •  Forward chaining is an eager method: new facts are inferred as
      soon as possible





                                                                                    68
```

## Slide 59

```text
Backward chaining

• When a query q is asked of the KB
     •   If q is in the KB already, return true
     •  Else, use inference for q with other sentences in the KB to find
       implications in the KB whose conclusion is q
       ▪If all the premises of one of those implications is true, then q is true

• Two important properties:
     •  Backward chaining is goal-driven:
          It centers the reasoning around the query being asked
     •   It is a lazy reasoning method: new facts are only inferred as
      needed, and only to the extent that they help answer the
       question





                                                                                    70
```

## Slide 60

```text
Forward chaining example

Let’s say we have a knowledge base with these sentences:•  HaveAILecture ⇒(TodayIsMonday ∨TodayIsWednesday)
•  ¬TodayIsMonday•  HaveAILecture ∨HaveNoClass•  HaveNoClass ⇒Sad
•  ¬Sad

Can you infer what day it is?





                                                                                    71
```

## Slide 61

```text
Forward chaining example
¬Sad       HaveNoClass ⇒Sad





                                                                                   72
```

## Slide 62

```text
Forward chaining example
¬Sad       HaveNoClass ⇒Sad

                                  Contraposition + Modus Ponens

      ¬HaveNoClass





                                                                                   73
```

## Slide 63

```text
Forward chaining example
¬Sad       HaveNoClass ⇒Sad
      ¬HaveNoClass       HaveAILecture ∨HaveNoClass





                                                                                   74
```

## Slide 64

```text
Forward chaining example
¬Sad       HaveNoClass ⇒Sad
      ¬HaveNoClass       HaveAILecture ∨HaveNoClass

               Resolution

                   HaveAILecture





                                                                                   75
```

## Slide 65

```text
Forward chaining example
¬Sad       HaveNoClass ⇒Sad
      ¬HaveNoClass       HaveAILecture ∨HaveNoClass
                                         HaveAILecture ⇒                   HaveAILecture        (TodayIsMonday ∨
                                      TodayIsWednesday)





                                                                                   76
```

## Slide 66

```text
Forward chaining example
¬Sad       HaveNoClass ⇒Sad
      ¬HaveNoClass       HaveAILecture ∨HaveNoClass
                                         HaveAILecture ⇒                   HaveAILecture        (TodayIsMonday ∨
                                      TodayIsWednesday)

                     Modus Ponens
                     TodayIsMonday ∨TodayIsWednesday





                                                                                   77
```

## Slide 67

```text
Forward chaining example
  ¬Sad       HaveNoClass ⇒Sad
        ¬HaveNoClass       HaveAILecture ∨HaveNoClass
                                           HaveAILecture ⇒                     HaveAILecture        (TodayIsMonday ∨
                                         TodayIsWednesday)
¬TodayIsMonday          TodayIsMonday ∨TodayIsWednesday





                                                                                       78
```

## Slide 68

```text
Forward chaining example
  ¬Sad       HaveNoClass ⇒Sad
        ¬HaveNoClass       HaveAILecture ∨HaveNoClass
                                           HaveAILecture ⇒                     HaveAILecture        (TodayIsMonday ∨
                                         TodayIsWednesday)
¬TodayIsMonday          TodayIsMonday ∨TodayIsWednesday

         Resolution
            TodayIsWednesday!


                                                                                       79
```

## Slide 69

```text
Summary

• A knowledge-based agent
      •  Knowledge base
      •  Inference engine
• Wumpus World

•  Propositional Logic
      •  Sentences and Models
      •  Entailment

•  Inference methods
      •  Model checking
      •  Theorem proving
           •   Inference rules
           •  Forward chaining and backward chaining



                                                                                   80
```

## Slide 70

```text
The Goal Today





                                                           81
```

## Slide 71

```text
The Goal Today





3, 1          3, 2          3, 3
   ?        ?        ?


2, 1          2, 2          2, 3
   ?        ?        ?


1, 1          1, 2          1, 3
   ?        ?        ?





                                                                                 82
```

## Slide 72

```text
The Goal Today
                                   B1,1 ⇒(B1,2 ∨B2,1)                                   B1,2 ⇒(B1,1 ∨B1,3 ∨B2,2)                                   B1,3 ⇒(B1,2 ∨B2,3)
3, 1          3, 2          3, 3                                   B2,1 ⇒(B1,1 ∨B2,2 ∨B3,1)   ?        ?        ?                B2,2 ⇒(B1,2 ∨B2,1 ∨B2,3 ∨B3,2)                                   B2,3 ⇒(B1,3 ∨B2,2 ∨B3,3)2, 1          2, 2          2, 3   ?        ?        ?                B3,1 ⇒(B3,2 ∨B2,1)                                   B3,2 ⇒(B3,1 ∨B3,3 ∨B2,2)
1, 1          1, 2          1, 3                                   B3,3 ⇒(B3,2 ∨B2,3)
   ?        ?        ?





                                                                                 83
```

## Slide 73

```text
The Goal Today
                                   B1,1 ⇒(B1,2 ∨B2,1)                                   B1,2 ⇒(B1,1 ∨B1,3 ∨B2,2)                                   B1,3 ⇒(B1,2 ∨B2,3)
3, 1          3, 2          3, 3                                   B2,1 ⇒(B1,1 ∨B2,2 ∨B3,1)   ?        ?        ?                B2,2 ⇒(B1,2 ∨B2,1 ∨B2,3 ∨B3,2)                                   B2,3 ⇒(B1,3 ∨B2,2 ∨B3,3)2, 1          2, 2          2, 3   ?        ?        ?                B3,1 ⇒(B3,2 ∨B2,1)                                   B3,2 ⇒(B3,1 ∨B3,3 ∨B2,2)
1, 1          1, 2          1, 3                                   B3,3 ⇒(B3,2 ∨B2,3)
  Hit        ?        ?
                                   B1,1





                                                                                 84
```

## Slide 74

```text
The Goal Today
                                   B1,1 ⇒(B1,2 ∨B2,1)                                   B1,2 ⇒(B1,1 ∨B1,3 ∨B2,2)                                   B1,3 ⇒(B1,2 ∨B2,3)
3, 1          3, 2          3, 3                                   B2,1 ⇒(B1,1 ∨B2,2 ∨B3,1)   ?        ?        ?                B2,2 ⇒(B1,2 ∨B2,1 ∨B2,3 ∨B3,2)                                   B2,3 ⇒(B1,3 ∨B2,2 ∨B3,3)2, 1          2, 2          2, 3   ?        ?        ?                B3,1 ⇒(B3,2 ∨B2,1)                                   B3,2 ⇒(B3,1 ∨B3,3 ∨B2,2)
1, 1          1, 2          1, 3                                   B3,3 ⇒(B3,2 ∨B2,3)
  Hit        ?        ?
                                   B1,1                                   B1,2 ∨B2,1





                                                                                 85
```

## Slide 75

```text
The Goal Today
                                   B1,1 ⇒(B1,2 ∨B2,1)                                   B1,2 ⇒(B1,1 ∨B1,3 ∨B2,2)                                   B1,3 ⇒(B1,2 ∨B2,3)
3, 1          3, 2          3, 3                                   B2,1 ⇒(B1,1 ∨B2,2 ∨B3,1)   ?        ?        ?                B2,2 ⇒(B1,2 ∨B2,1 ∨B2,3 ∨B3,2)                                   B2,3 ⇒(B1,3 ∨B2,2 ∨B3,3)2, 1          2, 2          2, 3Empty      ?        ?                B3,1 ⇒(B3,2 ∨B2,1)                                   B3,2 ⇒(B3,1 ∨B3,3 ∨B2,2)
1, 1          1, 2          1, 3                                   B3,3 ⇒(B3,2 ∨B2,3)
  Hit        ?        ?
                                   B1,1                                   B1,2 ∨B2,1

                                ¬B2,1




                                                                                 86
```

## Slide 76

```text
The Goal Today
                                   B1,1 ⇒(B1,2 ∨B2,1)                                   B1,2 ⇒(B1,1 ∨B1,3 ∨B2,2)                                   B1,3 ⇒(B1,2 ∨B2,3)
3, 1          3, 2          3, 3                                   B2,1 ⇒(B1,1 ∨B2,2 ∨B3,1)   ?        ?        ?                B2,2 ⇒(B1,2 ∨B2,1 ∨B2,3 ∨B3,2)                                   B2,3 ⇒(B1,3 ∨B2,2 ∨B3,3)2, 1          2, 2          2, 3Empty      ?        ?                B3,1 ⇒(B3,2 ∨B2,1)                                   B3,2 ⇒(B3,1 ∨B3,3 ∨B2,2)
1, 1          1, 2          1, 3                                   B3,3 ⇒(B3,2 ∨B2,3)
  Hit        ?        ?
                                   B1,1                                   B1,2 ∨B2,1

                                ¬B2,1
                                   B1,2


                                                                                 87
```

## Slide 77

```text
The Goal Today
                                   B1,1 ⇒(B1,2 ∨B2,1)                                   B1,2 ⇒(B1,1 ∨B1,3 ∨B2,2)                                   B1,3 ⇒(B1,2 ∨B2,3)
3, 1          3, 2          3, 3                                   B2,1 ⇒(B1,1 ∨B2,2 ∨B3,1)   ?        ?        ?                B2,2 ⇒(B1,2 ∨B2,1 ∨B2,3 ∨B3,2)                                   B2,3 ⇒(B1,3 ∨B2,2 ∨B3,3)2, 1          2, 2          2, 3Empty      ?        ?                B3,1 ⇒(B3,2 ∨B2,1)                                   B3,2 ⇒(B3,1 ∨B3,3 ∨B2,2)
1, 1          1, 2          1, 3                                   B3,3 ⇒(B3,2 ∨B2,3)
  Hit        Hit        ?
                                   B1,1                                   B1,2 ∨B2,1

                                ¬B2,1
                                   B1,2


                                                                                 88
```

## Slide 78

```text
The Goal Today





                                                           89
```

## Slide 79

```text
Next Class

•  First-Order Logic





                                                                                   90
```
