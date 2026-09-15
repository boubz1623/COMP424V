# L1-Intro

> Source: [original PDF](<../slides/L1-Intro.pdf>) · 50 slides. Text extraction may omit figures and alter equations; check the PDF.

## Slide 1

```text
COMP 424 - Artificial Intelligence
             Fall 2026


             Lecture 1: Aug 31st, 2026
       Course Info and General AI Discussion

     Su Lin Blodgett (sulin.blodgett@mcgill.ca)
     Jackie CK Cheung (jackie.cheung@mcgill.ca)
```

## Slide 2

```text
About Us

•  Su Lin Blodgett
      •   Visiting researcher at Mila
      •  Researcher at Microsoft Research Montréal, 2020 – 2026
      •  Research topics: natural language processing, responsible NLP
      and AI, evaluation and measurement

•  Jackie CK Cheung
      •  Associate professor, at McGill since 2015
      •  Core member of Mila
      •  Research topics: natural language processing, text
       summarization and generation, computational pragmatics,
       evaluation of NLP systems




                                                                                  2
```

## Slide 3

```text
What is AI to you?

• When you hear the words “artificial intelligence”, what
  do you think of?





                                                                                  3
```

## Slide 4

```text
Do these seem like AI to you?

•  ChatGPT
•  Robot vacuum
•  Tic-tac-toe playing bot
•  Chess bot
•  NPC (Non-playable character) in a video game with
   scripted interactions
•  Calculator app
•  GPS navigation
•  Search engine

         Let’s come back to this, after the course intro!




                                                                                  4
```

## Slide 5

```text
About the Course

Textbook (Recommended):
    Russell & Norvig. “Artificial Intelligence:
   A Modern Approach”, 4th ed.

 We consider critical algorithms at the core of AI reasoning
   systems, of both historical and modern importance. Our
   focus is on AI for deliberative tasks including game playing, as
   well as probabilistic modeling and inference.
 This cannot be a comprehensive coverage of everything called
   AI today due to scope – Machine Learning, Vision, Robotics
  and RL are specifically excluded due to other McGill courses.





                                                                                    5
```

## Slide 6

```text
Course Topics of COMP 424

•  Uninformed Search                Warm up from 251
•  Informed search
•   Constraint satisfaction
                            Classical AI topics•   Partial information
   and stochastic search
•   AI for 2 player games
                   Game AI, project topic
•   Tree-based game solvers
•   Probabilistic reasoning
•   Learning probabilistic models
•   Causal probabilistic models                    Probabilistic
•  Reasoning with utilities                      representations
•   Sequential reasoning and decision-making                                Utility theory
•   Responsible AI





                                                                                   6
```

## Slide 7

```text
General Communication

•  Su Lin’s office hours: Mondays, time and location TBD

•  Jackie’s office hours: Wednesdays, 9:30 – 11am in MC
  108N

•  TAs will have office hours too (times and locations TBD)

• Use Ed discussion board for questions on content,
  technical queries, timing, etc.
• Use e-mail for personal issues





                                                                                   7
```

## Slide 8

```text
Evaluation

1. Individual assignments (20%)
2. Midterm (15%)
3. Final examinations (40%)
4. Final project: Implementation, check-ins, and written
   report (25%)





                                                                              8
```

## Slide 9

```text
Assignments (20%)

•  Four, roughly evenly spaced through term.
•  Analysis or problem solving related to course content
•  (Minimal) programming, problems, calculations
    •  When coding needed, will be flexible on language





                                                                                   9
```

## Slide 10

```text
Examinations

•  Midterm (15%) + Final (40%)
•  Midterm date TBD; awaiting booking

•  Final exams to be centrally scheduled, in person during
  exam period

•  Mix of multiple-choice and written answer
•  Closed-book but crib-sheet allowed





                                                                                    10
```

## Slide 11

```text
Course Project (25%)

•  Design and implement a game playing program.
•  Use ideas from the course to design your algorithm.
•  Basic code (for a random player) will be provided
•  Language of agent must be Python
•  Evaluation: results, ongoing check-ins, written report
• Two rounds of performance evaluation with opportunities to
  have feedback and refine your solution





                                                                                    11
```

## Slide 12

