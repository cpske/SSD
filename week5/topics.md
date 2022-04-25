## Elaboration

In a course on OO Analysis & Design, the Elaboration phase is central.

### You Should Know Well

1. Summary of Inception Phase Activities and Outputs in section 8.1 (p. 121).
   - Activities
     * (short) requirements workshop
     * "proof of concept" code written to explore special or risky requirements
     * create UI prototypes to clarify vision
     * identify high-level candidate architecture
     * plan the first (elaboration) iteration 
   - Artifacts
     * most actors and goals
     * most use cases named & written in brief form
     * most influential & risky requirements identified
     * Vision & Suplementary Spec version 1 written
     * risk list
     * recommendation of what to build versus buy or reuse
     * Iteration Plan

2. Goals of Elaboration in section 8.2 (p. 109, PDF 122).

3. Key Practices and Activities in Elaboration (p. 122).
   - do short timeboxed, risk-driven iterations
   - start programming early
   - adaptively design, implement, and test core and risky parts of the architecture
   - test early, often, realistically
   - adapt based on feedback from tests, users, developers
   - write most of the use cases and other requirements in detail
   - hold one workshop per iteration to develop use cases and other requirements in detail


## Exercise

- Identify Domain classes

- Draw a domain class diagram

- Draw a system sequence diagram

- What is Representational Gap?  Is it good or bad?
  p 146: Representational Gap [is] the gap between our mental model of the
  domain and its representation in software.

- Conceptual, Software, & Design classes.

  Conceptual class - represents a real-world concept or thing.  The Domain Model contains conceptual classes. Also called Domain concepts.
  Software class or Design class - a class in the software design, not tied to a particular implementation.
  Implementation class - a class implemented in an OO language such as Java.

  > A domain model is a visualization of things in the real-world domain of interest,
  > not of software components, or software objects with responsibilities.
  > The following are **not** suitable in a domain model
  > - software artifacts such as a window or database
  > - responsibilities or methods

- How to Find Conceptual Classes
  1. use a category list
  2. look for noun phrases (in Use Cases and other requirements)
  3. use an existing model, such as from *Analysis Patterns* (Martin Fowler)

- Suggest a free UML diagram editor.  Need class and sequence diagrams. State chart is also desirable.

## UML "Classes" versus software Classes

(Larman v2, p. 145)

>In the raw UML, the rectangular boxes shown in Figure 10.9 are called classes,
>but note that in the UML, this term encompasses a variety of phenomenon—
>physical things, software things, events, and so forth. 
>
>A process or method will superimpose alternative terminology on top of the UML.
>For example, in the UP, when the UML boxes are drawn in the Domain Model, 
>they may be called domain concepts or conceptual classes; the Domain Model 
>offers a conceptual perspective. 
>In the UP, when UML boxes are drawn in the Design Model, they are officially 
>called design classes; the Design Model offers a specification
>or implementation perspective, as desired by the modeler.