```text
Course Policies

•  Course work is individual unless otherwise stated. It is the
   responsibility of each student to understand the policy for
  the course and ask questions of the instructor if this is not
   clear.


•   It is the responsibility of each student to carefully
  acknowledge all sources (papers, code, books, websites,
   individual communications) using appropriate referencing
   style when submitting work.





                                                                                    12
```

## Slide 13

```text
Collaboration Guidelines

•  You are free to meet with fellow students(s) and discuss
  assignments with them. Writing on a board or shared
   piece of paper is acceptable during the meeting;
  however, you should not take any written (electronic or
   otherwise) record away from the meeting.

•  This applies when the assignment is supposed to be an
   individual effort or whenever two teams discuss common
  problems they are each encountering (inter-group
   collaboration).





                                                                                   13
```

## Slide 14

```text
Collaboration Guidelines

•  To assure that all collaboration is on the level, you must
  always write the name(s) of your collaborators on your
   assignment. This also applies when two groups
   collaborate.

•  Suggestion: After the meeting, engage in a half hour of
  mind-numbing activity (like watching an episode of The
   Office),before starting to work on the assignment. This
   will assure that you are able to reconstruct what you
   learned from the meeting, by yourself, using your own
   brain.





                                                                                   14
```

## Slide 15

```text
Use of Generative AI

•  Generative AI may be used in an assistive manner
•  Acceptable use examples:
           •  Help understand course content
           •   Search for relevant information
           •  Help brainstorm ideas
           •  Check for grammar and style errors in writing and in code
•  Unacceptable use examples:
           •  As primary means of completing assignments
           •  As primary means of completing project

•  Use must be declared and referenced in your
   submission!




                                                                                   15
```

## Slide 16

```text
Automated Plagiarism Detection

• We may use automated systems to detect possible cases
   of text or software plagiarism. Cases that warrant
   further investigation will be referred to the university
   disciplinary officers. Students who have concerns about
  how to properly use and acknowledge third-party
   software should consult the course instructor or TAs.

•  Unfortunately, we often detect and send cases of
   plagiarism to the office. This may delay your graduation!
  Do not do it! We have AI techniques at our disposal!





                                                                                    16
```

## Slide 17

```text
Acknowledgements

•  Course slides based on previous offerings of COMP 424:
     •  Doina Precup
     •  Joelle Pineau
     •  Jackie CK Cheung
     •  Dave Meger
     •  Golnoosh Farnadi
     •  Prakhar Ganesh





                                                                                    17
```

## Slide 18

```text
What is Intelligence?





                                                                18
```

## Slide 19

```text
Definition of Intelligence?

•  Definition is contested. May be multi-factorial – ask a
   psychologist or cognitive scientist!

Possible characteristics and aspects of intelligence:
•  Acquire, retain, and apply knowledge
•  Apply logic and reason
•  Be able to change and manipulate one’s environment
•  Be able to adapt, foresee, and plan
•  Be able to deal with uncertainty
•  Possible modalities of intelligence:
     •  Spatial, verbal, logical, musical, social, …




                                                                                    19
```

## Slide 20

```text
One Model: Biological Intelligence

•  Sensory processing:
     •  Visual cortex
     •  Auditory cortex
     •  Somatosensory cortex
• Motor cortex
•  Cognitive functions:
     • Memory
     •  Reasoning
     •  Executive control
     •  Learning
     •  Language





                                                                                    20
```

## Slide 21

```text
Characteristics of Biological
              Intelligence
• A mix of domain-general and domain-specific capabilities
•  Domain-general:
     • Memory formation, updating, retrieval
     •  Learning new tasks
•  Domain-specific:
     •  Recognizing visual patterns
     •  Recognizing sounds
     •  Learning language





                                                                                    21
```

## Slide 22

```text
What is AI?





                                                      22
```

## Slide 23

```text
What is AI?





                                                      23
```

## Slide 24

```text
What is AI?

Human intelligence:
•  Sensory processing:
     •  Visual cortex
     •  Auditory cortex
     •  Somatosensory cortex
• Motor cortex
•  Cognitive functions
     • Memory
     •  Reasoning
     •  Executive control
     •  Learning
     •  Language




                                                                                    24
```

## Slide 25

```text
What is AI?

Human intelligence:          Artificial Intelligence:
•  Sensory processing:     •  Visual cortex       →     Computer vision     •  Auditory cortex      →      Signal/speech processing     •  Somatosensory cortex   →      Haptics• Motor cortex        →      Robotics
•  Cognitive functions     • Memory         →     Knowledge representation     •  Reasoning         →      Search, inference     •  Executive control     →       Planning, decision-making     •  Learning         →     Model learning     •  Language         →      Language understanding




                                                                                    25
```

## Slide 26

```text
What is AI?

Human intelligence:          Artificial Intelligence:
•  Sensory processing:     •  Visual cortex       →     Computer vision     •  Auditory cortex      →      Signal/speech processing     •  Somatosensory cortex   →      Haptics• Motor cortex        →      Robotics
•  Cognitive functions     • Memory         →     Knowledge representation     •  Reasoning         →      Search, inference     •  Executive control     →      Planning, decision-making     •  Learning         →     Model learning     •  Language         →      Language understanding




                                                                                    26
```

## Slide 27

```text
Possible Goals of AI

•  Modeling or replicating human cognition using computers
•  Replicating human behaviours using computers
•  Studying problems that others don’t know how to solve
     •  Cool stuff!
           • Game playing, machine learning, data mining, speech recognition,
          computer vision, web agents, robots
     •  Useful stuff!
           • Medical diagnosis, fraud detection, genome analysis, object
             identification, space shuttle scheduling, information retrieval





                                                                                    27
```

## Slide 28

```text
Goals of AI





Thinking      Thinking
Humanly      Rationally


 Acting         Acting
Humanly      Rationally





                                                           28
```

## Slide 29

```text
Goals of AI

Let’s first consider these boxes



                  Thinking      Thinking
               Humanly      Rationally


                   Acting         Acting
               Humanly      Rationally





                                                                                       29
```

## Slide 30

```text
Potential Issues

•  What does it mean to “think humanly”?
      •  Studied in cognitive science
      •  Can use computational methods to model and study this!
      •  Not the focus of this course!
      •   Also: can an AI have a mind and consciousness? No agreed
        definition and test!

•  What does it mean to “think rationally”?
      •  Possible answer: use a well-understood and described logic
       system.
      •   Is this the right goal for developing intelligent systems?





                                                                                   30
```

## Slide 31

```text
Goals of AI





                    Thinking      Thinking
                Humanly      Rationally
What about this?

                     Acting         Acting
                Humanly      Rationally





                                                                                           31
```

## Slide 32

```text
Acting Humanly


•  AI is about duplicating what the (human) brain DOES.

•  Alan Turing (1912-1954) had interesting thoughts about this.

   Can a machine think?  ->  If it could, how would we tell?

                                   Turing (1950): “Computing machinery and intelligence”


       Human interrogator                               ?           Human



                                                    AI agent


       An operator interacts with either the human or the AI agent.
        Can he correctly guess which one?


                                                                                    32
```

## Slide 33

```text
Turing’s Prediction

•  By 2000, a machine would have a 30% chance of fooling a
   lay person for 5 minutes.
    •  This actually happened in 2014:
      http://www.bbc.com/news/technology-27762088
     •  Does this mean that we have solved AI?

•  Suggested major components of AI:
     •  Knowledge representation, automated reasoning, language
       understanding, machine learning





                                                                                    33
```

## Slide 34

```text
AI = Acting Humanly?

• Humans have biological resource constraints
     •  Limited memory, thinking speed, attention span…
• Humans are not necessarily the gold standard!
• Humans are often “irrational”
     •  Or else we do not understand our own notion of rationality
     •  e.g., don't act towards our own goals; hold contradictory beliefs
       or preferences
     • Kahneman and Tversky demonstrate ways that people are
       systematically irrational.





                                                                                    34
```

## Slide 35

```text
Different Goals of AI





   Thinking      Thinking
   Humanly      Rationally

                                                Let’s try this!
     Acting         Acting
   Humanly      Rationally





                                                                35
```

## Slide 36

```text
Acting Rationally

•  Rational behaviour = doing the “right” thing.

•  Doing what is expected to maximize goal achievement,
   given the available information and available resources.



           This is the flavour of AI we will focus on.


    Who gets to decide what is the “right” thing?
     – A question to ponder.




                                                                                    36
```

## Slide 37

```text
Finally, Our Working Definition of AI




Developing models and algorithms that can produce rational
behaviours in response to incoming stimuli and information.





                                                                                    37
```

## Slide 38

```text
Does this change your views?

•  ChatGPT
•  Robot vacuum
•  Tic-tac-toe playing bot
•  Chess bot
•  NPC (Non-playable character) in a video game with
   scripted interactions
•  Calculator app
•  GPS navigation
•  Search engine





                                                                                   38
```

## Slide 39

```text
Different Goals of AI





   Thinking      Thinking
   Humanly      Rationally


     Acting         Acting
   Humanly      Rationally





                                                                39
```

## Slide 40

```text
Rational Agents

•  This course is about designing rational agents.
     • An agent is an entity that perceives and acts.
     •  Goal: Learn a function mapping percept histories to actions:
            f : Ph → A
• A rational agent implements this function such as to maximize
  performance.
     •  Performance measures: goal achievement, resource consumption, ...
 •  Caveat: Resource constraints (time, space, energy,
   bandwidth, …) which make perfect rationality unachievable
 •  Objective: Find best function for given information and
   resources





                                                                                    40
```

## Slide 41

```text
Note on Terminology

•  What terms have we used that could be applied to both
   AI and humans?
      •   E.g., “rational”





•  What assumptions may differ when applying the same
  term to the two?





                                                                                   41
```

## Slide 42

```text
What is AI?





                                                      42
```

## Slide 43

```text
How is "AI" being used?





                                                                     43
```

## Slide 44

```text
AI Beginnings

•  Pre/early compute:
    •  Feedback devices enable water supply, steam power, encryption
      and code breaking
    •  Devices provide automation not computation. Can never surpass
        creator’s understanding

•  ENIAC: First super-computer, created in 1946.
•  Early work in 1950s:
     •  Rosenblatt’s perceptron
     •  Samuel’s checkers player

•  AI successes come in many waves




                                                                                    44
```

## Slide 45

```text
Dartmouth Conference (1956)





                                                                          45
```

## Slide 46

```text
Dartmouth Conference (1956)

• Some of the attendees:
     •  John McCarthy: LISP, time-sharing, application of logic
       to reasoning
     •  Marvin Minsky: popularized neural networks and
      showed their limits, introduced slots and frames
     •  Claude Shannon: information theory, juggling machine
     •  Allen Newell and Herb Simon: bounded rationality,
       general problem solver, SOAR

•  The meeting coined the
  term “artificial intelligence''





                                                                                        46
```

## Slide 47

```text
Early AI Hopes and Dreams

• Make programs that exhibit similar signs of intelligence as
   people: prove theorems, play chess, have a conversation.

•  Logical reasoning was key.
•  Learning from experience was considered important.
•  The research agenda was geared towards building general
  problem solvers.

•  There was a lot of hope that natural language could be
   easily understood and processed.





                                                                                    47
```

## Slide 48

```text
AI Downswings

•  Early successes did not scale up!
     • Demos were impressive, but only worked in a narrow domain
     •  e.g., Machine translation for general texts

1966         Perceived failure of machine translation
1973, 1974   Major cut in AI research funding
1987-1993    “AI Winter”: many companies working in AI
                   fail

• Much progress actually made in this period, but
  overpromising of results led to disappointments




                                                                                    48
```

## Slide 49

```text
Recent AI: Statistical Techniques

•  Heavy use of probability theory, decision theory, statistics.
•  Trying to solve specific problems rather than aim for general
   reasoning.
•  AI today is a collection of sub-fields:
     •  Perception and computer vision.
     •  Natural language understanding.
     •  Robotics
     •  Etc.
• Deep learning unleashed a further wave of enthusiasm about
  AI progress (especially 2014 onwards)
•  Recent claims that large language models and multi-modal
  models surpass the problem-specific limitation and are
  moving towards “general” intelligence or even
   “superintelligence”.                                                                                    49
```

## Slide 50

```text
Next Class

•  Start with discussion of search as a fundamental
  paradigm for AI!

•  Starting next week (Sept 9), we'll be in MCMED 522.





                                                                                   50
```
